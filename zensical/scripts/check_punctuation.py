#!/usr/bin/env python3
"""Report em dashes and semicolons in the prose of Markdown content files.

This is a reviewer aid for the mechanics-and-rhythm pass in
`zensical/references/article-review.md`, which owns the density judgment. The
scan counts prose only: YAML front matter, fenced code blocks (``` and ~~~),
and inline code spans are stripped before counting. It reports candidates and
never edits or rewrites content.

A mark inside a quoted title can be legitimate prose punctuation; the USENIX
`;login:` publication name is the usual example. Such marks still appear as
findings, and a reviewer clears them by judgment. The script deliberately does
not special-case any title or pattern.

Exit codes: 0 clean, 1 findings, 2 the check could not run.
"""

from __future__ import annotations

import argparse
from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path
import re
import sys
import tempfile

EM_DASH = "\u2014"
SEMICOLON = ";"
MARKDOWN_SUFFIXES = frozenset({".md", ".markdown"})
SKIPPED_DIRECTORIES = frozenset({".git", "node_modules", "site", "public", "dist", ".output"})
FENCE = re.compile(r"^[ \t]{0,3}(`{3,}|~{3,})")
INLINE_CODE = re.compile(r"(`+)(.+?)\1")
LINK_TARGET = re.compile(r"\]\([^)]*\)")


class CheckError(RuntimeError):
    """The check could not run, as opposed to finding a problem."""


@dataclass(frozen=True)
class Finding:
    """One candidate mark, with its source line and trimmed text."""

    line: int
    mark: str
    text: str


@dataclass(frozen=True)
class FileReport:
    """Prose punctuation counts and findings for one Markdown file."""

    path: Path
    em_dashes: int
    semicolons: int
    prose_words: int
    findings: tuple[Finding, ...]

    @property
    def density(self) -> float:
        """Candidate marks per 1,000 prose words."""
        if self.prose_words == 0:
            return 0.0
        return (self.em_dashes + self.semicolons) * 1000 / self.prose_words


def prose_lines(text: str) -> Iterator[tuple[int, str]]:
    """Yield (line number, text) for lines outside front matter and fences."""
    lines = text.splitlines()
    start = 0
    if lines and lines[0].strip() == "---":
        for index in range(1, len(lines)):
            if lines[index].strip() in {"---", "..."}:
                start = index + 1
                break
        else:
            return

    fence_char = ""
    fence_length = 0
    for index in range(start, len(lines)):
        line = lines[index]
        fence = FENCE.match(line)
        if fence_char:
            if (
                fence
                and fence.group(1)[0] == fence_char
                and len(fence.group(1)) >= fence_length
                and line.strip() == fence.group(1)
            ):
                fence_char = ""
            continue
        if fence:
            fence_char = fence.group(1)[0]
            fence_length = len(fence.group(1))
            continue
        yield index + 1, line


def scan_text(path: Path, text: str) -> FileReport:
    """Count prose punctuation and record each candidate mark."""
    findings: list[Finding] = []
    em_dashes = 0
    semicolons = 0
    prose_words = 0
    for line_number, line in prose_lines(text):
        prose = INLINE_CODE.sub("", line)
        prose_words += len(LINK_TARGET.sub("]", prose).split())
        line_em_dashes = prose.count(EM_DASH)
        line_semicolons = prose.count(SEMICOLON)
        em_dashes += line_em_dashes
        semicolons += line_semicolons
        findings.extend(Finding(line_number, "em dash", line.strip()) for _ in range(line_em_dashes))
        findings.extend(Finding(line_number, "semicolon", line.strip()) for _ in range(line_semicolons))
    return FileReport(path, em_dashes, semicolons, prose_words, tuple(findings))


def markdown_files(target: Path) -> list[Path]:
    """Return Markdown files for one target, skipping generated directories."""
    if target.is_file():
        if target.suffix.lower() not in MARKDOWN_SUFFIXES:
            raise CheckError(f"not a Markdown file: {target}")
        return [target]
    if not target.is_dir():
        raise CheckError(f"no such file or directory: {target}")

    files: list[Path] = []
    for path in sorted(target.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in MARKDOWN_SUFFIXES:
            continue
        relative_parts = path.relative_to(target).parts[:-1]
        if SKIPPED_DIRECTORIES.intersection(relative_parts):
            continue
        files.append(path)
    return files


def scan_targets(targets: list[Path]) -> list[FileReport]:
    """Scan every Markdown file under the given file or directory targets."""
    reports: list[FileReport] = []
    for target in targets:
        for path in markdown_files(target):
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeError) as error:
                raise CheckError(f"could not read {path}: {error}") from error
            reports.append(scan_text(path, text))
    return reports


def emit_report(reports: list[FileReport]) -> int:
    """Print per-file counts and findings, then return the exit code."""
    total_em_dashes = sum(file_report.em_dashes for file_report in reports)
    total_semicolons = sum(file_report.semicolons for file_report in reports)
    total_words = sum(file_report.prose_words for file_report in reports)

    for file_report in reports:
        print(
            f"{file_report.path}: em dashes {file_report.em_dashes}, "
            f"semicolons {file_report.semicolons}, prose words {file_report.prose_words}, "
            f"density {file_report.density:.1f}/1000 words"
        )
        for finding in file_report.findings:
            print(f"  line {finding.line} [{finding.mark}]: {finding.text}")

    total_marks = total_em_dashes + total_semicolons
    total_density = total_marks * 1000 / total_words if total_words else 0.0
    print(
        f"Summary: {len(reports)} file(s), {total_words} prose words, "
        f"{total_em_dashes} em dash(es), {total_semicolons} semicolon(s), "
        f"density {total_density:.1f}/1000 words"
    )
    if total_marks:
        print(f"FAIL: {total_marks} candidate punctuation mark(s) found")
        return 1
    print("PASS: no em dashes or semicolons in prose")
    return 0


def self_test() -> int:
    """Exercise known counts, exclusion rules, and the missing-path boundary."""
    known = "# Heading\n\nOne \u2014 two \u2014 three; four; five.\n"
    excluded = (
        "---\n"
        'title: "Front \u2014 matter; here"\n'
        "---\n\n"
        "Prose stays clean.\n\n"
        "```text\n"
        "code \u2014 ;\n"
        "```\n\n"
        "~~~text\n"
        "more \u2014 ;\n"
        "~~~\n\n"
        "Inline `code \u2014 ;` is excluded.\n"
    )

    with tempfile.TemporaryDirectory() as temporary_directory:
        root = Path(temporary_directory)
        (root / "known.md").write_text(known, encoding="utf-8")
        (root / "excluded.markdown").write_text(excluded, encoding="utf-8")

        by_name = {file_report.path.name: file_report for file_report in scan_targets([root])}

        known_report = by_name["known.md"]
        assert known_report.em_dashes == 2
        assert known_report.semicolons == 2
        assert known_report.prose_words > 0
        print("PASS: known em-dash and semicolon counts are reported")

        excluded_report = by_name["excluded.markdown"]
        assert excluded_report.em_dashes == 0
        assert excluded_report.semicolons == 0
        assert excluded_report.prose_words > 0
        print("PASS: front matter, fenced blocks, and inline code are excluded")

        try:
            scan_targets([root / "missing.md"])
        except CheckError:
            print("PASS: a missing path is an exit-2 condition")
        else:
            raise AssertionError("missing path did not raise CheckError")

    print("PASS: punctuation self-test")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Report em dashes and semicolons in Markdown prose.")
    parser.add_argument("targets", nargs="*", type=Path, metavar="PATH")
    parser.add_argument("--self-test", action="store_true")
    arguments = parser.parse_args(argv)

    if arguments.self_test:
        return self_test()
    if not arguments.targets:
        parser.print_usage(sys.stderr)
        print("error: at least one target path is required", file=sys.stderr)
        return 2

    try:
        reports = scan_targets(arguments.targets)
    except CheckError as error:
        print(f"Punctuation check could not run: {error}", file=sys.stderr)
        return 2
    return emit_report(reports)


if __name__ == "__main__":
    raise SystemExit(main())

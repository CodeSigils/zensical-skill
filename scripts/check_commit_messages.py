#!/usr/bin/env python3
"""Check commit subjects and rationale fields for this repository."""

from __future__ import annotations

import subprocess
import sys

SUBJECT_LIMIT = 72
FIELDS = ("what:", "why:")


def run(*args: str) -> str:
    """Return command output, or raise RuntimeError with git's own message."""
    result = subprocess.run(args, text=True, capture_output=True)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"{' '.join(args)} failed")
    return result.stdout


def resolve(refs: list[str]) -> list[str]:
    """Return the commit hashes named by refs, in log order, without duplicates.

    A range lists every commit it covers; a bare ref names exactly one. `git log
    HEAD` would walk the entire history, so a single ref is resolved directly
    instead.
    """
    hashes: list[str] = []
    seen: set[str] = set()
    for ref in refs:
        listed = (
            run("git", "log", "--format=%H", ref)
            if ".." in ref
            else run("git", "rev-parse", "--verify", f"{ref}^{{commit}}")
        )
        for line in listed.splitlines():
            if line and line not in seen:
                seen.add(line)
                hashes.append(line)
    return hashes


def field_value(body_lines: list[str], field: str) -> str | None:
    """Return the text after field on the first body line that starts with it.

    Anchoring at the start of a line is what makes the check meaningful: a
    mention of the word mid-sentence is prose, not a field. %b is used to read
    the body so a subject line can never satisfy the requirement.
    """
    for line in body_lines:
        if line.lower().startswith(field):
            return line.split(":", 1)[1].strip()
    return None


def check(commit: str) -> list[str]:
    short = commit[:12]
    subject = run("git", "show", "--quiet", "--format=%s", commit).strip()
    body = run("git", "show", "--quiet", "--format=%b", commit).strip()

    errors: list[str] = []
    if not subject:
        errors.append(f"{short}: empty subject")
    elif len(subject) > SUBJECT_LIMIT:
        errors.append(f"{short}: subject exceeds {SUBJECT_LIMIT} characters")
    elif subject.endswith("."):
        errors.append(f"{short}: subject must not end with a period")

    body_lines = body.splitlines()
    for field in FIELDS:
        value = field_value(body_lines, field)
        if value is None:
            errors.append(f"{short}: missing {field} field")
        elif not value:
            errors.append(f"{short}: empty {field} field")
    return errors


def main() -> int:
    refs = sys.argv[1:] or ["HEAD"]
    try:
        hashes = resolve(refs)
    except RuntimeError as exc:
        print(f"Commit message policy could not run: {exc}", file=sys.stderr)
        return 2

    errors: list[str] = []
    for commit in hashes:
        errors.extend(check(commit))

    if errors:
        print("Commit message policy failed:", file=sys.stderr)
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Commit message policy passed for {len(hashes)} commit(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

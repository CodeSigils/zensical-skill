#!/usr/bin/env python3
"""Check that the README's file trees still match the repository.

The README inventories the runtime payload and the repository layout by hand.
That is a duplicated value, and duplicated values drift: a payload file added in
one commit is invisible to a reader of the README until someone re-reads it.

This check compares only the directories a tree *expands*. A directory listed
without children is a deliberate summary, so it is not compared. That keeps the
check from demanding the README document directories the tree deliberately omits.

Exit codes: 0 clean, 1 findings, 2 the check could not run.
"""

from __future__ import annotations

import re
import subprocess
import sys
import tempfile
from pathlib import Path

COMMENT = re.compile(r"\s+#.*$")
TREE_BRANCH = re.compile(r"^(?P<indent>[│ ]   )?(?P<branch>├── |└── )(?P<name>.+)$")


class CheckError(RuntimeError):
    """The check could not run, as opposed to finding a problem."""


def run(*args: str) -> str:
    """Return command output, or raise CheckError with git's own message.

    A missing git binary raises FileNotFoundError, which is translated here so
    the caller has one exception type to handle rather than two.
    """
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=False)
    except FileNotFoundError as error:
        raise CheckError(f"{args[0]} is not available on this host") from error
    if result.returncode != 0:
        raise CheckError(result.stderr.strip() or f"{args[0]} failed")
    return result.stdout


def tracked_files(root: Path) -> set[str]:
    output = run("git", "-C", str(root), "ls-files", "-z")
    return {entry for entry in output.split("\0") if entry}


def strip_comment(line: str) -> str:
    return COMMENT.sub("", line)


def parse_trees(markdown: str) -> list[list[tuple[int, bool, str]]]:
    """Return every fenced block that actually contains tree branches.

    Entries are (column, is_bare_root, name). A block with no branch characters
    is a command sample, not an inventory, and is skipped.
    """
    trees: list[list[tuple[int, bool, str]]] = []
    entries: list[tuple[int, bool, str]] = []
    saw_branch = False
    in_fence = False

    def flush() -> None:
        if saw_branch and entries:
            trees.append(list(entries))

    for raw in markdown.splitlines():
        if raw.lstrip().startswith("```"):
            if in_fence:
                flush()
            entries.clear()
            saw_branch = False
            in_fence = not in_fence
            continue
        if not in_fence:
            continue

        branch = TREE_BRANCH.match(raw)
        if branch:
            saw_branch = True
            column = len(branch.group("indent") or "")
            name = strip_comment(branch.group("name")).strip()
            if name:
                entries.append((column, False, name))
            continue

        name = strip_comment(raw).strip()
        if name:
            # A bare line names a root, and its children sit one column in.
            entries.append((0, True, name))

    if in_fence:
        flush()
    return trees


def nest(entries: list[tuple[int, bool, str]]) -> dict[str, object]:
    """Turn flat tree entries into nested dicts; leaves become their own name."""
    root: dict[str, object] = {}
    stack: list[tuple[int, dict[str, object]]] = [(-2, root)]

    for column, is_bare, name in entries:
        effective = column - 1 if is_bare else column
        while len(stack) > 1 and stack[-1][0] >= effective:
            stack.pop()
        parent = stack[-1][1]
        if name.endswith("/"):
            node: dict[str, object] = {}
            parent[name.rstrip("/")] = node
            stack.append((effective, node))
        else:
            parent[name] = name
    return root


def real_children(files: set[str], directory: str) -> set[str] | None:
    """Immediate child names of a tracked directory, or None if not a directory."""
    prefix = f"{directory}/" if directory else ""
    children: set[str] = set()
    found = False
    for path in files:
        if not path.startswith(prefix):
            continue
        remainder = path[len(prefix) :]
        if not remainder:
            continue
        found = True
        head = remainder.split("/", 1)[0]
        children.add(head)
    return children if found or directory == "" else None


def compare(
    documented: dict[str, object],
    files: set[str],
    directory: str,
    findings: list[str],
) -> None:
    """Compare one expanded directory level; recurse only into expanded children."""
    actual = real_children(files, directory)
    if actual is None:
        findings.append(f"{directory or '.'}: documented as a directory, but no tracked files live there")
        return

    for name in sorted(documented):
        node = documented[name]
        path = f"{directory}/{name}" if directory else name
        is_directory = isinstance(node, dict)

        if not is_directory and "/" in name:
            # A leaf written as a path, such as agents/openai.yaml, is checked
            # against the file list rather than against its sibling names.
            if path in files or any(f.startswith(f"{path}/") for f in files):
                continue
            findings.append(f"{path}: listed in the README but not tracked in the repository")
            continue

        if name not in actual:
            findings.append(f"{path}: listed in the README but not tracked in the repository")
            continue

        real_is_dir = any(f.startswith(f"{path}/") for f in files)
        if is_directory and not real_is_dir:
            findings.append(f"{path}: documented as a directory but tracked as a file")
        elif real_is_dir and not is_directory:
            continue  # A collapsed directory is a deliberate summary, not a claim.
        elif is_directory and node:
            compare(node, files, path, findings)

    # A path leaf stands in for its first segment, so agents/openai.yaml counts
    # as a mention of agents when looking for children the tree failed to list.
    documented_names = {name.split("/", 1)[0] for name in documented}
    for name in sorted(actual - documented_names):
        findings.append(f"{directory}/{name}: tracked in the repository but missing from the README tree")


def check(root: Path, readme: Path) -> int:
    files = tracked_files(root)
    trees = parse_trees(readme.read_text())
    if not trees:
        raise CheckError(f"no file tree found in {readme}")

    findings: list[str] = []
    for entries in trees:
        for name, node in nest(entries).items():
            if isinstance(node, dict):
                if node:
                    compare(node, files, name, findings)
            else:
                if node not in files and not any(f.startswith(f"{node}/") for f in files):
                    findings.append(f"{name}: listed in the README but not tracked in the repository")

    if findings:
        print("README inventory does not match the repository:")
        for finding in findings:
            print(f"  - {finding}")
        return 1

    print(f"README inventory matches the repository ({len(trees)} tree(s) checked).")
    return 0


def self_test() -> int:
    readme = "README.md"
    tree = """pkg/
├── SKILL.md
└── references/
    ├── a.md
    └── b.md"""

    def project(target_root: Path, files: dict[str, str]) -> None:
        for name, body in files.items():
            target = target_root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(body)

    cases: list[tuple[str, dict[str, str], int]] = [
        ("matching tree passes", {
            "README.md": f"# t\n\n```text\n{tree}\n```\n",
            "pkg/SKILL.md": "a\n",
            "pkg/references/a.md": "a\n",
            "pkg/references/b.md": "b\n",
        }, 0),
        ("a new payload file is reported", {
            "README.md": f"# t\n\n```text\n{tree}\n```\n",
            "pkg/SKILL.md": "a\n",
            "pkg/references/a.md": "a\n",
            "pkg/references/b.md": "b\n",
            "pkg/references/c.md": "c\n",
        }, 1),
        ("a removed payload file is reported", {
            "README.md": f"# t\n\n```text\n{tree}\n```\n",
            "pkg/SKILL.md": "a\n",
            "pkg/references/a.md": "a\n",
        }, 1),
        ("a new directory is reported", {
            "README.md": f"# t\n\n```text\n{tree}\n```\n",
            "pkg/SKILL.md": "a\n",
            "pkg/references/a.md": "a\n",
            "pkg/references/b.md": "b\n",
            "pkg/scripts/run.sh": "#!/bin/sh\n",
        }, 1),
        ("a collapsed directory is not descended into", {
            "README.md": "# t\n\n```text\npkg/\n├── SKILL.md\n└── references/  # loaded on demand\n```\n",
            "pkg/SKILL.md": "a\n",
            "pkg/references/a.md": "a\n",
            "pkg/references/b.md": "b\n",
        }, 0),
        ("a leaf written as a path is checked as a path", {
            "README.md": "# t\n\n```text\npkg/\n├── agents/openai.yaml\n└── SKILL.md\n```\n",
            "pkg/SKILL.md": "a\n",
            "pkg/agents/openai.yaml": "a\n",
        }, 0),
        ("a leaf written as a path that does not exist is reported", {
            "README.md": "# t\n\n```text\npkg/\n├── agents/gone.yaml\n└── SKILL.md\n```\n",
            "pkg/SKILL.md": "a\n",
            "pkg/agents/openai.yaml": "a\n",
        }, 1),
        ("a listed top-level file that does not exist is reported", {
            "README.md": "# t\n\n```text\npkg/\n\u2514\u2500\u2500 SKILL.md\nMISSING.md\n```\n",
            "pkg/SKILL.md": "a\n",
        }, 1),
        ("a tree block with no branches is ignored", {
            "README.md": "# t\n\n```text\nnpx skills add owner/repo\n```\n\n"
                         "```text\npkg/\n\u251c\u2500\u2500 SKILL.md\n```\n",
            "pkg/SKILL.md": "a\n",
        }, 0),
    ]

    failures = 0
    for label, files, expected in cases:
        with tempfile.TemporaryDirectory() as sandbox:
            case_root = Path(sandbox)
            project(case_root, files)
            run("git", "-C", str(case_root), "init", "--quiet")
            run("git", "-C", str(case_root), "add", "--all")
            actual = check(case_root, case_root / readme)
            verdict = "ok" if actual == expected else "FAILED"
            if actual != expected:
                failures += 1
            print(f"  [{verdict}] {label}: expected {expected}, got {actual}")

    if failures:
        print(f"self-test failed: {failures} case(s) did not behave as specified")
        return 1
    print(f"self-test passed: {len(cases)} cases")
    return 0


def main(argv: list[str]) -> int:
    try:
        if "--self-test" in argv:
            return self_test()
        return check(Path.cwd(), Path.cwd() / "README.md")
    except CheckError as error:
        print(f"README inventory check could not run: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

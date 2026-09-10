#!/usr/bin/env python3
"""Check documented Zensical deployment instructions against a docs workflow."""

from __future__ import annotations

import argparse
from pathlib import Path
import tempfile


REQUIRED_TEXT = (
    "docs/**",
    "zensical.toml",
    "pyproject.toml",
    "uv.lock",
    ".python-version",
    ".github/workflows/docs.yml",
    "uv sync --locked",
    "uv run zensical build --clean",
)


def missing_contract_text(repository: Path) -> list[str] | None:
    """Return missing documented workflow details, or None when not applicable."""
    instructions = repository / "AGENTS.md"
    workflow = repository / ".github" / "workflows" / "docs.yml"
    if not instructions.is_file() or not workflow.is_file():
        return None

    instruction_text = instructions.read_text(encoding="utf-8")
    if "## Deployment" not in instruction_text:
        return None

    workflow_text = workflow.read_text(encoding="utf-8")
    return [
        value
        for value in REQUIRED_TEXT
        if value in workflow_text and value not in instruction_text
    ]


def self_test() -> int:
    with tempfile.TemporaryDirectory() as temporary_directory:
        repository = Path(temporary_directory)
        workflow = repository / ".github" / "workflows"
        workflow.mkdir(parents=True)
        (workflow / "docs.yml").write_text("\n".join(REQUIRED_TEXT), encoding="utf-8")
        (repository / "AGENTS.md").write_text(
            "## Deployment\n" + "\n".join(REQUIRED_TEXT), encoding="utf-8"
        )
        assert missing_contract_text(repository) == []
        (repository / "AGENTS.md").write_text("## Deployment\n", encoding="utf-8")
        assert missing_contract_text(repository) == list(REQUIRED_TEXT)
    print("PASS: instruction-contract self-test")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compare AGENTS.md deployment instructions with .github/workflows/docs.yml."
    )
    parser.add_argument("repository", nargs="?", default=".", type=Path)
    parser.add_argument("--self-test", action="store_true")
    arguments = parser.parse_args()
    if arguments.self_test:
        return self_test()

    missing = missing_contract_text(arguments.repository)
    if missing is None:
        print("SKIP: no AGENTS.md deployment section and conventional docs workflow pair")
        return 0
    if missing:
        print("FAIL: deployment instructions omit workflow details:")
        for value in missing:
            print(f"- {value}")
        return 1
    print("PASS: documented deployment contract matches the conventional docs workflow")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

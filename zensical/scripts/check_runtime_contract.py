#!/usr/bin/env python3
"""Keep the portable runtime's shared routing contract linked from each guide."""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path


PAYLOAD = Path(__file__).resolve().parents[1]
REFERENCE_NAMES = tuple(
    sorted(path.name for path in (PAYLOAD / "references").glob("*.md") if path.name != "source-registry.md")
)
METHOD_HEADING = "## Shared target-first method"
METHOD_LINK = "[shared target-first method](../SKILL.md#shared-target-first-method)"
VALIDATION_BOUNDARY_MARKERS = (
    "build verifies generation",
    "rendered inspection verifies affected presentation",
    "neither verifies deployment or indexing",
)


def missing_contracts(payload: Path) -> list[str]:
    """Return missing shared-method markers for one portable payload."""
    missing: list[str] = []
    skill_path = payload / "SKILL.md"
    skill_text = skill_path.read_text(encoding="utf-8") if skill_path.is_file() else ""
    if not skill_path.is_file() or METHOD_HEADING not in skill_text:
        missing.append("SKILL.md lacks the shared target-first method")
    for marker in VALIDATION_BOUNDARY_MARKERS:
        if marker not in skill_text:
            missing.append(f"SKILL.md lacks validation boundary marker: {marker}")
    references_dir = payload / "references"
    reference_names = tuple(
        sorted(path.name for path in references_dir.glob("*.md") if path.name != "source-registry.md")
    )
    for name in reference_names:
        reference = references_dir / name
        if not reference.is_file() or METHOD_LINK not in reference.read_text(encoding="utf-8"):
            missing.append(f"references/{name} lacks the shared target-first link")
    return missing


def self_test() -> int:
    """Exercise both the passing and failing contract paths."""
    with tempfile.TemporaryDirectory() as temporary_directory:
        payload = Path(temporary_directory)
        references = payload / "references"
        references.mkdir()
        skill_body = METHOD_HEADING + "\n" + "\n".join(VALIDATION_BOUNDARY_MARKERS)
        (payload / "SKILL.md").write_text(skill_body, encoding="utf-8")
        for name in REFERENCE_NAMES:
            (references / name).write_text(METHOD_LINK, encoding="utf-8")
        (references / "source-registry.md").write_text("registry", encoding="utf-8")
        assert missing_contracts(payload) == []
        (references / REFERENCE_NAMES[0]).write_text("missing", encoding="utf-8")
        assert missing_contracts(payload) == [
            f"references/{REFERENCE_NAMES[0]} lacks the shared target-first link"
        ]
        (references / REFERENCE_NAMES[0]).write_text(METHOD_LINK, encoding="utf-8")
        (payload / "SKILL.md").write_text(METHOD_HEADING, encoding="utf-8")
        missing = missing_contracts(payload)
        assert missing[:3] == [
            f"SKILL.md lacks validation boundary marker: {marker}"
            for marker in VALIDATION_BOUNDARY_MARKERS
        ]
    print("PASS: runtime-contract self-test")
    return 0


def main(arguments: list[str]) -> int:
    """Run the payload check or its deterministic self-test."""
    if arguments == ["--self-test"]:
        return self_test()
    if arguments:
        print("usage: check_runtime_contract.py [--self-test]", file=sys.stderr)
        return 2
    missing = missing_contracts(PAYLOAD)
    if missing:
        print("FAIL: runtime contract drift:", *[f"- {item}" for item in missing], sep="\n")
        return 1
    print("PASS: runtime shared target-first contract")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

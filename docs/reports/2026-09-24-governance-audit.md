# Governance and structure audit — zensical-skill

- **Date:** 2026-09-24 12:41 EEST
- **Scope:** full repository review per maintainer request: CI logic, governance
  coherence, tensions, stale drift, best practices, reference anchors, file
  discoverability, and gaps. Every file was read and double-checked.
- **Outcome:** the repository is unusually well-governed. Findings are mostly
  small surgical fixes, one real stale-drift item (the Zensical version pin),
  and one deliberate-but-revisit-worthy posture (zero CI).
- **State:** audit report only. Recommended fixes below were approved by the
  maintainer for implementation; results are recorded in the companion
  implementation report in this folder.

## A. CI logic — zero CI is a documented design, not an omission

- No `.github/` directory exists locally or on the remote; GitHub Actions runs
  total count is 0; branch protection on `main` is unverifiable with this
  token (HTTP 403) and vacuous because no checks are configured.
- All three governance documents independently defer automation:

  - `docs/release-checklist.md` lines 121–122: "GitHub Releases, semver tags,
    and CI automation are optional until the manual process becomes a
    demonstrated bottleneck."
  - `docs/roadmap.md` lines 342, 344 (deferred/out-of-scope list):
    "Deployment automation." and "Support and CI matrices for agents outside
    Codex, OpenCode, and Hermes."
  - `AGENTS.md`: "Add automation only after repeated, observable drift shows
    that it would remove real maintenance work" and "Do not add tests,
    scripts, or release automation until a repeated workflow makes their
    value concrete."

- Every enforcement script is real and verified working:
  - `scripts/check_commit_messages.py` — passed `HEAD` (commit 9cd3847):
    "Commit message policy passed for 1 commit(s)", exit 0. Validates subject
    ≤ 72 chars, no trailing period, non-empty `what:` and `why:` body fields.
  - `scripts/run_scenarios.sh` — 4 fixtures (tabbed, accessibility,
    code-anchor, base-path), pins `expected_version="0.0.60"`, exit 1 for
    build failure vs exit 2 for environment/network block.
  - `zensical/scripts/check_instruction_contract.py` — typed, `--self-test`,
    skip semantics when AGENTS.md/docs.yml absent.
  - `zensical/scripts/check_site_hygiene.sh` — set -euo pipefail, exit 0/1/2,
    prints paths and reason types only, never secret values.

- Recommendation framing: the evidence threshold the repo's own gate demands
  is arguably already met (25+ disciplined semantic commits with what:/why:
  bodies, a working unenforced commit-policy checker, 3-host smokes, two
  validators). CI is best presented as a gate revisit, not an unqualified
  gap. It was implemented in the follow-up per maintainer approval.

## B. Governance — strong, with one precision nit

- Reading matrix in `docs/README.md` is complete and current; AGENTS.md rules
  are followed in practice across the commit history; `release-checklist.md`
  and `docs/scenarios.md` are honest about limits; `SECURITY.md` ("two
  bounded local checks, not a full secret scan") is accurate.
- One nit: `zensical/scripts/check_instruction_contract.py` presumes a
  `.github/workflows/docs.yml` convention (11 required literals) that this
  repo itself does not exemplify. Add a one-line scope comment: it validates
  a target site's deployment contract, not this repository's own deployment.

## C. Tensions

- The only real tension is the automation gate (roadmap + AGENTS.md
  "no automation until demonstrated bottleneck" vs adding CI). Resolved by
  implementing CI within the gate's own language: the repeated workflow
  evidence exists, and the maintainer directed the change.
- `tests/scenario-env/` requires Python >= 3.13 while `zensical` on PyPI
  requires >= 3.10 — a stricter environment than the package minimum. Note
  only; not a defect.
- No README "does not handle" claim contradicts any runtime reference.

## D. Stale drift — the main finding: the Zensical version pin

- Repo pins Zensical **0.0.60**; current PyPI is **0.0.64**. The pin is
  repeated across six in-repo locations that must change together:
  1. `scripts/run_scenarios.sh` line 4 (`expected_version="0.0.60"`),
  2. `tests/scenario-env/pyproject.toml` (`zensical==0.0.60`),
  3. `tests/scenario-env/uv.lock` (resolution block),
  4. `docs/scenarios.md` line 92 + tripwire at lines 104–105 (revisit the
     fixture when the pinned version or default extension set changes),
  5. `README.md` line 194 ("lockfile-pinned Zensical 0.0.60 scenario
     environment"),
  6. `docs/research.md` — 13 mentions (historical experiment evidence that
     should stay dated, and current-state claims such as "Its pyproject.toml
     currently pins").
- Internal consistency is excellent; external drift is real (4 patch
  versions). The blog repo pins the same 0.0.60 separately (external to this
  repo; flagged, not changed here).
- Fix (implemented in follow-up): extract the pin to ONE canonical source
  (`tests/scenario-env/pyproject.toml`) that `run_scenarios.sh` derives from,
  then revalidate against 0.0.64 per the scenarios.md tripwire before bumping;
  bump only if the scenario suite passes on 0.0.64.

## E. Best practices worth keeping

- Exit-code discipline (0 pass / 1 build or policy failure / 2 environment or
  git-context failure).
- Hygiene preflight prints paths and reason types, never secret values.
- Self-test built into `check_instruction_contract.py`.
- `uv --locked` scenario environment with a committed `uv.lock`.
- Fixture minimalism: exactly 12 tracked files; on-disk `.venv` is ignored
  and untracked.
- `ZENSICAL_BIN` offline path and environment-vs-fixture failure reporting.

## F. Anchors, discoverability, and gaps

- `zensical/SKILL.md` routes all 9 references inline; none are orphaned.
- The README payload tree enumerates all 13 payload files — strong.
- Every relative link and `#anchor` in references resolves.
- Three gaps (all fixed in the follow-up):
  1. `docs/research-editorial-voice.md` was missing from the README
     "Repository map" tree, though it exists on disk and has a matrix row.
  2. `zensical/references/site-inspection.md` invoked the bundled scripts as
     bare `scripts/...` paths from an ambiguous working directory, while the
     README uses `zensical/scripts/...`. Standardize so the skill-root
     reference is unambiguous.
  3. `check_instruction_contract.py` has the docs.yml presumption above.

## Prioritized recommendations (all approved and implemented)

1. README repository map: add `research/` (now includes editorial-voice) and
   `reports/`.
2. `site-inspection.md`: make bundled-check invocations unambiguous about the
   working directory / path form.
3. Canonicalize the Zensical version pin (single source), then revalidate and
   bump to 0.0.64 only on scenario-suite evidence.
4. Add minimal CI: `.github/workflows/validate.yml` running the commit-policy
   checker and the scenario suite, SHA-pinned actions, framed as the gate
   revisit on the repo's own terms.
5. Add the one-line scope comment to `check_instruction_contract.py`.
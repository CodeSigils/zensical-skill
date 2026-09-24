# Version-drift strategy and code-quality findings (2026-09-24)

Date: 2026-09-24 13:02 EEST
Status: Recommendations for the maintainer; the drift fix itself is already
implemented and verified (see 2026-09-24-implementation.md). No approval has
been given for anything here beyond recording the strategy.

## Why this record exists

Zensical is under heavy development. Five releases shipped in two weeks:
`0.0.60` (2026-09-08), `0.0.61` (2026-09-11), `0.0.62` (2026-09-13),
`0.0.63` (2026-09-19), `0.0.64` (2026-09-22); every release keeps
`requires-python >= 3.10`. At that cadence, anything that copies the version
into more than one place goes stale in days, not months.

The governance audit found the pin duplicated across six in-repo locations
plus the live blog (all at `0.0.60` while PyPI current was `0.0.64`). That was
a textbook repeated-value drift signal. The implementation pass already
collapsed it to one canonical source and bumped to `0.0.64` with an evidence
gate. This report records the strategy that keeps the collapse permanent.

## Where the version lives now

- Canonical pin: `tests/scenario-env/pyproject.toml` (`dependencies =
  ["zensical==0.0.64"]`). One hand-edited location owns the version.
- `scripts/run_scenarios.sh` derives it (`expected_version="$(sed -n
  's/^dependencies = \["zensical==\([^"]*\)"\]$/\1/p'
  "$scenario_root/pyproject.toml")"`, line 7) with a fail-fast guard that
  exits 1 if the parse comes up empty (lines 8-11). A formatting change to
  the pin line fails loudly instead of drifting silently.
- `.github/workflows/validate.yml` calls `scripts/run_scenarios.sh` on push
  and pull request; it never carries a version literal of its own.
- `tests/scenario-env/uv.lock` is generated (`uv lock --project
  tests/scenario-env`) and pins the resolved transitive graph.
- Maintainer-facing docs reference the pin location instead of repeating the
  literal (`tests/scenario-env/pyproject.toml` in README, scenarios.md, and
  the current-state lines of the research record).
- The live blog (`/home/sand/labs/zensical-test`) still pins `0.0.60` in its
  own `pyproject.toml` and `uv.lock`; it is an external repository and is
  deliberately out of scope here.

## Recommendations

### R1 — No root VERSION file

A `VERSION` file at the repository root would re-create the drift it is meant
to fix: the six-way copy becomes a two-way copy (`VERSION` plus
`pyproject.toml`) that can disagree again. `pyproject.toml` is already the
ecosystem-standard canonical location — uv, PyPI tooling, and CI all read it.
Do not add a second owner.

### R2 — One canonical source; everything derives or points

The rule to keep, stated once: exactly one file owns the version
(`tests/scenario-env/pyproject.toml`); every other surface either derives it
(the scenario runner, the lockfile generation) or points at the owner by
path (docs prose). When a new literal version appears anywhere, ask which of
two kinds it is:

- a current-state claim, which must derive or point, or
- a dated historical record, which keeps its literal together with its date
  and context (research entries from 2026-09-09/10/13 legitimately say
  `0.0.60`; they describe what was installed then).

### R3 — Docs policy for the pin

Never write the current pin as a bare literal in maintainer-facing prose that
is expected to stay current. Write "the `zensical` pin in
`tests/scenario-env/pyproject.toml`" instead. Keep literals only inside dated
records (research entries, reports), where the date is the qualifier.
Document this classification rule beside the reading matrix so future edits
do not "fix" historical records.

### R4 — Code and CI share one variable

The scenario runner already reads the version from the canonical source, and
CI calls the runner, so there is exactly one code path and no CI copy. If
another script ever needs the version, it should parse `pyproject.toml` the
same way (or accept it as an argument), never grep a literal. Do not add a
version check to CI that duplicates the runner's.

### R5 — Dependency handling in toml and .env

- `pyproject.toml`: the only hand-edited dependency truth. Direct pins
  belong here; ranges do not, because the scenarios assert rendered output
  against a known target version.
- `uv.lock`: generated. Regenerate with `uv lock --project
  tests/scenario-env` after a pin change; never hand-edit.
- `.env`-style host configuration: must not carry version pins. Host
  configuration is per-machine runtime state, not dependency truth.
- `ZENSICAL_BIN`: an override (a path to a binary), not a version source —
  and it is still verified against `expected_version` at runtime, so a
  mismatched override fails loudly. Keep that behavior.

### R6 — Bump protocol under heavy development (the evidence gate)

Every pin bump follows the same five steps, so a bump is a decision backed by
a run rather than a version-number edit:

1. Read the changelog deltas between the pinned version and the candidate
   (`zensical.org/docs/changelog/` redirects to the GitHub releases; source
   at github.com/zensical/zensical) and identify any output-affecting change
   (for example the `0.0.63` dotfile exclusion, commit 2070bf1, or the
   `0.0.64` blog plugin, commit 5825381).
2. Bump `tests/scenario-env/pyproject.toml`.
3. Regenerate the lockfile.
4. Run `bash scripts/run_scenarios.sh` — the suite is the acceptance evidence
   for "the pinned version still renders the fixture contract".
5. Pass: keep the bump and record the evidence. Fail: revert the pin and
   record why.

The standing trigger is the Scenario E tripwire in `docs/scenarios.md`
(revisit the code-line-anchor fixture when the pinned version or the default
extension set changes). Do not bypass it on the assumption that a patch
release is output-neutral.

### R7 — Version-freshness detection stays human (for now)

The audit found the `0.0.60`→`0.0.64` gap only because a human read every
file. CI's `validate.yml` catches build breaks against the current pin on
every push, but it cannot see that the pin is behind PyPI without network
checks and a decision about what "behind" means. Adding a staleness detector
is the kind of automation the roadmap gates ("add automation only after
repeated, observable drift shows that it would remove real maintenance
work") — the incident happened once. Record this as a named deferred item:
if manual bumps become a bottleneck, the natural form is a Dependabot flow
for the uv project at `tests/scenario-env` (it would need the ecosystem
manifest registration; the repository root has no `pyproject.toml` of its
own, which is why there is no `pip`/`uv` Dependabot entry yet).

### R8 — The blog applies the same pattern

The blog pins `0.0.60` in its own `pyproject.toml` + `uv.lock`. When it is
bumped, it follows the same shape: one pin, `uv lock`, then `uv run zensical
build --clean` and a rendered review as the evidence gate — in that repo,
not here.

## Code-quality findings (py-review pass)

Reviewed surfaces: `scripts/check_commit_messages.py`,
`zensical/scripts/check_instruction_contract.py`,
`scripts/run_scenarios.sh`. No `ruff`/`mypy`/`pyright` configuration exists in
this repository (the scenario environment requires Python 3.13 but the root
has no toolchain config), so per the review router, style findings are
deferred to tooling and only correctness/clarity findings are reported.

1. `scripts/check_commit_messages.py` — LOW (clarity only). Lines 22-25
   carry a redundant condition: for `refs == ["HEAD"]` the hash is
   pre-seeded and the loop body never runs; for every other ref the condition
   is always true. It works (verified: `check_commit_messages.py HEAD` passes
   on the current HEAD), but the special-casing obscures the intent. A
   single expression — hashes derived by expanding every ref, then dedup — is
   simpler and behaves identically.
2. `zensical/scripts/check_instruction_contract.py` — no findings. Typed,
   self-tested, bounded (SKIP semantics when the target lacks the workflow or
   `## Deployment` section), clear exit behavior.
3. `scripts/run_scenarios.sh` — no findings. The sed derivation is pinned to
   the exact `dependencies = ["zensical==X"]` shape and fails loudly on any
   deviation; the inline `python3` heredoc is bounded and typed; exit-code
   discipline (0 pass / 1 build failure / 2 environment block) is intact;
   the failure log is classified before exit so an offline or network-blocked
   run is distinguished from a real fixture failure.
4. Duplication and variable use — the six-way version copy from the audit is
   collapsed; no current-state literal remains outside the canonical pin and
   the dated records. Variable names across the scripts are consistent and
   scoped. No action.

## Payload sync status

Follow-up check requested alongside this report:

- `py-review-skill` repository (`/home/sand/projects/py-review-skill`):
  clean working tree, branch `main` at `12214ee`, in sync with
  `origin/main` (0 ahead / 0 behind), remote
  `git@github.com:CodeSigils/py-review-skill.git`. Nothing to fetch.
- Installed OpenCode payload (`~/.config/opencode/skills/`): four of the six
  `py-*` skills are stale relative to the repository — `py-review`,
  `py-async-patterns`, `py-code-style`, and `py-type-safety` differ;
  `py-anti-patterns` and `py-error-handling` match. The installed
  `py-review` router still carries the pre-fix version-threshold bullets
  ("If `>=3.10`: load all relevant core skills...") and the routing row
  without the four style signals (`duplicated logic`, `regex/string
  construction`, `constants`, `domain string transformations`), i.e. the
  `a32600d` fix is not installed. Sync is: copy each `skills/*/SKILL.md` from
  the repository into `~/.config/opencode/skills/*/SKILL.md` (or re-run the
  skills CLI install), then re-load. Pending maintainer decision.
- Live blog: external, still pins `0.0.60`; flag only (R8).

## Records intentionally unchanged

Roadmap — revisited after action; phases, the deferred list, and the
capability-admission rule are unaffected by a recommendations report, so
unchanged. Vision, research records, source registry, runtime payload, and
CHANGELOG: no user-visible capability change this thread; the strategy is
recorded here, not in the runtime skill. No commit or push is authorized by
this report.
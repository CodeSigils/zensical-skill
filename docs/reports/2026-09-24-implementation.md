# Zensical-skill governance audit — implementation record

**Date:** 2026-09-24 13:05 EEST
**Scope:** [Governance audit](./2026-09-24-governance-audit.md) follow-up — all
approved recommendations implemented, gaps closed, structure re-validated.

## What was done

### 1. Research records moved under `docs/research/`

- `docs/research.md` → `docs/research/index.md` (git-tracked rename).
- `docs/research-editorial-voice.md` → `docs/research/editorial-voice.md`.
- Every reference and reading-matrix row updated repo-wide (AGENTS.md,
  docs/README.md, docs/roadmap.md, docs/scenarios.md, docs/vision.md,
  docs/release-checklist.md, zensical/references/source-registry.md,
  README.md), including moved-file internal links and the README
  "Repository map" tree, which now lists `research/` (index + editorial-voice)
  and `reports/`.
- `docs/README.md` gained a note that dated audit and implementation records in
  `reports/` are historical records, not planning inputs.

### 2. Dated audit report written

- `docs/reports/2026-09-24-governance-audit.md` records the full audit: CI
  posture (zero CI by documented design), governance strength and one nit,
  the automation-gate tension, the stale Zensical version pin, best practices
  to keep, and the anchors/discoverability gaps — with the five approved
  recommendations.

### 3. Minimal validation CI added

- `.github/workflows/validate.yml` (first CI in the repo): `commit-policy` job
  runs `scripts/check_commit_messages.py` on the pushed/PR range (fallback to
  HEAD); `scenarios` job runs `scripts/run_scenarios.sh`. SHA-pinned actions
  (`actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1` # v7.0.1,
  `astral-sh/setup-uv@c18668ad3cf93ea998bef934396af7bb5c839dc7` # v10.2.0),
  `permissions: contents: read`.
- `.github/dependabot.yml` for `github-actions` weekly updates.
- Deferral docs reconciled: `docs/release-checklist.md` handoff paragraph now
  states the minimal gate runs while GitHub Releases/semver stay optional;
  `docs/roadmap.md` Deferred section records the single host-agnostic gate
  without per-host CI or deployment automation.

### 4. Version pin canonicalized and Zensical bumped 0.0.60 → 0.0.64

- `scripts/run_scenarios.sh` no longer hardcodes the version; it derives
  `expected_version` from the single canonical source
  `tests/scenario-env/pyproject.toml` (with a fail-fast guard).
- `tests/scenario-env/pyproject.toml` → `zensical==0.0.64`; `uv.lock`
  regenerated (11 packages, 474 ms; zensical v0.0.60 → v0.0.64).
- **Evidence gate passed:** `bash scripts/run_scenarios.sh` built all four
  fixtures on 0.0.64 (tabs, iframe-title findings, code-line-anchor repair,
  base-path links, sitemap + robots assertions) → `PASS`. Deltas 0.0.60→0.0.64
  verified safe for the fixture set: markdown-extension defaults and
  `line_spans="__span"` byte-identical, tabs/admonitions/sitemap unchanged,
  no `zensical.toml` key removals, `build --clean` unchanged. The only
  output-affecting changes (0.0.63 dotfile exclusion
  [2070bf1](https://github.com/zensical/zensical/commit/2070bf1cbe4ca6eff4078113f6d3665dcb43f77c);
  0.0.64 `rebase_urls` no-op for plain pages; blog plugin
  [5825381](https://github.com/zensical/zensical/commit/5825381d75cf22256f7b87096a865d91c27e7756))
  do not touch our fixture inputs.
- Current-state version mentions updated: README "lockfile-pinned Zensical
  `0.0.64` scenario environment (pin in `tests/scenario-env/pyproject.toml`)",
  docs/scenarios.md Scenario E ("pinned Markdown-extension defaults" →
  canonical pin), docs/research/index.md Current evidence limits (`0.0.64`,
  pin location). Dated historical experiment records keep 0.0.60 with their
  original context — they describe what was installed then.
- Out of scope: the external blog repo `/home/sand/labs/zensical-test` still
  pins 0.0.60 in its own `pyproject.toml`/`uv.lock`; C-note in the audit. Not
  changed here.

### 5. Skill structure fixed to the industry standard

- `zensical/SKILL.md` frontmatter: `compatibility` moved from `metadata.compatibility`
  to the **top-level** field, per the Agent Skills specification
  (https://agentskills.io/specification; `skills-ref` validator at pinned
  commit `69ef37e9424c0a7ea9dd2293b559e43ec8176379` allows exactly
  `name, description, license, allowed-tools, metadata, compatibility`).
- `metadata` keeps house-convention keys (short-description, keywords,
  repository, maintainers) — spec-tolerated, not validator-enforced.
- Verified against skills.sh CLI conventions (vercel-labs/skills @
  `7407f3893ad4dceab546ac002c3ef806e4000c73`): `skills validate` does not
  exist; validation is the agentskills `skills-ref validate`, which passes:
  `Valid skill: zensical`. `agents/openai.yaml` follows the OpenClaw/ClawHub
  convention and stays.
- **Re-validation passed:** pinned `skills-ref validate zensical` →
  `Valid skill: zensical` (2026-09-24).

### 6. Discoverability gaps closed

- `zensical/references/site-inspection.md` bundled-script commands now state
  the working directory explicitly ("Run it from the skill root — the
  directory containing `SKILL.md`"), keeping the spec-recommended
  skill-root-relative `scripts/…` paths unambiguous.
- `zensical/scripts/check_instruction_contract.py` docstring now scopes the
  check to *target-site* deployment contracts (the conventional `docs.yml`
  lockfile-backed contract), explicitly not this repo's own deployment.
- README "Repository map" tree now includes `research/`, `reports/`, and the
  re-aligned `docs/` entries.

## Verification

- `python3 scripts/check_commit_messages.py HEAD` — passed (1 commit).
- `bash scripts/run_scenarios.sh` — PASS on zensical 0.0.64.
- `bash zensical/scripts/check_site_hygiene.sh .` — PASS.
- `git diff --check` — clean.
- `skills-ref validate zensical` at pinned agentskills commit — `Valid skill:
  zensical`.
- Repo-wide grep — no stale `research.md` / `research-editorial-voice`
  references outside dated records.

## Records intentionally unchanged

- `docs/vision.md` — scope/quality boundary unchanged (portable-suggestion
  framing preserved); only its research link path updated.
- `docs/roadmap.md` — phases and deferred list intact; Deferred section gained
  the CI-gate note and the after-action gate is satisfied for this work.
- Digital Basement umbrella (`/home/sand/projects/digital-basement/`) — this
  change alters the skill's automation posture and doc layout but not its
  maturity, scope, or editorial relationship; no cross-project update made.
- Live blog `/home/sand/labs/zensical-test` — untouched (external repo).

## Remaining items

- Commit + push this batch on explicit authorization (imperative subject with
  `what:`/`why:` body; `python3 scripts/check_commit_messages.py HEAD`).
- The external blog repo pin (0.0.60) may later be revalidated against 0.0.64
  via the same scenario gate when the blog is next touched.
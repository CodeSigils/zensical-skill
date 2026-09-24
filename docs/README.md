# Planning documentation index

This directory is maintainer context, not runtime skill context. Read only the
documents relevant to the proposed change.

| Change | Read first |
| --- | --- |
| Skill scope or trigger | `vision.md`, `roadmap.md` |
| Workflow or validation change | `vision.md`, `roadmap.md`, `research/index.md` |
| Media or asset workflow | `vision.md`, `roadmap.md`, `research/index.md` |
| CSS, theme, or landing-page workflow | `vision.md`, `roadmap.md`, `research/index.md` |
| Accessibility workflow | `vision.md`, `roadmap.md`, `research/index.md` |
| Documentation freshness contract | `AGENTS.md`, the canonical owner for each affected claim, and the relevant planning document |
| Runtime distribution contract | `AGENTS.md`, `release-checklist.md`, and the relevant host-install evidence |
| Commit or changelog policy | `AGENTS.md`, `README.md`, `release-checklist.md`, `CHANGELOG.md` |
| Repeated values or centralization | `AGENTS.md`, `vision.md`, `roadmap.md`, `release-checklist.md` |
| External source or comparable-skill pattern | `research/index.md`, `vision.md` |
| Editorial voice or prose-tell guidance | `research/editorial-voice.md`, `research/index.md`, `vision.md` |
| Sequencing or release gate | `roadmap.md`, `vision.md` |
| Acceptance scenario or fixture | `scenarios.md`, `roadmap.md`, `research/index.md` |
| Distribution or compatibility | `vision.md`, `roadmap.md`, `research/index.md`, `release-checklist.md` |
| Release or market discoverability | `roadmap.md`, `research/index.md`, `release-checklist.md` |
| Digital Basement umbrella alignment | `AGENTS.md`, `roadmap.md`, `research/index.md`; then the corresponding Digital Basement architecture, roadmap, editorial core, and session note when available |

When a change affects scope, sequencing, evidence, or release expectations,
update the corresponding planning document before completing the work. Recheck
volatile sources before a release or after a Zensical upgrade.

`release-checklist.md` records commands and evidence that are only meaningful
for a public or package-discovery release. Do not copy its installation
commands into the runtime skill until they have been verified for the target
host and current provider contract.

Dated governance audits and implementation records live in `reports/`; they are
historical records, not planning inputs.

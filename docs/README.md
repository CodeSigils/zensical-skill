# Planning documentation index

This directory is maintainer context, not runtime skill context. Read only the
documents relevant to the proposed change.

| Change | Read first |
| --- | --- |
| Skill scope or trigger | `vision.md`, `roadmap.md` |
| Workflow or validation change | `vision.md`, `roadmap.md`, `research/current-state.md` |
| Media or asset workflow | `vision.md`, `roadmap.md`, `research/index.md` |
| CSS, theme, or landing-page workflow | `vision.md`, `roadmap.md`, `research/index.md` |
| Accessibility workflow | `vision.md`, `roadmap.md`, `research/index.md` |
| Documentation freshness contract | `AGENTS.md`, the canonical owner for each affected claim, and the relevant planning document |
| Runtime distribution contract | `AGENTS.md`, `release-checklist.md`, and the relevant host-install evidence |
| Commit or release-history policy | `AGENTS.md`, `README.md`, `release-checklist.md` |
| Repeated values or centralization | `AGENTS.md`, `vision.md`, `roadmap.md`, `release-checklist.md` |
| External source or comparable-skill pattern | `research/current-state.md`, then `research/index.md` for dated observations, `vision.md` |
| Editorial voice or prose-tell guidance | `research/editorial-voice.md`, `research/current-state.md`, `vision.md` |
| Skill packaging, frontmatter, or payload contract | `research/skill-structure-conventions.md`, `research/skill-sync-and-cross-agent-distribution.md`, `research/index.md`, `release-checklist.md` |
| Sequencing or release gate | `roadmap.md`, `vision.md` |
| Acceptance scenario or fixture | `scenarios.md`, `roadmap.md`, `research/current-state.md` |
| Distribution or compatibility | `vision.md`, `roadmap.md`, `research/skill-sync-and-cross-agent-distribution.md`, `research/index.md`, `release-checklist.md` |
| Release or market discoverability | `roadmap.md`, `research/index.md`, `release-checklist.md` |
| Digital Basement umbrella alignment | `AGENTS.md`, `roadmap.md`, `research/index.md`; then the corresponding Digital Basement architecture, roadmap, editorial core, and session note when available |

When a change affects scope, sequencing, evidence, or release expectations,
update the corresponding planning document before completing the work. Recheck
volatile sources before a release or after a Zensical upgrade.

`release-checklist.md` records commands and evidence that are only meaningful
for a public or package-discovery release. Do not copy its installation
commands into the runtime skill until they have been verified for the target
host and current provider contract.

Dated governance audits and implementation records live in `reports/`, and
dated field observations live in `research/index.md`; both are historical
records, not planning inputs. For what is currently true, read
`research/current-state.md`, which owns current facts and carries a
`Reviewed <date>` marker.

Reports are never retro-edited, so read the one matching your question rather
than the newest:

| Report | Read it for |
| ------ | ----------- |
| [2026-09-24-governance-audit.md](reports/2026-09-24-governance-audit.md) | The audit that found the scenario pin behind the current release. |
| [2026-09-24-implementation.md](reports/2026-09-24-implementation.md) | What that audit changed, and what it deliberately left alone. |
| [2026-09-24-version-drift-strategy.md](reports/2026-09-24-version-drift-strategy.md) | Why repeated version literals were collapsed to one canonical source. |
| [2026-09-24-oh-my-openagent-editorial-review.md](reports/2026-09-24-oh-my-openagent-editorial-review.md) | An external editorial review of a sibling guide, and what was declined. |
| [2026-09-26-payload-review-and-remediation.md](reports/2026-09-26-payload-review-and-remediation.md) | The payload review that admitted feeds and corrected stale claims. |
| [2026-09-26-governance-mechanism.md](reports/2026-09-26-governance-mechanism.md) | Why documentation is governed by a duplication rule rather than a size limit. |
| [2026-09-26-governance-recommendations-applied.md](reports/2026-09-26-governance-recommendations-applied.md) | The four documentation recommendations that followed, and the counts that verify them. |

Every behavioral rule has exactly one owning file, per the canonical-owner rule
in `AGENTS.md`. This table routes to owners; it does not restate them. If a row
below sends you to two files that both state the same rule, one is a stale
pointer: fix the duplicate rather than reconciling them at read time.

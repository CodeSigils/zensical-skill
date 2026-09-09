# Planning documentation index

This directory is maintainer context, not runtime skill context. Read only the
documents relevant to the proposed change.

| Change | Read first |
| --- | --- |
| Skill scope or trigger | `vision.md`, `roadmap.md` |
| Workflow or validation change | `vision.md`, `roadmap.md`, `research.md` |
| Media or asset workflow | `vision.md`, `roadmap.md`, `research.md` |
| CSS, theme, or landing-page workflow | `vision.md`, `roadmap.md`, `research.md` |
| Accessibility workflow | `vision.md`, `roadmap.md`, `research.md` |
| Commit or changelog policy | `AGENTS.md`, `README.md`, `release-checklist.md`, `CHANGELOG.md` |
| Repeated values or centralization | `AGENTS.md`, `vision.md`, `roadmap.md`, `release-checklist.md` |
| External source or comparable-skill pattern | `research.md`, `vision.md` |
| Sequencing or release gate | `roadmap.md`, `vision.md` |
| Acceptance scenario or fixture | `scenarios.md`, `roadmap.md`, `research.md` |
| Distribution or compatibility | `vision.md`, `roadmap.md`, `research.md`, `release-checklist.md` |
| Release or market discoverability | `roadmap.md`, `research.md`, `release-checklist.md` |

When a change affects scope, sequencing, evidence, or release expectations,
update the corresponding planning document before completing the work. Recheck
volatile sources before a release or after a Zensical upgrade.

`release-checklist.md` records commands and evidence that are only meaningful
for a public or package-discovery release. Do not copy its installation
commands into the runtime skill until they have been verified for the target
host and current provider contract.

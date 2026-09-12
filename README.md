# zensical-skill

[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-2563eb.svg)](https://agentskills.io/specification)
[![skills.sh](https://skills.sh/b/codesigils/zensical-skill)](https://skills.sh/codesigils/zensical-skill)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

`zensical-skill` is a focused Agent Skill for inspecting, lightly editing,
reviewing, and validating existing [Zensical](https://zensical.org/) sites.
It helps an agent preserve a repository's conventions while working with
Zensical Markdown components, navigation, media assets, and presentation
customization.

This is a usable, actively developed skill for its documented, evidence-backed
maintenance scope—not a complete Zensical automation suite. The current payload
is intentionally narrow and is being developed from real maintenance work on
the Code Sigils blog; rely on its recorded checks, not implied coverage beyond
them.

It can evolve into a broader methodology or automation capability, but only
when real use demonstrates value and current official Zensical documentation,
the target's installed version, validation cost, and ongoing maintenance support
the addition.

When a user explores an addition, the skill should turn that documentation
check into a short, relevant set of Zensical options with fit, trade-offs, and
validation needs—not a generic feature catalog or an unapproved change.

## Quick start

Copy the complete `zensical/` directory; its references are part of the
runtime payload. The following project-scoped paths have file-availability
smoke evidence, but they do not imply long-running host reload behavior.

| Host     | Project-scoped location                     | Setup                                                                                                                                     |
| -------- | ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Codex    | `.agents/skills/zensical/`                  | `mkdir -p .agents/skills && cp -R zensical .agents/skills/`                                                                               |
| OpenCode | `.opencode/skills/zensical/`                | `mkdir -p .opencode/skills && cp -R zensical .opencode/skills/`                                                                           |
| Hermes   | configured `skills.external_dirs` directory | Add the repository's `zensical/` directory to `external_dirs`; do not copy it into a live global skill directory unless that is intended. |

Skills CLI `1.5.25` installed this direct-source command successfully from
commit `d7ef1e0` in a disposable Codex project on 2026-09-10. Skills.sh
indexing was also confirmed that day; review the payload before using it. The
documented baseline is `npx skills add <skill-name>`; the flags below are
recorded installation evidence, not a claim about every current CLI option.

```bash
npx skills add CodeSigils/zensical-skill \
  --skill zensical --agent codex --copy --yes
```

For live development, agents that support external skill directories can point
directly at the repository's `zensical/` directory. The security policy and
release checklist are maintainer records, not guarantees that every target site
is safe.

## Current scope

The skill currently routes these tasks:

- inspect an existing Zensical repository and identify its conventions;
- make an explicitly authorized light Markdown edit;
- review content, navigation, links, front matter, admonitions, tabs, and
  images or embeds, including proportionate HTML-media semantics and new-tab
  link policy;
- review responsive CSS, theme overrides, and landing-page conventions;
- review accessibility concerns across content, media, components, and themes;
- use a browser for a representative rendered-page check when it is available
  and the requested presentation scope warrants it;
- run a bounded tracked-file hygiene preflight before authorized commits,
  publishing, or deployment;
- validate a build and, where feasible, affected rendered output; and
- report deployment boundaries and configuration/documentation drift.

## How to use it

Load `zensical` for a concrete task in an existing Zensical repository. The
runtime router selects focused references progressively.

| Request                                          | Routed workflow                              |
| ------------------------------------------------ | -------------------------------------------- |
| “Orient me in this Zensical site”                | Site inspection                              |
| “Make this small Markdown, tab, or link edit”    | Authorized light edit and content components |
| “Review this article, navigation, or embed”      | Editorial, media, and component review       |
| “Check accessibility or responsive presentation” | Accessibility and customization review       |
| “Build and validate this change”                 | Build and rendered-output validation         |
| “Why did this Zensical build fail?”              | Narrow failure diagnosis                     |

## What it does not handle

The skill does not own prose craft, blog voice, SEO, generic frontend work,
full theme authoring, autonomous publishing or deployment, comprehensive WCAG
certification, or every Zensical feature. Those remain separate editorial,
presentation, or release capabilities.

## Repository map

```text
zensical/
├── SKILL.md                 # portable runtime payload
├── agents/openai.yaml       # Codex metadata
├── scripts/                 # bounded runtime checks
└── references/              # loaded only when a workflow needs detail
docs/
├── vision.md                # purpose, boundaries, and quality criteria
├── roadmap.md               # evidence-gated implementation plan
├── research.md              # verified sources and comparable patterns
├── scenarios.md             # bounded real-site acceptance procedures
└── README.md                # maintainer reading matrix
tests/fixtures/              # site-only deterministic scenario inputs
tests/scenario-env/          # locked Zensical test environment
scripts/run_scenarios.sh     # isolated fixture runner
AGENTS.md                   # maintainer change contract
CHANGELOG.md                # project-level history
LICENSE                     # MIT license
SECURITY.md                 # reporting and payload boundaries
```

The runtime payload is under `zensical/`. The `docs/` directory is maintainer
context and is not loaded as part of the skill.

## Skill Payload — What Ships to the User

Only the `zensical/` directory is the portable Agent Skill payload. It contains
the router, on-demand references, client metadata, and the bounded tracked-file
hygiene check.

```text
zensical/
├── SKILL.md                         # scope, routing, and safety boundaries
├── agents/openai.yaml               # optional Codex display metadata
├── references/
│   ├── accessibility.md             # semantic and rendered a11y checks
│   ├── content-components.md        # admonitions, tabs, links, navigation
│   ├── customization.md             # CSS, themes, templates, landing pages
│   ├── editorial-review.md          # bounded article-quality review
│   ├── light-edit.md                # authorized minimal Markdown edits
│   ├── media.md                     # media, embeds, assets, base paths
│   ├── site-inspection.md           # repository orientation and preflight
│   ├── source-registry.md           # version-sensitive primary sources
│   └── validation.md                # build and rendered-output checks
└── scripts/
    ├── check_instruction_contract.py # deployment-instruction drift check
    └── check_site_hygiene.sh         # no-secret-output tracked-file preflight
```

What users receive:

- agentskills.io `name` and `description` frontmatter for `zensical`;
- repository-agnostic Zensical maintenance and review instructions;
- references loaded progressively for the requested workflow; and
- a bounded, read-only-by-default hygiene preflight for authorized publication
  work.

What does not ship in the payload:

- Code Sigils or Digital Basement editorial conventions;
- blog-specific content types, tone, or terminology;
- test fixtures, the locked scenario environment, or generated site output;
- maintainer planning, research, release, and session documentation; or
- host-specific copies and project configuration.

Copy the complete `zensical/` directory to preserve reference discovery.
Everything outside it is repository-only development or acceptance evidence.

## Current state

| Surface            | Status                      | Evidence boundary                                                                        |
| ------------------ | --------------------------- | ---------------------------------------------------------------------------------------- |
| Codex              | Project-scoped smoke passed | `SKILL.md` and required references resolve under `.agents/skills/zensical/`              |
| OpenCode           | Project-scoped smoke passed | `SKILL.md` and required references resolve under `.opencode/skills/zensical/`            |
| Hermes             | Project-scoped smoke passed | Payload and required references resolve through the documented external-directory layout |
| Skills CLI install | Passed at `d7ef1e0`         | Version 1.5.25 copied all 13 payload files into disposable `.agents/skills/zensical/` |
| Skills.sh search   | Indexed on 2026-09-10        | Public API searches returned `codesigils/zensical-skill/zensical`                        |
| Public release     | Not claimed                 | Marketplace indexing is not a release, support, or compatibility guarantee               |

- The payload passes the local Agent Skill structural validator and the pinned
  official `skills-ref` validator at agentskills commit
  `69ef37e9424c0a7ea9dd2293b559e43ec8176379`.
- The repository is licensed under MIT and has a security reporting policy.
- The initial workflows are acceptance-tested against the Code Sigils Zensical
  blog; its editorial conventions are not part of the portable payload.
- The initial fixtures run through a lockfile-pinned Zensical `0.0.60`
  scenario environment.
- The scenario suite covers tab rendering, reproducible accessibility findings,
  and non-root deployment links; it is not a complete site or WCAG conformance
  suite.
- The runner distinguishes dependency/network blocks from fixture failures and
  accepts an installed matching binary through `ZENSICAL_BIN`.
- The runtime payload includes a no-secret-output hygiene preflight for common
  tracked credential and private-key indicators; it is not a full secret scan.
- Direct Skills CLI installation, project-scoped host-loader smoke checks for
  Codex, OpenCode, and Hermes, and Skills.sh search indexing have been
  verified; public release remains unclaimed.

These are development facts, not guarantees about every Zensical repository.
Version-sensitive behavior must be checked against the current documentation
and the target site's configuration.

## Security model

The skill works only in the repository and scope the user authorizes. Its
tracked-file hygiene preflight reports candidate paths and finding types, never
secret values; it is not a full secret scan. Builds, documentation lookups, and
external-link checks can require network access. Commits, publishing,
deployment, credential rotation, and history rewriting require separate,
explicit authorization. See [SECURITY.md](SECURITY.md) for disclosure and
payload boundaries.

## Development workflow

1. Read [`AGENTS.md`](AGENTS.md) and the relevant documents in
   [`docs/README.md`](docs/README.md).
2. Make a narrow change to the runtime payload or its supporting evidence.
3. Run the Agent Skills validator and inspect the diff for duplicated or
   drifting guidance.
4. Record changed sources, uncertainty, and the validation performed.

Do not install, execute, publish, or deploy third-party material as part of
discovery or review without explicit authorization.

## Validate

Run the focused checks from the repository root:

```bash
uvx --from git+https://github.com/agentskills/agentskills.git@69ef37e9424c0a7ea9dd2293b559e43ec8176379#subdirectory=skills-ref skills-ref validate zensical
bash scripts/run_scenarios.sh
bash zensical/scripts/check_site_hygiene.sh .
python3 zensical/scripts/check_instruction_contract.py /path/to/site
git diff --check
```

The validator checks payload structure, the scenario runner checks the pinned
Zensical fixtures, and the hygiene preflight checks tracked files for common
sensitive-material candidates. The instruction-contract check compares a
conventional documented deployment section with its workflow. None proves
deployment success, player behavior, remote-link availability, or full
accessibility conformance.

## Primary references

- [Zensical documentation](https://zensical.org/docs/)
- [Admonitions](https://zensical.org/docs/authoring/admonitions/)
- [Content tabs](https://zensical.org/docs/authoring/content-tabs/)
- [Agent Skills specification](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx)
- [Zola skill architectural reference](https://github.com/CodeSigils/zola-skill)

The source registry in
[`zensical/references/source-registry.md`](zensical/references/source-registry.md)
records what each source supports and when it was checked.

Repeated semantic values are review signals for possible duplication or drift,
not automatic extraction targets. Centralize a value only when its copies
should change together and the trade-off improves clarity.

Commit policy is checked with `python3 scripts/check_commit_messages.py`; each
commit must explain `what:` and `why:` in its body. The changelog is curated and
does not duplicate the full commit history.

Public distribution and market discoverability are not claimed yet. The
verification steps are documented in
[`docs/release-checklist.md`](docs/release-checklist.md).

## Roadmap

See [`docs/roadmap.md`](docs/roadmap.md). The existing-site review and light-
edit workflow is substantially proven against the Code Sigils blog, with a
small repeatable scenario suite for the observed failures. The completed
three-task field run did not justify another helper or fixture. The next
milestone requires either a repeated, testable maintenance gap or an explicit
reviewed release candidate; new scripts, fixtures, integrations, and CI should
earn their place through observed need.

## Status and feedback

This repository is maintained as a small, evidence-driven experiment. Please
report unclear routing, stale source assumptions, or a workflow that changes
the requested scope. A useful issue includes the target repository shape, the
authorized operation, the observed output, and the source/version involved.

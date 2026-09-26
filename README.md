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
maintenance scope—not a complete Zensical automation suite.

It can evolve into a broader methodology or automation capability only under the
[capability-admission rule](docs/roadmap.md#capability-admission-rule).

When a user explores an addition, the skill should turn that documentation
check into a short, relevant set of Zensical options with fit, trade-offs, and
validation needs—not a generic feature catalog or an unapproved change.

## Quick start

Copy the complete [`zensical/`](zensical/) directory; its references are part
of the runtime payload. The following project-scoped paths have
[file-availability smoke evidence](docs/research/current-state.md), but they
do not imply long-running host reload behavior.

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

### Refreshing an installed copy

The agent specification has no version field and no update channel, so nothing
can compare an installed copy against the source on its own. Refresh explicitly:

```bash
npx skills update zensical     # or: npx skills upgrade zensical
```

Skills CLI `1.5.25` was recorded as the install baseline on 2026-09-10; the
refresh behaviour described here was inspected on 2026-09-26 through
`npx skills@latest --help`. `update` (alias `upgrade`) is the only refresh
command. There is no read-only staleness check, because `check` and `update`
dispatch to the same code path rather than only reporting a difference, and
there is no `--dry-run`. It compares a content hash of the installed files, not
a version number, so a payload edit is picked up even though no version
changed.

Two caveats are worth knowing before relying on it. An open upstream issue
reports that `update` re-installs skills originally added with `--copy` as
symlinks, so a copied install can turn into a linked one; re-copy manually if
that matters. And a skill installed by copying files has no recorded source, so
the CLI cannot update it at all — re-run the `cp -R` command from the table
above.

Maintainers refresh every installed copy after changing the payload, and say
which files changed. That is a maintainer obligation rather than a user step,
because a host loads its installed copy and never reads the repository.

## Current scope

The skill currently routes these tasks:

- inspect an existing Zensical repository and identify its conventions;
- make an explicitly authorized light Markdown edit or place a new article in
  the best-fitting existing category;
- review publication-facing structure: navigation, links, front matter,
  headings, admonitions, tabs, and images or embeds, including proportionate
  HTML-media semantics, performance, and new-tab link policy;
- provide an optional, target-guidance-first content review when explicitly
  requested, without imposing a house style or article formula;
- review responsive CSS, theme overrides, and landing-page conventions;
- review accessibility concerns across content, media, components, and themes;
- use a browser for a representative rendered-page check when it is available
  and the requested presentation scope warrants it;
- run a bounded tracked-file hygiene preflight before authorized commits,
  publishing, or deployment;
- review generated sitemaps and canonical URLs during an explicit release-output
  review, without claiming indexing or deployment success;
- enable and verify RSS and JSON feeds on a target running a Zensical version
  that provides them natively, including the discovery link a feed needs to be
  findable and the Git history its item dates come from;
- validate a build and, where feasible, affected rendered output; and
- identify a focused, validated pending diff as ready to commit and offer that
  next step, without treating review or validation as Git authorization; and
- report deployment boundaries and configuration/documentation drift.

## How to use it

Load `zensical` for a concrete task in an existing Zensical repository. The
runtime router selects focused references progressively.

| Request                                          | Routed workflow                              |
| ------------------------------------------------ | -------------------------------------------- |
| “Orient me in this Zensical site”                | Site inspection                              |
| “Make this small Markdown, tab, or link edit”    | Authorized light edit and content components |
| “Check article structure, navigation, or embed” | Media and component review                    |
| “Review this article draft”                      | Optional target-guidance-first content review |
| “Check accessibility or responsive presentation” | Accessibility and customization review       |
| “Add an RSS or JSON feed to my site”              | Feed setup and discovery-link check          |
| “Build and validate this change”                 | Build and rendered-output validation         |
| “Why did this Zensical build fail?”              | Narrow failure diagnosis                     |

## What it does not handle

The skill can offer optional, target-guidance-first article suggestions, but it
does not define a house voice, mandatory article formula, SEO strategy, or full
theme-authoring workflow. It also does not autonomously publish or deploy,
claim comprehensive WCAG certification, or cover every Zensical feature. Those
remain target-specific editorial, presentation, or release capabilities.

## Skill Payload — What Ships to the User

Only the [`zensical/`](zensical/) directory is the portable Agent Skill
payload. It contains the router, on-demand references, client metadata, and
two bounded checks: a tracked-file hygiene preflight and a conventional
deployment-instruction contract check.

```text
zensical/
├── SKILL.md                         # scope, routing, and safety boundaries
├── agents/openai.yaml               # optional Codex display metadata
├── references/
│   ├── accessibility.md             # semantic and rendered a11y checks
│   ├── article-review.md             # optional portable content review
│   ├── content-components.md        # admonitions, tabs, links, navigation
│   ├── customization.md             # CSS, themes, templates, landing pages
│   ├── light-edit.md                # authorized minimal Markdown edits
│   ├── media.md                     # media, embeds, assets, base paths
│   ├── rss.md                       # native RSS and JSON feeds
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

## Repository map

```text
zensical/
├── SKILL.md                 # portable runtime payload
├── agents/openai.yaml       # Codex metadata
├── scripts/                 # bounded runtime checks
└── references/              # loaded only when a workflow needs detail
docs/
├── vision.md                        # purpose, boundaries, and quality criteria
├── roadmap.md                       # evidence-gated implementation plan
├── research/
│   ├── current-state.md             # what the project currently knows, with check dates
│   ├── index.md                     # append-only dated field record
│   ├── editorial-voice.md           # human editorial voice and AI-tell research
│   ├── skill-structure-conventions.md # agentskills/skills.sh packaging contract
│   └── skill-sync-and-cross-agent-distribution.md # install, refresh, and versioning research
├── scenarios.md                     # bounded real-site acceptance procedures
├── release-checklist.md             # release gate and recorded evidence
├── reports/                         # dated governance audits and implementation records
└── README.md                        # maintainer reading matrix
tests/fixtures/                      # site-only deterministic scenario inputs
tests/scenario-env/                  # locked Zensical test environment
scripts/
├── check_commit_messages.py         # commit subject and what:/why: policy
├── check_readme_inventory.py        # README file trees against the repository
└── run_scenarios.sh                 # isolated fixture runner
AGENTS.md                            # maintainer change contract
ruff.toml                            # narrow lint scope for the local checks
LICENSE                              # MIT license
SECURITY.md                          # reporting and payload boundaries
```

The runtime payload is under `zensical/`. The `docs/` directory is maintainer
context and is not loaded as part of the skill.

## Current state

The [dated current-state record](docs/research/current-state.md) is the
authoritative evidence ledger for these status claims.

| Surface            | Status                      | Evidence boundary                                                                        |
| ------------------ | --------------------------- | ---------------------------------------------------------------------------------------- |
| Codex              | Project-scoped smoke passed | `SKILL.md` and required references resolve under `.agents/skills/zensical/`              |
| OpenCode           | Project-scoped smoke passed | `SKILL.md` and required references resolve under `.opencode/skills/zensical/`            |
| Hermes             | Project-scoped smoke passed | Payload and required references resolve through the documented external-directory layout |
| Skills CLI install | Passed at `d7ef1e0`         | Version 1.5.25 copied all 13 payload files into disposable `.agents/skills/zensical/` at the time; the payload has since grown to 14 files |
| Skills.sh search   | Indexed on 2026-09-10        | Public API searches returned `codesigils/zensical-skill/zensical`                        |
| Public release     | Not claimed                 | Marketplace indexing is not a release, support, or compatibility guarantee               |

- The payload passes the local Agent Skill structural validator and the pinned
  official `skills-ref` validator at agentskills commit
  `69ef37e9424c0a7ea9dd2293b559e43ec8176379`.
- The repository is licensed under MIT and has a security reporting policy.
- The initial workflows are acceptance-tested against the Code Sigils Zensical
  blog; its editorial conventions are not part of the portable payload.
- The initial fixtures run through a lockfile-pinned Zensical `0.0.65`
  scenario environment (pin in
  [`tests/scenario-env/pyproject.toml`](tests/scenario-env/pyproject.toml)).
- The scenario suite covers tab rendering, reproducible accessibility findings,
  code-line-anchor repair, non-root deployment links, and sitemap/canonical
  assertions; it is not a complete site or WCAG conformance suite.
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

Three CI jobs run on every push and pull request against `main`
([`.github/workflows/validate.yml`](.github/workflows/validate.yml)): the
[commit-policy check](scripts/check_commit_messages.py), the
[scenario suite](scripts/run_scenarios.sh), and a third job running five local
checks ([`check_instruction_contract.py --self-test`](zensical/scripts/check_instruction_contract.py),
[`check_site_hygiene.sh`](zensical/scripts/check_site_hygiene.sh),
[`check_readme_inventory.py --self-test`](scripts/check_readme_inventory.py),
[`check_readme_inventory.py`](scripts/check_readme_inventory.py), which fails
when the README's file trees stop matching the repository, and
[`uvx ruff@0.15.16 check .`](.github/workflows/validate.yml) against the
narrow rule set in [`ruff.toml`](ruff.toml); that workflow is the authoritative command
definition). [Dependabot](.github/dependabot.yml) watches the pinned workflow
actions. The gate runs checks, not a deployment.

## Primary references

- [Zensical documentation](https://zensical.org/docs/)
- [Admonitions](https://zensical.org/docs/authoring/admonitions/)
- [Content tabs](https://zensical.org/docs/authoring/content-tabs/)
- [Agent Skills specification](https://agentskills.io/specification)
- [Zola skill architectural reference](https://github.com/CodeSigils/zola-skill)

The source registry in
[`zensical/references/source-registry.md`](zensical/references/source-registry.md)
records what each source supports and when it was checked.

Repeated semantic values are review signals for possible duplication or drift,
not automatic extraction targets. Centralize a value only when its copies
should change together and the trade-off improves clarity.

Commit policy is checked with
[`python3 scripts/check_commit_messages.py`](scripts/check_commit_messages.py);
each commit must explain `what:` and `why:` in its body. Release-facing history
lives in those commit bodies; there is no changelog file, because a running
list duplicated the commit log, drifted from it, and never changed a decision.

Public release, support, and compatibility guarantees are not claimed yet.
Skills.sh indexing is discoverability evidence, not a release. The verification
steps are documented in
[`docs/release-checklist.md`](docs/release-checklist.md).

## Generic-site expansion

Code Sigils is the current product-facing acceptance environment, not a
template that other sites must follow. The next expansion is to prove the
existing-site workflow on two or three materially different Zensical
repositories. Candidate slices are generic content-model/authoring work,
bounded MiniJinja theme overrides, explicit release review, and a
multi-deployment language-selector workflow. Each must satisfy the
capability-admission rule before it becomes part of the portable payload.

Do not promise Zola-equivalent multilingual content routing: Zensical currently
supports one canonical language per generated project and can link
alternate-language deployments. Feeds are an admitted bounded capability,
because Zensical has provided them natively since 0.0.65; check the target's
version before writing feed configuration. Generated sitemap behavior can be
reviewed when `site_url` is configured; it is an admitted bounded
release-output review, not deployment proof. See the roadmap and source
registry for the capability boundaries.

## Roadmap

See [`docs/roadmap.md`](docs/roadmap.md). The existing-site review, light-
edit, and native-feed workflows are substantially proven against the Code Sigils
blog, with a small repeatable scenario suite for the observed failures. The completed
three-task field run did not justify another helper or fixture. The next
milestone requires either a repeated, testable maintenance gap or an explicit
reviewed release candidate; new scripts, fixtures, integrations, and CI should
earn their place through observed need.

## Status and feedback

This repository is maintained as a small, evidence-driven experiment. Please
report unclear routing, stale source assumptions, or a workflow that changes
the requested scope. A useful issue includes the target repository shape, the
authorized operation, the observed output, and the source/version involved.

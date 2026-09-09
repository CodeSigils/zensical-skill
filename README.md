# zensical-skill

[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-2563eb.svg)](https://agentskills.io/specification)
[![skills.sh](https://skills.sh/b/codesigils/zensical-skill)](https://skills.sh/codesigils/zensical-skill)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

`zensical-skill` is a focused Agent Skill for inspecting, lightly editing,
reviewing, and validating existing [Zensical](https://zensical.org/) sites.
It helps an agent preserve a repository's conventions while working with
Zensical Markdown components, navigation, media assets, and presentation
customization.

This is an early, reviewable project—not a complete Zensical automation suite.
The current payload is intentionally narrow and is being developed from real
maintenance work on the Code Sigils blog.

## Install with Skills CLI

```bash
npx skills add CodeSigils/zensical-skill \
  --skill zensical --agent codex --copy --yes
```

For a live project-scoped checkout, point an agent that supports external skill
directories at the repository's `zensical/` directory instead. Review the
payload and its references before installing; the repository's security policy
and release checklist are maintainer records, not a guarantee that every
target site is safe.

## Current scope

The skill currently routes these tasks:

- inspect an existing Zensical repository and identify its conventions;
- make an explicitly authorized light Markdown edit;
- review content, navigation, links, front matter, admonitions, tabs, and
  images or embeds;
- review responsive CSS, theme overrides, and landing-page conventions;
- review accessibility concerns across content, media, components, and themes;
- run a bounded tracked-file hygiene preflight before authorized commits,
  publishing, or deployment; and
- validate a build and, where feasible, affected rendered output; and
- report deployment boundaries and configuration/documentation drift.

It does not own prose craft, blog voice, SEO, generic frontend work,
autonomous publishing, or every Zensical feature. Those remain separate
editorial or presentation capabilities.

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

## Current state

- The payload passes the local Agent Skill structural validator and the pinned
  official `skills-ref` validator at agentskills commit
  `69ef37e9424c0a7ea9dd2293b559e43ec8176379`.
- The repository is licensed under MIT and has a security reporting policy.
- The initial workflows are designed around the Code Sigils Zensical blog.
- The initial fixtures run through a lockfile-pinned Zensical `0.0.60`
  scenario environment.
- The scenario suite covers tab rendering, reproducible accessibility findings,
  and non-root deployment links; it is not a complete site or WCAG conformance
  suite.
- The runner distinguishes dependency/network blocks from fixture failures and
  accepts an installed matching binary through `ZENSICAL_BIN`.
- The runtime payload includes a no-secret-output hygiene preflight for common
  tracked credential and private-key indicators; it is not a full secret scan.
- Direct Skills CLI source listing has been verified; Skills.sh search indexing
  for this repository remains pending, and no host-loader smoke check is
  claimed yet.
- Codex, OpenCode, and Hermes are the maintained compatibility targets.

These are development facts, not guarantees about every Zensical repository.
Version-sensitive behavior must be checked against the current documentation
and the target site's configuration.

## Development workflow

1. Read [`AGENTS.md`](AGENTS.md) and the relevant documents in
   [`docs/README.md`](docs/README.md).
2. Make a narrow change to the runtime payload or its supporting evidence.
3. Run the Agent Skills validator and inspect the diff for duplicated or
   drifting guidance.
4. Record changed sources, uncertainty, and the validation performed.

Do not install, execute, publish, or deploy third-party material as part of
discovery or review without explicit authorization.

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
small repeatable scenario suite for the observed failures. The next milestone
is Phase 2 component and content-model confidence. New scripts, fixtures,
integrations, and CI should earn their place through observed need.

## Status and feedback

This repository is maintained as a small, evidence-driven experiment. Please
report unclear routing, stale source assumptions, or a workflow that changes
the requested scope. A useful issue includes the target repository shape, the
authorized operation, the observed output, and the source/version involved.

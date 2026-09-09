# zensical-skill

`zensical-skill` is a focused Agent Skill for inspecting, lightly editing,
reviewing, and validating existing [Zensical](https://zensical.org/) sites.
It helps an agent preserve a repository's conventions while working with
Zensical Markdown components, navigation, media assets, and presentation
customization.

This is an early, reviewable project—not a complete Zensical automation suite.
The current payload is intentionally narrow and is being developed from real
maintenance work on the Code Sigils blog.

## Current scope

The skill currently routes these tasks:

- inspect an existing Zensical repository and identify its conventions;
- make an explicitly authorized light Markdown edit;
- review content, navigation, links, front matter, admonitions, tabs, and
  images or embeds;
- review responsive CSS, theme overrides, and landing-page conventions;
- review accessibility concerns across content, media, components, and themes;
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
└── references/              # loaded only when a workflow needs detail
docs/
├── vision.md                # purpose, boundaries, and quality criteria
├── roadmap.md               # evidence-gated implementation plan
├── research.md              # verified sources and comparable patterns
└── README.md                # maintainer reading matrix
AGENTS.md                   # maintainer change contract
CHANGELOG.md                # project-level history
LICENSE                     # MIT license
SECURITY.md                 # reporting and payload boundaries
```

The runtime payload is under `zensical/`. The `docs/` directory is maintainer
context and is not loaded as part of the skill.

## Current state

- The payload is structurally validated with the Agent Skills validator.
- The repository is licensed under MIT and has a security reporting policy.
- The initial workflows are designed around the Code Sigils Zensical blog.
- Zensical `0.0.60` is observed in that site, but fixtures are not yet pinned
  to a release.
- No independent scenario suite, public package, or host installation smoke
  check exists yet.
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

See [`docs/roadmap.md`](docs/roadmap.md). The next milestone is one complete
existing-site review and light-edit workflow with evidence-backed validation.
New scripts, fixtures, integrations, and CI should earn their place by solving
a repeated problem observed in that workflow.

## Status and feedback

This repository is maintained as a small, evidence-driven experiment. Please
report unclear routing, stale source assumptions, or a workflow that changes
the requested scope. A useful issue includes the target repository shape, the
authorized operation, the observed output, and the source/version involved.

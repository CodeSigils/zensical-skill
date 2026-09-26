# Current research state

Reviewed: 2026-09-26.

This file owns what the project currently knows to be true. Every claim here
carries a check date. A claim that can no longer be re-checked against a primary
source moves to [index.md](index.md) as a dated record rather than being
refreshed in place, and nothing in this file is history.

Sections describing a durable convention rather than a current fact are still
owned here, because an unowned convention is what drifts. When a rule also
appears in `AGENTS.md` or the runtime payload, this file records the evidence
behind it and the other file states it.

Related: [field record](index.md), [vision](../vision.md),
[roadmap](../roadmap.md), [documentation index](../README.md).

## Link effectiveness evidence

The [agent-concepts-study link-integrity research](https://github.com/CodeSigils/agent-concepts-study/blob/main/research/note-organization/link-integrity-and-stable-identifiers.md)
and its [anti-drift findings](https://github.com/CodeSigils/agent-concepts-study/blob/main/2026-07-26-DRIFT-minimum-anti-drift-strategy.md)
provide a useful cross-project reference. The transferable rules are:

- prefer stable identifiers and treat renames as repository-wide migrations;
- validate references recursively, including anchors and non-content pointers;
- separate navigation links from integrity checks and semantic relationships;
- keep one owner for each truth and link to it rather than duplicating prose;
- add links to solve a navigation need, not to inflate connectivity metrics; and
- test link controls with both valid and intentionally broken cases.

These are maintenance patterns, not universal Zensical behavior. Apply them
proportionately to the target repository and record the target's actual link
checker and deployment behavior.

## Zola skill patterns worth transferring

The existing `zola-skill` provides several transferable maintenance patterns:

- concise runtime router with progressive disclosure;
- explicit light authoring, review-only, and modification workflows;
- source registry rows containing source, verified version/date, and caveat;
- evidence-based review findings with severity, path, evidence, impact,
  remediation, and validation;
- isolated build validation and a clear deployment boundary;
- realistic scenario prompts that include prohibited unsafe advice;
- documentation-index and phase-close gates that make drift visible.

The corresponding quality pattern is also transferable: precise trigger
selection, evidence-first inspection, authorization fidelity, minimal repairs,
reproducible validation, and an honest handoff. Zola's exact commands,
templates, and fixture expectations are not transferable facts.

These are architectural patterns, not Zensical facts. Zensical-specific syntax,
commands, configuration, and supported features must be verified separately.

## Current evidence limits

- The runtime payload passes the local Agent Skill structural validator and the
  pinned official `skills-ref` validator at agentskills commit
  `69ef37e9424c0a7ea9dd2293b559e43ec8176379`.
- The initial fixture scenarios run in isolated temporary copies through the
  committed, lockfile-pinned Zensical `0.0.65` scenario environment (pin in
  `tests/scenario-env/pyproject.toml`).
- Three CI jobs are wired into the repository: the commit-message policy, the
  scenario suite, and a job running the instruction-contract self-test, the
  site-hygiene preflight, the README inventory self-test, the README inventory
  check, and `ruff check .`. All local scripts share one exit contract: 0
  clean, 1 findings, 2 could not run.
- The independent scenario suite covers tab rendering, reproducible
  accessibility findings, the deployment-instruction contract, and
  non-root deployment and sitemap output; it is not a complete site or WCAG
  conformance suite. Feeds are an admitted capability with no scenario yet.
- Direct Skills CLI installation and project-scoped host smoke checks are
  recorded; public release and long-running host-reload behavior remain
  unclaimed.

## Evidence and scope lessons from a Zola skill review

The Zola evidence reinforces four rules for this project:

- `skills-ref` conformance is a reproducible format gate only; pin its source
  revision before release.
- Structural checks, real-site behavior, host loading, and marketplace listing
  are separate evidence layers and must not be collapsed into one support
  claim.
- A capability enters the roadmap only under the capability-admission rule.
- Roadmap status is evidence, not aspiration; remove or relabel stale phase
  claims when implementation or validation changes.

The larger Zola fixture suite and future-capability document remain references,
not requirements. The current Zensical roadmap is intentionally smaller. The
blog acceptance workflow has since demonstrated a gap, and the one it
demonstrated, feeds, was admitted; the remaining deferred slices still need
their own real-site evidence.

## Acceptance-environment decision

The Code Sigils blog is the primary real-world testbed for this skill. Its
existing Zensical configuration and content exercise the components and
maintenance boundaries that matter to the first release. This is stronger
evidence than speculative fixtures, so the first behavioral validation should
run against the blog in an isolated branch or worktree. Synthetic fixtures
should be added only when a real-site failure needs a smaller reproducible case.

## Documentation governance state

Checked 2026-09-26. The canonical-owner rule is owned by `AGENTS.md` and its
documentation arm by `docs/roadmap.md` `## Capability-admission rule`. The
admission conditions are restated exactly twice: that section, and
`zensical/SKILL.md`, which keeps its own wording because an agent may read the
payload without the roadmap.

Maintainer documents carrying a `Reviewed:` marker are `docs/roadmap.md`,
`SECURITY.md`, and this file. The seven dated reports carry a date instead,
because a report's date records when it was written; four write it as a plain
`Date:` line and three as a bolded list label, so a marker search must accept
both forms. Eight of ten payload
references carry a review footer naming Zensical 0.0.65 and pointing at the
registry row; `article-review.md` is version-independent and `source-registry.md`
is the registry.

Evidence and measurements for these statements are in
`docs/reports/2026-09-26-governance-recommendations-applied.md`.

## Research-source priority

Because a personal site spans Zensical behavior, accessibility, media, design,
providers, and editorial concerns, agents should use web search as a research
instrument without flattening all sources into one authority order. Inspect the
repository first; use current official Zensical documentation for Zensical-
specific behavior; then consult W3C or other standards and primary provider
documentation for cross-cutting claims. Community guides are useful for
alternatives and practical observations when clearly labelled. Cached blog
posts and search snippets are discovery leads, not evidence.

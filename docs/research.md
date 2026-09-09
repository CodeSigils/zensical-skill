# Research and design record

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

- The runtime payload has been validated for structure with the skill creator's
  validator.
- A current Zensical version has not yet been pinned for fixtures.
- Admonition and tab behavior has been used in the Code Sigils site, but the
  skill has not yet run an independent scenario suite.
- Public package installation and host-specific smoke checks are deferred.

## Blog research evidence

The Code Sigils repository provides a useful, but site-specific, Zensical
reference. Its `pyproject.toml` currently pins Zensical `0.0.60`; its
`zensical.toml` demonstrates the `[project]` configuration shape, feature
toggles such as `content.tabs.link`, implicit navigation, and the warning that
replacing the complete Markdown-extension configuration can remove defaults.
Its landing page exercises admonitions, collapsible blocks, code annotations,
content tabs, diagrams, footnotes, formatting, task lists, and tooltips.

These observations are valuable evidence for future fixtures and guidance, but
they are not universal defaults. Verify each behavior against the current
Zensical documentation and a target repository before promoting it into the
runtime skill.

The initial portability target is deliberately small: Codex, OpenCode, and
Hermes. Their installation and discovery mechanisms still need to be verified
from current host documentation before being written as release commands. A
single portable payload and shared scenarios are preferred over host-specific
copies or parallel CI pipelines.

Update this record when a primary source or real workflow changes the skill's
decision boundary. Do not turn one site's convention into a universal rule.

## Related skill discovery (2026-09-09)

The first related-skill search found no direct Zensical skill in the sources
that were reachable. Relevant
comparators were the local `zola-skill`, Hermes `project-state-audit` and
`config-doc-drift-prevention`, and the external `docs-guard` project. They
offer useful patterns for source-of-truth routing, drift detection, and
evidence-based documentation review, but none should become a Zensical
dependency without a separate compatibility and maintenance review.

The search also exposed a discovery-process risk: a local `learn-skills.dev`
checkout may contain recent generated metadata while still being an unverified
mirror. The checkout used in that search later proved to match
`upstream/main`, but that check happened after the search. Future searches must
query the documented remote artifact/API directly, or explicitly record the
checkout's remote, revision comparison, generation timestamp, and sync status
before relying on it. Local filesystem search remains appropriate for installed
and project skills; it is not a substitute for a fresh external catalog query.

The remote catalog could not be re-queried during final verification because
DNS/network access was unavailable, so absence is provisional rather than
proof that no such skill exists. No candidate was installed, copied, executed,
or added as a dependency.

### Remote follow-up search

The remote GitHub/web search was repeated on 2026-09-09 using `Zensical`,
`MkDocs`, `static site`, and `documentation site` with `SKILL.md` qualifiers.
It found no clearly maintained, direct Zensical skill. Search results were
mostly Agent Skills specifications or general documentation skills.

Two references are useful as patterns rather than dependencies:

- [`using-agent-skills`](https://github.com/addyosmani/agent-skills/blob/main/skills/using-agent-skills/SKILL.md)
  uses a task-to-workflow router, explicit assumption surfacing, a stop-on-
  confusion rule, pushback against weak approaches, scope discipline, and
  evidence-based verification. Borrow the behavioral gates; do not copy its
  broad software-lifecycle map into a Zensical skill.
- [`documentation-and-adrs`](https://github.com/addyosmani/agent-skills/blob/main/skills/documentation-and-adrs/SKILL.md)
  matches existing repository conventions before creating documents, records
  rationale and alternatives, preserves superseded decisions, and treats ADRs
  as context for future agents. Borrow its “why”, convention-first, and
  lifecycle ideas for site maintenance notes.

The current Agent Skills specification confirms that `SKILL.md` is required,
supporting scripts/references are optional, and progressive disclosure is the
intended structure. This validates the current narrow payload shape but is not
evidence that either reference is Zensical-compatible.

The follow-up was static and read-only. Candidate scripts were not executed;
no installation or behavior smoke test was authorized.

## Evidence and scope lessons from the latest Zola review

The latest Zola evidence reinforces four rules for this project:

- `skills-ref` conformance is a reproducible format gate only; pin its source
  revision before release.
- Structural checks, real-site behavior, host loading, and marketplace listing
  are separate evidence layers and must not be collapsed into one support
  claim.
- A capability enters the roadmap only after a user need, observed failure,
  primary-source evidence, bounded fixture, and maintenance owner exist.
- Roadmap status is evidence, not aspiration; remove or relabel stale phase
  claims when implementation or validation changes.

The larger Zola fixture suite and future-capability document remain references,
not requirements. The current Zensical roadmap is intentionally smaller until
the Code Sigils blog acceptance workflow demonstrates a gap.

## Acceptance-environment decision

The Code Sigils blog is the primary real-world testbed for this skill. Its
existing Zensical configuration and content exercise the components and
maintenance boundaries that matter to the first release. This is stronger
evidence than speculative fixtures, so the first behavioral validation should
run against the blog in an isolated branch or worktree. Synthetic fixtures
should be added only when a real-site failure needs a smaller reproducible case.

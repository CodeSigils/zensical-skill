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

## Independent Zensical capability review (2026-09-09)

Zola is an architectural reference for repository discipline, not a capability
baseline. Current official Zensical documentation shows a broader, partly
batteries-included surface:

- a native `zensical.toml` project scope plus compatibility with existing
  `mkdocs.yml` projects and most Material for MkDocs settings;
- Python Markdown and a large set of supported extensions, including
  admonitions, tabs, tooltips, task/definition lists, snippets, and diagrams;
- implicit or explicit navigation, sections, tabs, instant navigation,
  previews, breadcrumbs, pruning, and section index pages;
- a built-in development server and preview workflow;
- theme customization through MiniJinja-compatible templates and Material
  extensions; and
- workspace watch and symlink rules that affect what content is visible during
  builds.

These features create distinct Zensical concerns that should not be collapsed
into a generic “Markdown site” workflow. The runtime skill should initially
route only the subset already exercised by the Code Sigils blog. The roadmap
may later add focused capability references when a real site task demonstrates
the need.

The independent review also identified two version-sensitive cautions to keep
visible: Zensical's Markdown compatibility currently follows Python Markdown,
including four-space indentation behavior, and some navigation features have
explicit incompatibilities (for example, pruning versus expansion). A target
repository's configuration and current official documentation remain the
source of truth.

Primary sources checked:

- [Zensical basics](https://zensical.org/docs/setup/basics/)
- [Navigation](https://zensical.org/docs/setup/navigation/)
- [Markdown](https://zensical.org/docs/authoring/markdown/)
- [MkDocs compatibility](https://zensical.org/docs/compatibility/mkdocs/)
- [Python Markdown extensions](https://zensical.org/docs/compatibility/markdown/python-markdown/)
- [Customization](https://zensical.org/docs/customization/)
- [Get started](https://zensical.org/docs/get-started/)

## Phase 1 acceptance run (2026-09-09)

The first real-site review used the Code Sigils blog at
`/home/sand/labs/zensical-test` and the `free-ai-models.md` article as the
review target. The source checkout remained clean. Its declared environment
uses Python `>=3.13`, Zensical `0.0.60`, `uv`, implicit navigation, native
search, linked tabs, navigation pruning, and GitHub Pages deployment.

The documented command `uv run zensical build --clean` could not write to the
read-only source checkout in this environment. Running the same command from
an isolated copy under `/tmp` succeeded:

- Zensical build: passed with `No issues found`;
- rendered output: 18 HTML files, including the target route;
- native search output: `site/search.json` generated (164,788 bytes);
- rendered target: article metadata, admonitions, OpenCode content, feature
  flags, and canonical resource links were present;
- source mutation: none.

This is partial behavioral evidence for inspection, rendering, search, and
review boundaries—not proof of host discovery, deployment success, or every
Zensical component. The next acceptance slice should exercise a tabbed article,
navigation/link review, and an explicitly authorized light edit in an isolated
branch or worktree.

## Tab-awareness acceptance slice (2026-09-09)

The next slice used `docs/JS-TS/oxc-formatting.md` in an isolated clone and
branch (`codex/zensical-tabs`). The source contained package-manager commands
written as separate one-label tab blocks with unindented code fences. Zensical
therefore built successfully but rendered empty tab panels; this is a semantic
rendering failure that a build-only check does not catch.

The authorized light edit grouped each equivalent installation command inside a
single tab set and added the missing Bun option. Commit `fd85f61` contains only
that article change. Rebuilding with the installed Zensical `0.0.60` binary
passed with `No issues found`; rendered HTML showed one `data-tabs="1:4"` group
and one `data-tabs="2:4"` group, each with non-empty npm/pnpm/yarn/bun panels.

This validates a concrete tab-awareness rule: equivalent package-manager
commands belong in one complete tab group, and rendered output must be checked
for panel content rather than trusting a successful build. The branch was not
published or pushed; the original blog checkout remained unchanged.

## Navigation and internal-link acceptance (2026-09-09)

The rendered isolated site was checked after the tab edit. The target article
contained its expected route, breadcrumb/sidebar navigation, footer navigation,
and related internal links. A read-only pass over all generated HTML checked 280
internal links and found no missing local targets, including root-absolute links
from the 404 page. This provides evidence for generated navigation and local
link integrity; it does not validate external URLs, browser interaction, or
deployment-host routing.

### Disco and native search

Zensical's current search documentation describes native client-side search,
enabled by default, with offline support and page/section/block exclusion
controls. The Zensical roadmap identifies the underlying engine as Disco, a
modular search system intended to evolve beyond the current integrated use.
Agents maintaining a Zensical site should therefore inspect the native search
configuration and generated behavior before proposing an external search
service. This is especially important for privacy, offline distribution, and
avoiding an unnecessary runtime dependency.

This does not mean the skill should configure or tune Disco automatically. It
should report the target site's search state, recognize exclusions and relevant
feature flags, and verify version-sensitive behavior against current sources.
The search interface is currently English-only while multilingual content
search is supported; this distinction should not be turned into a claim that
multilingual search is unavailable.

Sources: [Zensical site search](https://zensical.org/docs/setup/search/) and
[Zensical roadmap](https://zensical.org/about/roadmap/).

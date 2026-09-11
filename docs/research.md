# Research and design record

This is an active evidence index, not a graveyard. Each substantial entry must
support a current workflow, decision, or roadmap gate. When evidence is
superseded, mark the version/date and explain whether it was replaced, retained
as historical context, or removed. Keep detailed dated execution notes in the
related session record; keep this document concise enough to re-check.

Related documents: [vision](vision.md), [roadmap](roadmap.md),
[documentation index](README.md), and the
[source registry](../zensical/references/source-registry.md).

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

## Evaluation: lightweight article link manifests

The proposed middle ground is worth keeping as an evaluation, but not as a
new runtime requirement. A small optional manifest can record important
external URLs, their role, `last_verified` date, and a simple check cadence;
article Markdown remains the human-readable source. A generated inventory can
show all links without making a second manually maintained copy mandatory.

Zensical has a natural fit for only part of this design. Its current
[validation documentation](https://zensical.org/docs/setup/validation/)
states that internal links and anchors are checked during builds, and strict
mode can fail a CI build when issues are found. Its
[Markdown guidance](https://zensical.org/docs/authoring/markdown/) recommends
relative links so pages can move with a site and its `site_url` can change.
These native checks should remain the primary path for local integrity.

The external portion is separate. Zensical's documented
[GitHub Pages workflow](https://zensical.org/docs/publish-your-site/) builds and
publishes on pushes, but does not define an article manifest or scheduled
external-URL monitor. If the blog later needs this, add one small advisory
scheduled workflow that checks selected manifests with limited retries and
reports failures for review. It should not rewrite articles or block ordinary
publishing. Normalize URLs before comparing manifest entries so fragments,
trailing slashes, and harmless query differences do not create false drift.

**Disposition:** retain as a future, optional maintenance slice. Do not add a
manifest to every article until link inventory or a real rot incident shows
that inline links plus Zensical's native checks are insufficient.

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
  committed, lockfile-pinned Zensical `0.0.60` scenario environment.
- The independent scenario suite covers tab rendering, reproducible
  accessibility findings, and non-root deployment links; it is not a complete
  site or WCAG conformance suite.
- Public package installation and host-specific smoke checks are deferred.

## Browser-rendered accessibility evidence (2026-09-11)

A BrowserOS review of the deployed Code Sigils homepage and OpenCode guide
confirmed the expected language, main/article landmarks, skip links, image
alternative, titled YouTube iframe, desktop reflow, and absence of page-console
errors. It was a narrow desktop-browser check, not a mobile, contrast,
caption/transcript, assistive-technology, or WCAG-conformance audit.

The review found 202 empty, zero-width, focusable code-line anchors in the
OpenCode guide. The target used Zensical `0.0.60` with the default
`pymdownx.highlight.anchor_linenums = true`. An isolated build using the full
0.0.60 default extension list and `anchor_linenums = false` succeeded, retained
line spans, and removed the generated anchors. The live-site configuration was
then changed and rebuilt successfully. This is a focused acceptance finding;
it does not establish that all Zensical versions or sites have the same issue.

The acceptance finding now has a dedicated, lockfile-backed `code-anchor-site`
fixture. It makes the 0.0.60 extension defaults explicit, disables
`anchor_linenums`, and asserts that generated line spans remain while
`__codelineno-*` anchors do not appear. The fixture stays separate from the
iframe-title case so each assertion represents one repairable behavior.

The same review considered analytics and discoverability. The evidence supports
an opt-in decision boundary rather than a new runtime workflow: inspect a
target's canonical URL, metadata, robots, and sitemap when asked; start with
Search Console for indexing questions; do not add GA4 or consent configuration
without a concrete measurement question, authorization, and privacy review.
The current Zensical analytics integration is documented as under overhaul.

## Media semantics and new-tab link policy (2026-09-11)

The existing media workflow already requires meaningful alternatives,
descriptive iframe titles, appropriate captions/transcripts, player controls,
and rendered inspection. The durable refinement is to make raw HTML media a
contextual semantic review: inspect native controls, caption tracks or provider
captions, transcripts where needed, and reader-impacting autoplay/loop choices.
It does not prescribe `sandbox`, `referrerpolicy`, or provider attributes,
because those need provider-compatibility and site-privacy evidence.

Current MDN documentation states that `target="_blank"` provides implicit
`noopener` behavior in modern HTML. An explicit `rel="noopener"` can be a
project convention, but `noreferrer` also suppresses the HTTP referrer and is
therefore a privacy/attribution decision, not a universal security repair.
The runtime now asks for that decision only when a link intentionally opens a
new tab. No dedicated fixture was added: no target-site failure or repeated
Zensical rendering behavior has established a deterministic assertion.

## Maturity assessment (2026-09-11)

The payload currently contains 13 runtime files (628 lines across its router
and references) and five bounded acceptance scenarios. It is therefore best
understood as a work-in-progress, evidence-led maintenance playbook with a few
deterministic checks—not a comprehensive Zensical linter, browser test suite,
or accessibility conformance system. Its fixtures cover observed rendering and
configuration behavior, while media-provider operation, broad browser coverage,
and deployment remain bounded review concerns. The roadmap retains the current
narrow scope until two or three materially different real maintenance tasks
demonstrate a repeated, testable gap.

The resulting direction is not a permanent ceiling: it may become a reusable
methodology or automation capability if value is demonstrated. For each
proposal, the agent must first inspect the target repository and reconsult
current official Zensical documentation, then evaluate the installed version,
user value, validation path, maintenance owner, and authorization boundary.
That consultation should produce a concise, target-relevant set of documented
options for the user, including fit, trade-offs, and verification needs rather
than an exhaustive feature list or an implied configuration change.

## Sensitive-material preflight (2026-09-09)

The runtime now has a small Git-tracked-file preflight for common environment,
key, credential-file, and high-confidence token signatures. It reports paths
and finding types only, exits nonzero on candidates, and requires maintainer
direction before any remediation. It deliberately does not scan Git history,
ignored/untracked files, or every provider-specific format, and it does not
rotate credentials or rewrite history. GitHub's current secret-scanning and
sensitive-data-removal guidance supports that boundary: a real exposed secret
must be rotated or revoked before any coordinated history-removal work.

## Locked scenario-environment maintenance (2026-09-09)

The deterministic fixtures now use one committed `tests/scenario-env/uv.lock`
instead of independently resolving their direct dependencies. The environment
pins Zensical `0.0.60` and its resolved transitive graph; fixture directories
contain only the site inputs that the runner copies into isolation. The lock
was checked offline with `uv lock --check --offline --project
tests/scenario-env`, and the scenario runner passed against the matching
installed binary from the Code Sigils blog.

An isolated copy of `/home/sand/labs/zensical-test` was also rebuilt with that
binary. It passed with `No issues found`, generated 18 HTML files plus native
search output, and retained the tabbed OXC and embedded-media OpenCode routes.
The source checkout remained clean. This revalidates the current fixture
environment against the real acceptance site; it does not establish release,
host discovery, or deployment evidence.

## Blog research evidence

## Scenario assertion hardening (2026-09-09)

The isolated fixture runner now checks four rendered tab panels and their
command labels, keeps a correctly titled iframe alongside the intentional
missing-title finding, and verifies a nested page links back to the homepage
under the configured `/docs/` deployment path. The strengthened suite passed
with the pinned Zensical `0.0.60` package loaded from the local uv cache via
`ZENSICAL_BIN`; no network or source-site mutation was required. The iframe
assertion now uses Python's HTML parser, so it does not require `rg` PCRE2
support; `rg` remains a general runner prerequisite.

This improves regression confidence for the three observed boundaries without
claiming complete tab, accessibility, or deployment coverage.

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

## Media and asset capability review (2026-09-09)

The current Zensical documentation gives images a richer supported path than
other media: attribute-list alignment, captions/figures, lazy loading,
light/dark variants, and the optional GLightbox image gallery extension. The
official reference set does not describe an equivalent native video or audio
authoring component. Those commonly remain raw HTML, CSS, JavaScript, or
external-provider integrations and therefore need separate rendered and
privacy/offline checks.

The Code Sigils blog exercises this mixed model: local SVG/PNG/JPEG/WebP
assets, inline HTML images, and YouTube iframes styled by custom CSS. A build
can prove that these elements were emitted, but not that an external player
loads, that a caption is accessible, or that a media URL survives a deployment
subpath. The media reference now requires asset existence, alt text, responsive
dimensions, fallback/caption handling, base-path behavior, provider/privacy
boundaries, and explicit size/licensing decisions.

Primary sources: [Zensical images](https://zensical.org/docs/authoring/images/),
[GLightbox](https://zensical.org/docs/setup/extensions/glightbox/), and
[Zensical customization/assets](https://zensical.org/docs/customization/).

## Video-heavy article acceptance review (2026-09-09)

Review-only testing used `docs/AI/OpenCode/opencode-guide.md` in an isolated
copy of the Code Sigils blog. The documented Zensical `0.0.60` build passed with
`No issues found`. The generated page emitted the local OpenCode screenshot,
loaded `stylesheets/extra.css`, and preserved the responsive
`youtube-video-wrapper` and 16:9 iframe rules. The local image target existed in
the generated output, and the source checkout remained clean.

The review found one actionable accessibility concern: the YouTube iframe has
`allowfullscreen` but no descriptive `title` attribute. This is a review
finding, not an authorized edit. Static build and HTML inspection cannot prove
that YouTube loads, that keyboard focus behaves correctly, or that the remote
provider remains available offline.

## Accessibility baseline (2026-09-09)

Accessibility is now a cross-cutting quality concern rather than an ARIA-only
feature. The skill uses WCAG 2.2 and W3C guidance as the review baseline:
prefer semantic HTML and visible names, use `alt` according to image purpose,
provide captions and transcripts for time-based media, label iframes, preserve
keyboard and focus behavior, and check contrast, zoom/reflow, color
independence, and reduced motion where presentation changes. Static checks and
Zensical builds provide evidence about emitted markup only; they do not certify
WCAG conformance or replace browser and assistive-technology testing.

Accessibility can support discoverability through crawlable structure,
descriptive alternatives, and usable content. It should remain a quality and
inclusion goal rather than being reduced to keyword, ranking, or SEO advice.

Sources: [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [W3C Images Tutorial](https://www.w3.org/WAI/tutorials/images/), [W3C Audio and Video Media](https://www.w3.org/WAI/media/av/), and [W3C Accessible Names](https://www.w3.org/WAI/ARIA/apg/practices/names-and-descriptions/).

## Presentation and landing-page capability review (2026-09-09)

The blog supplies a real customization reference: `extra_css` loads scoped
responsive rules for YouTube wrappers and images, while `docs/index.md` acts as
the public landing page with front matter, introductory sections, admonitions,
tabs, diagrams, and links. The current Zensical customization documentation
also supports `extra_javascript`, `custom_dir`, MiniJinja template overrides,
focused `main.html` block extensions, and page-selected templates through front
matter. Its guidance favors focused block overrides over replacing `base.html`
because the latter is more likely to drift across releases.

This evidence expands the skill's awareness without making it a generic
frontend skill. It should inspect existing CSS and theme conventions, preserve
responsive and accessibility behavior, test narrow viewports and configured
color schemes when relevant, and treat custom templates and third-party
embeds as version-sensitive. A build proves emission, not visual layout,
keyboard behavior, contrast, or remote-player availability.

Primary sources: [Zensical customization](https://zensical.org/docs/customization/),
[front matter](https://zensical.org/docs/authoring/frontmatter/), and
[colors](https://zensical.org/docs/setup/colors/).

## Research-source priority

Because a personal site spans Zensical behavior, accessibility, media, design,
providers, and editorial concerns, agents should use web search as a research
instrument without flattening all sources into one authority order. Inspect the
repository first; use current official Zensical documentation for Zensical-
specific behavior; then consult W3C or other standards and primary provider
documentation for cross-cutting claims. Community guides are useful for
alternatives and practical observations when clearly labelled. Cached blog
posts and search snippets are discovery leads, not evidence.

## Front matter, base path, and asset acceptance (2026-09-09)

The isolated `opencode-guide.md` build confirmed that front matter generated the
expected title, description, and canonical URL
(`https://codesigils.github.io/AI/OpenCode/opencode-guide/`). The configured
stylesheet resolved under the generated route, and the root-absolute local
OpenCode screenshot existed in the output. The article's YouTube iframe remained
external and lacked a descriptive `title`; this is an accessibility finding,
not a build failure. The source blog checkout remained clean.

## Accessibility acceptance review (2026-09-09)

The rendered `opencode-guide.md` page was reviewed for basic accessibility
signals. It had a logical heading sequence with no level jumps, standard
header/nav/main/article/footer landmarks, no empty links, and an image with an
`alt` attribute. Two suggestions remain: add a descriptive `title` to the
YouTube iframe, and provide a nearby transcript or clearly labelled descriptive
fallback when the video's visual information is relevant. These are review
findings only; no source edit was authorized, and no browser, keyboard, screen
reader, contrast, or automated WCAG audit was performed.

This exposed an execution gap in the first acceptance pass: accessibility rules
existed, but the workflow did not route to a structured a11y report. The skill
now treats rule presence and workflow invocation as separate acceptance claims.

## Phase 2 rendered component repair (2026-09-10)

An isolated, lockfile-pinned Zensical `0.0.60` build of the clean Code Sigils
blog completed with `No issues found` and generated 18 HTML pages. Rendered
inspection then found two empty content-tab panels on `docs/index.md`: the
Python and Rust fences were adjacent to their tab labels instead of nested
inside them. The build did not report this semantic rendering failure.

The same pass found three YouTube iframes without descriptive `title`
attributes in the OpenCode, Hermes Agent, and Dolphin LLM guides. The affected
images had explicit alternatives, and the existing responsive CSS remained
scoped to the image and YouTube wrappers. The authorized repair indented the
two tab bodies and added descriptive iframe titles. The existing pinned
fixtures already cover non-empty tab panels and missing iframe titles, so this
real-site confirmation did not add another fixture.

Validation must rebuild an isolated copy and inspect the homepage's tab panels
plus the three rendered iframe titles. Browser keyboard, contrast, remote
player availability, captions, and transcript adequacy remain separate manual
checks; this result does not claim WCAG conformance.

## Skills CLI discovery regression (2026-09-10)

An isolated `npx --yes skills find zensical` query returned 20 indexed
candidates. The result included `layeredcraft/skills@zensical-site` (9
installs) and related setup, authoring, and debugging skills, but did not
surface `CodeSigils/zensical-skill`. The command completed successfully through
the Skills.sh provider; no installation or execution of a candidate was
performed. This confirms Skills CLI is useful as a retrieval stage while its
result set remains neither a quality assessment nor proof of complete indexing.

## Project-scoped host smoke checks (2026-09-10)

In one isolated temporary root, the portable `zensical/` payload was copied to
the documented project-scoped locations for Codex (`.agents/skills/zensical`),
OpenCode (`.opencode/skills/zensical`), and Hermes (`.hermes/skills/zensical`).
Each copy had a non-empty runtime `SKILL.md`, and the `site-inspection.md` and
`validation.md` references resolved from that runtime directory. The temporary
root was removed after validation. These are file-availability and path
discovery checks, not claims that a long-running host session has reloaded the
skill or that public package installation succeeds.

## Skills CLI clean installation (2026-09-10)

Skills CLI `1.5.25` ran `npx --yes skills add CodeSigils/zensical-skill
--skill zensical --agent codex --copy --yes` from an isolated temporary
directory. The provider cloned public `main` at
`23de5a7d01de6467133976cfd9c968b9f7404a6c`, found one skill, and copied the
complete payload to `.agents/skills/zensical`: `SKILL.md`, `agents/openai.yaml`,
nine references, and `scripts/check_site_hygiene.sh`. The temporary directory
was removed after inspection. This proves the current direct-source installation
path for Codex; it does not establish marketplace search indexing, a published
release, or long-running host reload behavior.

## Live Code Sigils blog audit (2026-09-10)

The clean `CodeSigils/CodeSigils.github.io` checkout at
`/home/sand/labs/zensical-test` was copied to a temporary directory and built
with its locked Zensical `0.0.60` environment. The build completed with `No
issues found` and produced 18 HTML pages. Static generated-output inspection
found three iframes with non-empty titles and 22 images with explicit `alt`
attributes; source inventory found eight content tabs, three iframes, and 57
admonitions. This is static/rendered evidence only, not browser keyboard,
contrast, captions/transcripts, remote-player, or deployment evidence.

One documentation-drift finding was recorded: the blog's `AGENTS.md` said the
deployment workflow watches only `docs/**`, `zensical.toml`, and its workflow
file and runs `pip install zensical` then `zensical build --clean`. The actual
`.github/workflows/docs.yml` also watches `pyproject.toml`, `uv.lock`, and
`.python-version`, runs `uv sync --locked`, then runs `uv run zensical build
--clean`. The authorized repair reconciled the instructions, and the new
bounded instruction-contract check covers this layout. The result remains
static workflow evidence, not deployment success.

## Related Zensical skill comparison (2026-09-09)

Two Skills.sh candidates were downloaded for static comparison into an
isolated project directory; neither was installed into a client skill path or
executed. `layeredcraft/skills@zensical-site` (MIT, repository updated
2026-09-09) has a progressive authoring router, voice/tone and content-type
references, front-matter and Markdown guidance, configuration caveats, and a
page-draft template. These are useful patterns for future authoring support,
but the skill targets Zensical.org content and does not cover real-site
maintenance, security hygiene, or bounded deployment checks.

The candidates show that authoring references and templates could complement
this skill, but they do not justify widening the runtime router yet. Admit a
feature only after a Code Sigils blog need, current primary-source evidence, a
bounded scenario, and a maintenance owner exist.

The first discovery pass missed these candidates because it did not run a
fresh, broad Skills CLI search. A follow-up `npx --yes skills find zensical`
query (2026-09-09) returned multiple indexed candidates, while direct source
listing confirmed `CodeSigils/zensical-skill` is installable but not yet
surfaced by search. Future discovery should use Skills CLI as a retrieval
stage after local and documented catalog checks, record query time and provider
status, inspect canonical repositories, and treat missing search results as
provisional rather than evidence of absence. The command downloads and runs
external CLI code, so it requires explicit authorization and an isolated
environment.

## Core source-registry freshness check (2026-09-10)

The official Zensical documentation and project home page were rechecked from
their canonical URLs. The documentation site was reachable but did not expose
a single global release version; the home page describes Zensical as an
open-source technical-writing system built by the creators of Material for
MkDocs. The registry therefore records the check date and retains the
target-lockfile requirement for version-sensitive syntax and installation
commands. This verifies source freshness and project identity, not a new
Zensical release or compatibility guarantee.

## Skills.sh indexing escalation and resolution (2026-09-10)

Direct Skills CLI discovery rechecked the public `CodeSigils/zensical-skill`
repository at `09e89eba53ff1ed2f4a5f89a6d6a02d1eb889ff1` and found its one
`zensical` skill. The Skills.sh API initially returned 31 matches for
`zensical` and three other CodeSigils skills, but omitted this repository. At
the same time, the canonical skill page returned HTTP 200 while the repository
page returned HTTP 404. The evidence and an indexing request were recorded in
[`vercel-labs/skills#2205`](https://github.com/vercel-labs/skills/issues/2205).

A same-day recheck returned `codesigils/zensical-skill/zensical` in both the
`zensical` and `CodeSigils` searches (32 and four results respectively), and
both the repository and skill pages returned HTTP 200. The requester posted
the verification and closed the issue. This confirms directory indexing only;
it does not establish ranking, verification, support, or public-release status.

## Current-main Skills CLI package refresh (2026-09-10)

The documented direct-source command was re-run in a disposable Codex project
with Skills CLI `1.5.25`. It cloned `main` at
`d7ef1e05583593d66e79fce807f38979566f088c`, found the one `zensical` skill,
and copied all thirteen payload files to `.agents/skills/zensical`: the
entrypoint, Codex metadata, nine references, and both runtime scripts. The
temporary project was removed after inspection. The CLI displayed provider risk
assessments during installation, but this record makes no independent safety,
support, or compatibility claim from those labels.

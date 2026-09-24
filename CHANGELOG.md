# Changelog

## Unreleased

- Refined the optional article review with three light behavioral guards
  borrowed from community de-slop skills: an over-correction guard, an
  authority-precedence rule for conflicting guidance, and second-generation
  "performed authenticity" tells; the sources and non-adopted heavy
  techniques are recorded in the editorial-voice research.
- Trimmed the `README.md` positioning paragraph to its scope statement,
  removing the product-facing/Code Sigils-and-Digital-Basement framing.
- Added a minimal validation gate in CI (`validate.yml`: commit-message
  policy and the shared scenario suite on push and pull request) after the
  governance audit; GitHub Releases and semver tags stay optional.
- Made the scenario runner and its assertions use portable `grep` instead of
  `rg`, so the validation gate needs no extra host tooling beyond `uv`.
- Moved research records under `docs/research/` and added dated audit records
  under `docs/reports/`; all references and reading-matrix rows updated.
- Recorded the agentskills specification and skills.sh CLI packaging
  conventions (frontmatter contract, payload layout, `agents/openai.yaml`
  scope, and our payload's status) in a dedicated
  `docs/research/skill-structure-conventions.md` reference.
- Refreshed `README.md` (repository map, scenario coverage, CI gate note, and
  canonical specification link), added a `docs/roadmap.md` revision history, and
  hardened `.gitignore` with cache, secret, and IDE/agent-artifact patterns.

- Allowed the optional article review to load an installed community de-slop
  skill as an additional lens when the user explicitly asks for a more human
  voice pass, always applied at sentence level with the density and quotation
  caveats; preferred skills and a ranking are recorded in the editorial-voice
  research.

- Expanded the optional article-review guidance with a compact catalogue of
  machine-typical prose tells (antithesis inversions, opener tics, filler
  hedges, formulaic lists, padding tails) plus density and quotation
  caveats, and recorded the supporting external evidence in a dedicated
  editorial-voice research file.

- Kept second-target release evidence in maintainer records only; the runtime
  source registry remains target-generic and contains no MapLibre-specific
  paths or canonical URLs.

- Tightened the runtime source-registry contract: primary-source pointers and
  generic caveats belong in the payload; target paths, counts, revisions, and
  test results belong in maintainer research records.

- Reconciled roadmap gates: the sitemap/canonical slice is admitted after two
  target validations, while generic authoring, content-model, theme-override,
  language, and feed workflows remain separately evidence-gated.

- Added a mandatory project-agent roadmap after-action gate for consequential
  work: agents must read the roadmap before acting, revisit it afterward, and
  record either the updated gate or an intentional no-change decision.

- Added bounded sitemap and canonical-URL validation for explicit release-output
  reviews, including a non-root deployment-path fixture and matching robots
  directive assertion.

- Added a verified-edit handoff: focused, validated pending Git changes are
  identified as ready to commit and the agent offers that next step without
  inferring commit, push, publish, or deployment authorization.

- Added a narrow new-article placement rule: choose an existing category from
  the primary reader question and request direction only when placement would
  materially change audience or navigation.

- Clarified optional article review: it follows target-repository guidance and
  offers portable content suggestions without imposing a voice, article
  formula, SEO strategy, or publication gate.

- Added the initial portable Zensical maintenance skill: repository inspection,
  bounded light edits and reviews, content components, media, presentation,
  accessibility, validation, and explicit publishing boundaries.
- Added evidence-gated maintainer records, release/discoverability checks, and
  a source registry so target-repository conventions and current primary
  sources remain authoritative.
- Added a pinned Zensical `0.0.60` scenario environment covering rendered tabs,
  iframe-title review findings, and non-root deployment links, with an offline
  `ZENSICAL_BIN` path and explicit environment-block reporting.
- Added a bounded no-secret-output tracked-file hygiene preflight before
  authorized publication work.
- Clarified that Code Sigils is acceptance evidence rather than a target-site
  convention, and that the listed Skills CLI command remains a candidate until
  a clean host-install smoke test is recorded.
- Added an optional browser-rendered accessibility check and a version-sensitive
  code-line-anchor finding, while keeping analytics and search discoverability
  outside the runtime workflow unless explicitly requested.
- Added a pinned rendered fixture proving that the documented code-line-anchor
  repair preserves line spans without emitting empty keyboard tab stops.
- Clarified proportionate semantic review for raw HTML media and intentional
  new-tab links, including the boundary between `noopener` conventions and an
  explicitly authorized `noreferrer` privacy policy.
- Marked the payload explicitly as work in progress and added an evidence-gated
  directive against overstating coverage or expanding it without a proven need.
- Required current official Zensical documentation and target-version review
  before evaluating proposed additions, integrations, workflows, or automation.
- Require capability evaluations to offer users a concise, documented,
  target-relevant set of options with trade-offs and validation needs.
- Added a maintainer-only cross-project consistency gate for the related
  Digital Basement umbrella records when the skill's role or maturity changes.
- Clarified that the skill is usable for its documented, evidence-backed scope
  while actively developed beyond it.

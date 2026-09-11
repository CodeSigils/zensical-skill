# Roadmap

The roadmap is evidence-gated. A phase is complete when the workflow works on
the target blog and its limits are documented—not when every possible feature
has a placeholder.

## Priority order

1. **Prove the core workflow:** existing-site inspection, one light edit, and
   one review-only pass with an honest handoff.
2. **Stabilize component checks:** admonitions, content tabs, links, front
   matter, navigation, and rendered output.
3. **Add maintenance evidence:** source/version registry, drift checks, and a
   small shared validation suite.
4. **Release deliberately:** verify project-scoped discovery for Codex,
   OpenCode, and Hermes before considering public distribution.

The release gate includes the official `skills-ref` validator, a clean payload
tree, host-specific discoverability checks, and a documented skills.sh or
marketplace result. Marketplace presence is treated as distribution evidence
only; rankings, install counts, and badges do not establish quality or
compatibility. See [release-checklist.md](release-checklist.md).

## Current status

The core existing-site workflow has been exercised against the Code Sigils
blog. Inspection, an authorized tab light edit, navigation and internal-link
review, media and video review, presentation review, and a structured
accessibility pass all have recorded evidence in `docs/research.md` and the
Digital Basement session note. The observed tab, accessibility-invocation, and
non-root-link failures are now covered by a small repeatable fixture suite.
Further fixture work remains conditional on a real-site gap. The runtime also
includes a bounded tracked-file hygiene preflight for authorized publication
work; it is intentionally not a comprehensive secret-scanning claim.

Phase 2 is substantially proven for the target-used component and presentation
paths: admonitions, tabs, front matter, navigation, base paths, images, local
assets, video embeds, responsive CSS, and the landing page all have official
source and Code Sigils evidence. A narrow BrowserOS desktop review now also
confirms rendered structural and media signals and produced a repaired
code-line-anchor keyboard finding. GLightbox was documented as an optional
extension rather than enabled without a target need. Browser keyboard,
contrast, narrow-view reflow, captions/transcripts, remote-player availability,
and deployment remain manual or provider-bound checks rather than completion
claims.

No public release is claimed. Project-scoped host installation smoke checks are
recorded for Codex, OpenCode, and Hermes, and the public Skills.sh directory
now indexes the payload; public release remains Phase 3 work.

See the [research record](research.md) for the evidence behind this status and
the [vision](vision.md) for the quality criteria.

## Capability-admission rule

Do not add a new Zensical workflow, integration, or validation control merely
because the framework supports it. Admit a capability only when all five
conditions are present:

1. a concrete user need;
2. an observed failure or repeated workflow;
3. current primary-source evidence;
4. a bounded fixture or scenario that can prove the behavior; and
5. a named maintenance owner.

Keep structural validation, behavioral validation on the Code Sigils blog,
host discoverability, and marketplace availability as separate claims. A pass
in one layer must not imply a pass in another.

## Acceptance environment

The Code Sigils blog is the first real acceptance environment. It already
contains the Zensical features and maintenance conditions this skill must
understand: navigation, admonitions, content tabs, links, configuration,
editorial conventions, and a live deployment boundary. Use it to test behavior
before inventing synthetic fixtures. Run experiments in a branch or isolated
worktree, and keep validation separate from publication.

## Phase 1 — Existing-site review and light editing (substantially proven)

- [x] Test the runtime routing and review guidance against the Code Sigils blog.
- [x] Record the observed Zensical version, commands, configuration, and output
  path.
- [x] Exercise tabs, navigation, internal links, media, video embeds,
  presentation customization, and accessibility review.
- [x] Perform one authorized light edit in an isolated branch.
- [x] Define bounded scenarios for the observed tab-rendering and
  accessibility-invocation failures ([scenarios.md](scenarios.md)).
- [x] Add a pinned fixture and isolated runner for the two observed failures;
  keep broader fixtures deferred until another deterministic gap appears.
- [x] Add a bounded non-root deployment-link fixture based on the blog's
  `/docs/` boundary.
- [x] Strengthen fixture assertions for non-empty tab panels, positive iframe
  titles, and nested base-path navigation.

**Exit condition:** an agent can inspect an existing site, make an authorized
light edit or report a review finding, and validate the result without
inventing site conventions. The workflow must also satisfy the quality
criteria in [vision.md](vision.md): precise routing, evidence, authorization,
minimal scope, rendered confidence, and an honest handoff.

## Phase 2 — Component and content-model confidence (substantially proven)

- [x] Verify target-used admonitions, content tabs, front matter, navigation,
  base paths, images, local assets, embeds, responsive CSS, landing-page
  behavior, and static accessibility signals against current Zensical sources
  and the Code Sigils blog.
- [x] Record optional GLightbox behavior without enabling it or claiming
  interaction coverage where the acceptance target does not use it.
- [x] Add focused references only for behavior that changes agent decisions.

**Exit condition:** a target-used component can be inspected, changed only with
authorization, and checked in rendered output without importing another site's
conventions. Browser interaction, assistive technology, remote-player,
captions/transcripts, and deployment outcomes remain separate manual checks;
add another fixture only when a real-site run exposes a deterministic gap.

## Phase 3 — Release and maintenance evidence

- [x] Add a version-pinned source registry entry and validation runner when the
  workflow has stable observable behavior.
- [x] Add discovery scenarios for matching and non-matching prompts.
- [x] Define a project-scoped installation smoke check before public release.
- [x] Compare the downloaded `layeredcraft/zensical-site` references and
  templates for useful authoring patterns (voice/tone, content types,
  front-matter, and configuration caveats); admit only capabilities that meet
  the evidence-gated rule above.
- [x] Add a discovery regression scenario: run a broad Skills CLI query such as
  `npx --yes skills find zensical`, preserve the provider timestamp/result count,
  and compare its candidates with direct repository and documented catalog
  searches. Treat `skills find` as a retrieval signal, not proof of quality or
  complete indexing. Evidence is recorded in `docs/research.md`; the query
  returned related candidates but did not surface this repository.
- [x] Update the skill-discovery workflow to search Skills.sh after local and
  documented catalog sources, while recording unavailable, stale, or
  unauthenticated sources instead of interpreting absence as proof.

Keep release verification bounded to Codex, OpenCode, and Hermes. Run one
shared local validation suite, then one small installation/discoverability
check per host from an isolated temporary directory. Do not create a separate
CI workflow for each host or copy the skill into host-specific directories.

## Deferred

- Full theme authoring or generic frontend work.
- Broad plugin or JavaScript guidance.
- Deployment automation.
- A large fixture suite before the first workflow proves what needs testing.
- Support and CI matrices for agents outside Codex, OpenCode, and Hermes.

## Independent capability boundary

Zensical's wider built-in surface is documented independently from Zola. Do
not expand the runtime router just because a feature exists. Add a focused
capability only when the blog or another accepted target supplies a concrete
workflow, current primary-source evidence, a bounded behavior scenario, and a
maintenance owner. Candidate future slices include navigation feature
interactions, MkDocs compatibility, workspace watch/symlink behavior, and theme
customization; each remains deferred until real work requires it.

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

## Phase 1 — Existing-site review and light editing

- Test `SKILL.md`, `light-edit.md`, `editorial-review.md`,
  `content-components.md`, and `validation.md` against the Code Sigils blog.
- Record observed Zensical version, commands, configuration, and output path.
- Add a small fixture or scenario only if a repeated failure or ambiguity needs
  reproducible validation.

**Exit condition:** an agent can inspect an existing site, make an authorized
light edit or report a review finding, and validate the result without
inventing site conventions. The workflow must also satisfy the quality
criteria in [vision.md](vision.md): precise routing, evidence, authorization,
minimal scope, rendered confidence, and an honest handoff.

## Phase 2 — Component and content-model confidence

- Verify admonitions, content tabs, front matter, navigation, base paths, and
  asset links against current Zensical sources and a real repository.
- Add focused references only for behavior that changes agent decisions.

## Phase 3 — Release and maintenance evidence

- Add a version-pinned source registry entry and validation runner when the
  workflow has stable observable behavior.
- Add discovery scenarios for matching and non-matching prompts.
- Define a project-scoped installation smoke check before public release.

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

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

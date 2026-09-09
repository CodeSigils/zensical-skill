# Zensical skill vision

## Purpose

`zensical` is a focused Agent Skill for inspecting, lightly editing, reviewing,
and validating Zensical static sites. It helps an agent preserve an existing
site's conventions while using Zensical components such as admonitions and
content tabs, media assets, and the site's presentation customization safely.

## Boundaries

The skill owns repository inspection, presentation syntax, content/navigation
consistency, link and front-matter checks, builds, rendered-output inspection,
media and asset behavior, CSS/theme customization, landing pages, and bounded
deployment awareness.

It does not own prose craft, blog voice, SEO strategy, generic frontend work,
autonomous publishing, or every Zensical feature. Those capabilities remain
composable skills or repository-specific guidance.

## Principles

- Inspect the target repository before assuming its layout or commands.
- Keep light edits, article review, site modification, and publishing separate.
- Preserve one canonical source and detect duplicate or drifting guidance.
- Centralize repeated semantic configuration values when they should change
  together, while keeping illustrative examples readable.
- Treat local build success and remote deployment success as different evidence.
- Prefer current primary sources and record version uncertainty.
- Extract new workflows only after repeated work demonstrates a stable need.

## Quality criteria

A workflow is ready to keep when it demonstrates all of the following:

- **Precise routing:** the skill matches concrete Zensical work and does not
  attract generic writing, frontend, CMS, or publishing requests.
- **Evidence first:** it inspects the target repository and consults a current
  primary source for version-sensitive behavior.
- **Authorization fidelity:** it distinguishes light edits, review-only work,
  site modification, and publishing; it does not mutate beyond the request.
- **Source-of-truth discipline:** it preserves the observed content model,
  navigation, configuration, and output conventions without duplicating them.
- **Minimal coherent change:** an authorized repair changes only the affected
  scope and keeps unrelated architecture intact.
- **Rendered confidence:** validation covers the build and, where feasible, the
  affected rendered page, including links, admonitions, tabs, media assets,
  embeds, CSS/theme overrides, landing-page behavior, and base paths.
  Accessibility evidence must distinguish static inspection from browser or
  assistive-technology testing.
- Accessibility can support discoverability and reader usability, but remains
  distinct from SEO strategy and ranking claims.
- **Honest handoff:** the agent reports exact checks, remaining uncertainty,
  deployment limits, and any human decision still required.
- **Maintainability:** references remain discoverable, source dates or versions
  are recorded when volatile, and repeated guidance does not drift across files.

These criteria are acceptance questions, not a numeric score. A workflow may
need additional domain or presentation checks, but it should not claim broader
coverage than its evidence supports.

## Current status

The initial runtime payload is a reviewable narrow slice. It has not yet been
installed or published as a public skill, and no workflow fixture suite exists.

## Compatibility strategy

The maintained host matrix is intentionally limited to the environments we use:

- **Codex:** project-scoped Agent Skills installation.
- **OpenCode:** its documented local or external skill-directory mechanism.
- **Hermes:** its documented external skill-directory mechanism.

The source of truth remains one `zensical/` payload. Do not maintain host-
specific copies, host-specific instructions in the runtime skill, or a matrix
for agents we do not use. Host smoke checks should confirm discoverability and
referenced-file availability; they should not duplicate the workflow tests.

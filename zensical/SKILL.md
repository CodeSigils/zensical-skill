---
name: zensical
description: "Review, lightly edit, and validate existing Zensical static sites: inspect their configuration and content model, check Markdown components, links, accessibility, media, builds, and bounded deployment concerns. Use for concrete Zensical repository work; not for generic prose writing, frontend development, or autonomous publishing."
license: MIT
metadata:
  short-description: "Maintain Zensical sites safely"
  compatibility: "Requires filesystem and shell access; Zensical is required for build validation; network is needed only for current documentation and external-link checks."
  keywords:
    - zensical
    - static-site-generator
    - markdown
    - documentation-site
    - site-maintenance
    - content-tabs
    - admonitions
    - accessibility
    - link-validation
    - agent-skills
  repository: "CodeSigils/zensical-skill"
  maintainers:
    - CodeSigils
---

# Zensical

Use this skill for a concrete task in an existing or explicitly requested
Zensical site. It is a presentation and site-maintenance skill, not a writing
voice, SEO, generic frontend, or autonomous publishing skill.

Never impose conventions from the Code Sigils acceptance blog or any other
test site on a target repository. The target site's own configuration, content
model, and editorial rules are authoritative; project-specific observations in
the source registry are evidence only.

## Operating boundaries

- Inspect the repository before assuming its content layout, navigation,
  configuration, theme, output directory, or deployment workflow.
- Preserve the site's conventions and source-of-truth locations. Do not create
  parallel configuration or duplicate navigation entries.
- Notice repeated semantic values in site configuration, CI, scripts, and
  repository Python as possible duplication or drift smells. Recommend
  centralization only when the values should change together and the benefit
  outweighs the loss of local clarity; do not mechanically extract examples or
  prose.
- Separate editorial intent from presentation implementation. The article or
  review process decides whether a tip, warning, or tab is useful; this skill
  implements and validates the Zensical syntax.
- Make bounded changes authorized by the user. Do not publish, change hosting,
  or install third-party integrations unless requested.
- Before an authorized commit, publish, or deployment change, run the bounded
  tracked-file hygiene check when the target is a Git repository. Treat a
  finding as a stop-and-review signal: do not print its value, rotate or remove
  credentials, rewrite history, or bypass provider protection without explicit
  user authorization.
- Treat package versions, CLI commands, supported components, and theme
  behavior as release-dependent. Consult [references/source-registry.md](references/source-registry.md)
  and current upstream documentation when a claim depends on a version.
- Use web research deliberately for broad site concerns, but give sources a
  clear order: inspect the target repository, consult current official
  Zensical documentation first for Zensical behavior, then use authoritative
  standards (such as W3C) and reputable community or provider sources for
  accessibility, design, embeds, and context. Never replace an official
  Zensical answer with a cached blog or generic static-site advice.

## Route the request

Choose the smallest applicable workflow:

- **Inspect or orient:** read [references/site-inspection.md](references/site-inspection.md).
- **Lightly edit or author Markdown:** read [references/light-edit.md](references/light-edit.md)
  and [references/content-components.md](references/content-components.md), then
  preserve the article's own editorial rules.
- **Review media or assets:** read [references/media.md](references/media.md),
  then inspect the target's image, video, audio, embed, and asset conventions.
- **Review responsive presentation or customization:** read
  [references/customization.md](references/customization.md), then inspect
  `extra_css`, `extra_javascript`, `custom_dir`, theme settings, and landing
  page conventions.
- **Review accessibility:** read [references/accessibility.md](references/accessibility.md)
  whenever content, media, components, CSS, templates, or landing pages affect
  names, alternatives, keyboard use, contrast, zoom, or motion.
- **Review article quality:** read [references/editorial-review.md](references/editorial-review.md)
  and use its evidence-based finding format.
- **Review admonitions, tabs, links, or navigation:** read
  [references/content-components.md](references/content-components.md).
- **Review search behavior or exclusions:** inspect the target's native search
  configuration and current source-registry entry before proposing an external
  search service.
- **Build, render, or check a change:** read
  [references/validation.md](references/validation.md).
- **Diagnose a failure:** inspect the supplied error and repository commands
  first; consult the relevant reference only after identifying the failing
  layer.

## Default workflow

1. Confirm the requested outcome and whether the task is review-only or allows
   edits.
2. Inspect `pyproject.toml`, `zensical.toml`, `mkdocs.yml` if present,
   `docs/`, navigation declarations, theme overrides, scripts, and CI files.
3. Identify the canonical source file and the narrowest affected scope.
4. Check existing conventions before adding a component, link, section, or
   configuration key.
5. Make the smallest coherent change. Keep equivalent alternatives compact
   with tabs when that improves scanning, but keep shared prerequisites and
   warnings outside the tabs.
6. Validate Markdown structure, links, navigation, and the rendered output
   using the project's own commands where available.
7. Report changed files, checks run, deployment implications, and remaining
   version-sensitive uncertainty.

For review-only work, do not modify files or claim that a recommendation was
implemented. Tie every finding to repository evidence and distinguish a broken
site from a bounded maintainability or editorial concern.

## Authorization modes

Keep these modes distinct:

- **Light edit:** make a small requested wording, Markdown, front-matter, link,
  admonition, or tab change. Preserve the page's voice, route, metadata shape,
  and surrounding structure. Do not silently turn it into a rewrite.
- **Article-quality review:** inspect flow, reader promise, evidence, jargon,
  links, scope, and durability; report bounded findings. Do not edit unless the
  user authorizes a revision.
- **Site modification:** change navigation, configuration, assets, or templates
  only within the explicitly requested scope.
- **Publish or deploy:** never infer authorization from a successful build.
  Treat commit, push, hosting, and deployment as separate actions.

## Components that commonly need care

- Use admonitions as visible signposts for safety, comprehension, memory, or
  optional detail; do not box ordinary prose.
- Use content tabs for genuinely parallel alternatives such as npm, pnpm, Yarn,
  Python, or platform-specific commands. Do not hide material differences or
  warnings in a tab.
- Prefer descriptive links and one canonical navigation entry. Search for an
  existing page before creating a new one.
- Keep front matter and section metadata consistent with the site's existing
  conventions. Do not invent fields because another static-site generator uses
  them.
- Treat images, video, audio, and external embeds as separate media concerns.
  A passing build proves neither player behavior nor remote availability.
- Treat CSS overrides, custom templates, and landing pages as version-sensitive
  presentation layers. Preserve scoped changes and validate rendered behavior.
- Treat accessibility as a cross-cutting quality concern. Prefer native HTML
  and visible text before ARIA, and never claim WCAG compliance from a build
  alone.

## Handoff

For a review, report findings with file paths and concrete evidence before
proposing fixes. For an edit, report the focused change and validation. If a
source, command, link, or rendering behavior could have drifted, say exactly
what was verified and what still needs a maintainer's review.

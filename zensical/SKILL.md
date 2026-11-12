---
name: zensical
description: "Maintain, review, and validate Zensical sites and their source Markdown. Use for Zensical content, components, configuration, accessibility, and target-guided article revisions; exclude generic writing, SEO, frontend work, and autonomous publishing."
license: MIT
metadata:
  compatibility: "Requires filesystem and shell access; bundled checks require Python 3.10+ and Bash; Zensical is required for build validation; network is needed only for current documentation and external-link checks."
  short-description: "Maintain Zensical sites and source content"
  keywords: "zensical, static-site-generator, markdown, documentation-site, site-maintenance, content-components, accessibility"
  repository: "CodeSigils/zensical-skill"
  maintainers: "CodeSigils"
---

# Zensical

Use this skill for a concrete task in an existing or explicitly requested
Zensical site. It covers site maintenance and source-content work governed by
the target repository. It is not a generic writing voice, SEO, frontend, or
autonomous-publishing skill.

Never impose conventions from the Code Sigils acceptance blog or any other
test site on a target repository. The target site's own configuration, content
model, and editorial rules are authoritative; project-specific observations in
the source registry are evidence only.

## Core boundaries

- Inspect the target before assuming its layout, configuration, navigation,
  theme, output, or deployment workflow. Preserve its source-of-truth files;
  do not create parallel configuration or duplicate navigation.
- For version-sensitive Zensical behavior, consult
  [references/source-registry.md](references/source-registry.md) and current
  official documentation before recommending a change. Report a bounded
  finding rather than claiming browser, provider, deployment, or WCAG coverage
  that was not performed.
- For article work, the target's editorial rules decide voice and argument.
  This skill supplies review mechanics and Zensical-aware validation; it never
  invents author experience or imposes a house style.
- Keep publishing, hosting, third-party integrations, and Git delivery as
  separate authorization decisions. Before an authorized commit, publish, or
  deployment action in a Git repository, run the tracked-file hygiene check
  and stop for review on a finding.
- Treat local identifiers as potentially personal in publishable material. Use
  accurate neutral placeholders unless disclosure is necessary and authorized.

## Route the request

Choose the smallest applicable workflow:

- **Inspect or orient:** read [references/site-inspection.md](references/site-inspection.md).
- **Draft, revise, or review substantive article prose:** read
  [references/article-review.md](references/article-review.md) before changing
  it. Use the target's editorial guidance; this is a planning and review aid,
  not a house style or publication gate.
- **Make a light Markdown edit:** read
  [references/light-edit.md](references/light-edit.md). Read
  [references/content-components.md](references/content-components.md) only if
  the edit affects an admonition, tab, link, or navigation.
- **Review media or assets:** read [references/media.md](references/media.md),
  then inspect the target's image, video, audio, embed, and asset conventions.
- **Review admonitions, tabs, links, or navigation:** read
  [references/content-components.md](references/content-components.md).
- **Review responsive presentation or customization:** read
  [references/customization.md](references/customization.md), then inspect
  `extra_css`, `extra_javascript`, `custom_dir`, theme settings, and landing
  page conventions.
- **Review accessibility:** read [references/accessibility.md](references/accessibility.md)
  whenever content, media, components, CSS, templates, or landing pages affect
  names, alternatives, keyboard use, contrast, zoom, or motion.
- **Review or enable feeds (RSS, JSON Feed):** read
  [references/rss.md](references/rss.md). Feeds are ordinary component work
  once the target runs a Zensical version that supports them natively; they are
  not a third-party integration.
- **Review search behavior or exclusions:** inspect the target's native search
  configuration and current source-registry entry before proposing an external
  search service.
- **Review release output, sitemap, or canonical URLs:** read
  [references/validation.md](references/validation.md), inspect the configured
  `site_url`, and distinguish generated-output integrity from indexing or
  deployment success.
- **Build, render, or check a change:** read
  [references/validation.md](references/validation.md).
- **Upgrade to a newer Zensical version:** read
  [references/migration.md](references/migration.md), then recheck the
  release-channel row in
  [references/source-registry.md](references/source-registry.md).
- **Diagnose a failure:** inspect the supplied error and repository commands
  first; consult the relevant reference only after identifying the failing
  layer.

## Proportionate workflow

1. Confirm the outcome and whether the task permits edits.
2. Inspect only the configuration, source, and conventions needed for the
   requested scope; identify the canonical file.
3. Read the smallest routed reference, make the smallest coherent change, and
   validate the affected surface with the target's own commands.
4. For review-only work, report evidence and recommendations without editing.
   For an edit, report changed files, checks, and any remaining uncertainty.

A light edit must remain a light edit. A site modification may change
configuration, navigation, assets, or templates only within the requested
scope. A successful build never authorizes commit, push, hosting, or deploy.

## Handoff

For a review, report findings with file paths and concrete evidence before
proposing fixes. For an edit, report the focused change and validation. State
exactly what was verified and what still needs maintainer review. Do not run a
skill self-update command; if this copy may be stale, explain that the user can
choose to refresh it.

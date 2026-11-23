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
- For version-sensitive Zensical behavior, or when a task depends on an
  external primary source, consult the matching row in
  [references/source-registry.md](references/source-registry.md) at the point
  of use and confirm current official documentation before recommending a
  change. Treat external URLs and reviewed dates as time-sensitive evidence:
  recheck volatile or release-channel entries, report when a source cannot be
  verified or network access is unavailable, and do not cache snippets as
  current fact. Report a bounded finding rather than claiming browser,
  provider, deployment, or WCAG coverage that was not performed.
- For article work, the target's editorial rules decide voice and argument.
  This skill supplies review mechanics and Zensical-aware validation; it never
  invents author experience or imposes a house style.
- Keep publishing, hosting, third-party integrations, and Git delivery as
  separate authorization decisions. Before an authorized commit, publish, or
  deployment action in a Git repository, run the tracked-file hygiene check
  and stop for review on a finding.
- Treat local identifiers as potentially personal in publishable material. Use
  accurate neutral placeholders unless disclosure is necessary and authorized.

## Shared target-first method

Start every Zensical maintenance decision with this order:

1. **Establish scope and authority.** Identify the target repository, requested
   outcome, and whether the task permits review or edits. Preserve existing
   work and keep commit, publish, and deployment authority separate.
2. **Perform a bounded target scan.** Read local instructions and inspect only
   the relevant configuration, canonical source files, existing conventions,
   and target commands. Record unavailable evidence as uncertainty rather than
   importing assumptions from another site.
3. **Frame one affected outcome.** Identify the canonical source and the
   rendered or source surface that must remain correct. Do not turn one request
   into a site-wide audit or activate unrelated references.
4. **Reuse target records, then apply one conditional reference.** Use the
   target's own configuration, editorial guidance, maintenance records, and
   prior evidence before selecting the smallest routed reference below. A
   reference adds its topic-specific delta; it does not replace this method.
5. **Make or recommend the smallest coherent change, then validate and hand
   off.** Run target-appropriate checks within the validation boundary: a build verifies generation, rendered inspection verifies affected presentation, and neither verifies deployment or indexing. Report remaining limits.

## Route the request

Load only the smallest reference set that matches the task. References are
opt-in detail, not background context.

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
  [references/customization.md](references/customization.md) only when CSS,
  templates, theme settings, or landing pages are in scope, then inspect the
  target's `extra_css`, `extra_javascript`, `custom_dir`, and theme settings.
- **Review accessibility:** read [references/accessibility.md](references/accessibility.md)
  only when content, media, components, CSS, templates, or landing pages affect
  names, alternatives, keyboard use, contrast, zoom, or motion.
- **Review or enable feeds (RSS, JSON Feed):** read
  [references/rss.md](references/rss.md) when feed behavior is in scope. Feeds
  are ordinary component work once the target runs a Zensical version that
  supports them natively; they are not a third-party integration.
- **Review search behavior or exclusions:** inspect the target's native search
  configuration first; consult the search row in
  [references/source-registry.md](references/source-registry.md) at point of
  use only if current behavior, exclusions, or version details matter.
- **Review release output, sitemap, or canonical URLs:** read
  [references/validation.md](references/validation.md), inspect the configured
  `site_url`, and distinguish generated-output integrity from indexing or
  deployment success.
- **Build, render, or check a change:** read
  [references/validation.md](references/validation.md).
- **Upgrade to a newer Zensical version:** read
  [references/migration.md](references/migration.md), then recheck the
  release-channel row in
  [references/source-registry.md](references/source-registry.md) before relying
  on version-sensitive behavior.
- **Diagnose a failure:** inspect the supplied error and repository commands
  first; consult only the reference that matches the failing layer.

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

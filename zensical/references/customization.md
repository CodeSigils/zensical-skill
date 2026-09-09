# CSS, themes, and landing pages

Read this reference when a task changes responsive presentation, custom CSS,
theme templates, icons, JavaScript, or a homepage/landing page. This skill
preserves and validates the site's presentation system; it does not choose a
brand, write generic frontend applications, or replace editorial direction.

## Responsive presentation

- Inspect existing selectors and wrappers before adding CSS. Prefer a small,
  scoped override in the repository's configured `extra_css` file over editing
  generated output or copying the whole theme.
- For images, preserve intrinsic proportions (`max-width: 100%` and automatic
  height unless the design has a documented reason otherwise). Check narrow
  viewport behavior and captions, not only desktop screenshots.
- For video and embeds, use a responsive wrapper or `aspect-ratio`, constrain
  width to the content column, and preserve keyboard access and fallback text.
  Confirm that provider-specific selectors do not accidentally style unrelated
  iframes.
- Test light and dark palettes, reduced-width layouts, and content with long
  titles or captions when the override affects shared components.

## CSS and JavaScript overrides

Use `extra_css` and `extra_javascript` for additive site behavior when they are
already part of the repository's convention. Keep selectors scoped and avoid
depending on unstable generated class names where possible. For a script,
consider consent, offline use, loading order, and whether it breaks instant
navigation.

Record the source file, affected selectors, and validation page in the handoff.
Do not silently introduce a framework, CDN, analytics, or third-party player.

## Custom theme and templates

Inspect `custom_dir` before changing templates. Zensical uses MiniJinja and
supports page-selected templates through front matter. Prefer extending
`main.html` and overriding a focused block with `{{ super() }}` when adding
content; replacing `base.html` or a full partial creates more upgrade drift.
Treat custom templates as version-sensitive and compare them with the target
Zensical release before editing.

## Landing pages

Treat `docs/index.md` as both content and presentation. Check its front matter,
title/description, hero or introductory structure, navigation visibility,
responsive media, calls to action, and links to canonical sections. A custom
homepage template can be appropriate for a true landing page, but should be
explicitly selected in front matter and remain separate from ordinary article
templates.

## Validation boundary

Build output can confirm that CSS, templates, and assets were emitted. It
cannot prove responsive layout, keyboard behavior, palette contrast, or
third-party embeds. Use a rendered browser inspection for those claims and
report any viewport or interaction coverage honestly.

For the cross-cutting accessibility review, continue with
[accessibility.md](accessibility.md).

Sources: [Zensical customization](https://zensical.org/docs/customization/),
[front matter](https://zensical.org/docs/authoring/frontmatter/), and
[colors](https://zensical.org/docs/setup/colors/).

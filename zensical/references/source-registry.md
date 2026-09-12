# Source registry

Keep version-sensitive facts tied to current primary sources. Update this
registry when the skill is tested against a new Zensical release or when an
upstream route changes.

| Topic | Primary source | Verified version/date | What to verify and caveat |
| --- | --- | --- | --- |
| Zensical documentation | [zensical.org/docs](https://zensical.org/docs/) | Checked 2026-09-10; the documentation site does not state one global release version | Configuration, Markdown extensions, navigation, and release behavior; use the target lockfile or installed version for version-sensitive syntax, then recheck the current docs. |
| Admonitions | [authoring/admonitions](https://zensical.org/docs/authoring/admonitions/) | Checked 2026-09-09; site uses 0.0.60 | Supported callout types, nesting, collapsible details, and configuration; confirm against the target version. |
| Content tabs | [authoring/content-tabs](https://zensical.org/docs/authoring/content-tabs/) | Checked 2026-09-09; site uses 0.0.60 | Tab syntax, nested content, anchors, and linked tabs; labels link by title rather than position. |
| Code-block line anchors | [authoring/code-blocks](https://zensical.org/docs/authoring/code-blocks/) | Checked 2026-09-11; Code Sigils uses 0.0.60 | The upstream example enables `pymdownx.highlight.anchor_linenums`. Browser inspection found 202 empty, zero-width, focusable anchors in one rendered guide. Test target output before keeping or disabling it; replacing the extension table requires preserving all required defaults. |
| Images, captions, formats, and performance | [authoring/images](https://zensical.org/docs/authoring/images/), [MDN `<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img), [MDN responsive images](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images), and [MDN image formats](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Image_types) | Checked 2026-09-12 | Alignment, captions, lazy loading, intrinsic dimensions, fetch priority, responsive variants, SVG/WebP/AVIF/PNG/JPEG decisions, and image-path behavior; verify enabled extensions, target browser support, the target's optimization pipeline, and rendered output. |
| Image lightbox | [setup/extensions/glightbox](https://zensical.org/docs/setup/extensions/glightbox/) | Checked 2026-09-09 | Optional GLightbox extension, galleries, captions, exclusions, and themed images; do not infer gallery behavior from a build alone. |
| Customization and templates | [customization](https://zensical.org/docs/customization/) | Checked 2026-09-09; acceptance observation: Code Sigils blog uses `extra_css` | Additional CSS/JavaScript, `custom_dir`, MiniJinja templates, focused block overrides, and custom page templates; compare against the installed release before editing. |
| Front matter and landing pages | [authoring/frontmatter](https://zensical.org/docs/authoring/frontmatter/) | Checked 2026-09-09; acceptance observation: Code Sigils blog uses `docs/index.md` | Page-selected templates, metadata, hidden elements, and homepage conventions; inspect the site's actual landing-page source. |
| Colors and responsive palette | [setup/colors](https://zensical.org/docs/setup/colors/) | Checked 2026-09-09 | Palette variables and light/dark schemes; rendered contrast and narrow viewport behavior still require inspection. |
| Accessibility baseline | [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [W3C Images](https://www.w3.org/WAI/tutorials/images/), and [W3C Audio/Video](https://www.w3.org/WAI/media/av/) | Checked 2026-09-09 | Text alternatives, accessible names, captions, transcripts, keyboard and visual checks; this is a review baseline, not a Zensical compliance guarantee. |
| New-tab link security and privacy | [MDN `noopener`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/noopener) and [MDN `rel`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel) | Checked 2026-09-11 | Modern `target="_blank"` has implicit `noopener` behavior. Explicit `noopener` can remain a project convention; `noreferrer` also removes the HTTP referrer, so use it only for an intentional privacy/attribution policy. |
| Sensitive-material response | [GitHub secret scanning](https://docs.github.com/en/code-security/concepts/secret-security/secret-scanning) and [sensitive-data removal](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository) | Checked 2026-09-09 | A bounded tracked-file preflight can flag candidates but cannot prove absence. For a real exposure, rotate or revoke first; history rewriting requires explicit authorization and coordination. |
| Markdown compatibility | [authoring/markdown](https://zensical.org/docs/authoring/markdown/) | Checked 2026-09-09 | Python-Markdown compatibility and four-space indentation requirements; do not assume another Markdown renderer behaves the same way. |
| Navigation | [setup/navigation](https://zensical.org/docs/setup/navigation/) | Checked 2026-09-09 | Implicit folder navigation versus explicit configuration and navigation features. |
| Zensical project | [zensical.org](https://zensical.org/) | Checked 2026-09-10; describes an open-source technical-writing system built by the creators of Material for MkDocs | Current project identity and supported installation paths; obtain commands and versions from current documentation and the target lockfile rather than cached examples. |
| Project configuration | Repository's declared config and lockfile | Per target repository | Installed version, commands, output path, and local conventions; local evidence wins over generic examples. |
| Deployment | Repository workflow and hosting documentation | Per target repository | Trigger paths, build command, artifact, and deployment boundary; a local build does not prove deployment. |
| Site search / Disco | [setup/search](https://zensical.org/docs/setup/search/) and [Zensical roadmap](https://zensical.org/about/roadmap/) | Checked 2026-09-09; site uses 0.0.60 | Native client-side search is enabled by default and supports offline use; inspect `search.exclude` and search features before recommending a third-party service. The engine is evolving and its interface is currently English-only even though multilingual search is supported. |
| Analytics and privacy | [site analytics](https://zensical.org/docs/setup/analytics/) and [data privacy](https://zensical.org/docs/setup/data-privacy/) | Checked 2026-09-11 | Zensical supports GA4 and consent controls, but describes analytics as under overhaul. Do not add tracking without a stated measurement need, authorization, and an appropriate privacy review. |
| Search discoverability | [Google developer SEO guide](https://developers.google.com/search/docs/fundamentals/get-started-developers) and [sitemap guidance](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap) | Checked 2026-09-11 | Descriptive HTML, titles, metadata, links, canonical URLs, and sitemaps support discovery. A sitemap helps crawling but does not guarantee indexing or ranking; this is opt-in advice, not an SEO workflow. |

When network access is unavailable, distinguish repository evidence from memory
and do not present an unverified command as current. Record the review date in a
project's release or verification notes when the detail is volatile.

## Research order

For a live task, inspect the target repository first. For Zensical syntax,
configuration, theme, navigation, Markdown, or CLI behavior, check the current
official Zensical documentation and source registry before broad web search.
Use standards bodies and primary provider documentation for accessibility,
media, privacy, or embed claims, and use community material only for clearly
labelled observations or alternatives. Cached posts and search snippets are
leads, not evidence.

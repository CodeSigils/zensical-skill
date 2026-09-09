# Source registry

Keep version-sensitive facts tied to current primary sources. Update this
registry when the skill is tested against a new Zensical release or when an
upstream route changes.

| Topic | Primary source | Verified version/date | What to verify and caveat |
| --- | --- | --- | --- |
| Zensical documentation | [zensical.org/docs](https://zensical.org/docs/) | Not pinned yet | Configuration, Markdown extensions, navigation, and release behavior; recheck before relying on version-sensitive syntax. |
| Admonitions | [authoring/admonitions](https://zensical.org/docs/authoring/admonitions/) | Checked 2026-09-09; site uses 0.0.60 | Supported callout types, nesting, collapsible details, and configuration; confirm against the target version. |
| Content tabs | [authoring/content-tabs](https://zensical.org/docs/authoring/content-tabs/) | Checked 2026-09-09; site uses 0.0.60 | Tab syntax, nested content, anchors, and linked tabs; labels link by title rather than position. |
| Images and captions | [authoring/images](https://zensical.org/docs/authoring/images/) | Checked 2026-09-09 | Alignment, captions, lazy loading, light/dark variants, and image-path behavior; verify enabled extensions and rendered output. |
| Image lightbox | [setup/extensions/glightbox](https://zensical.org/docs/setup/extensions/glightbox/) | Checked 2026-09-09 | Optional GLightbox extension, galleries, captions, exclusions, and themed images; do not infer gallery behavior from a build alone. |
| Customization and templates | [customization](https://zensical.org/docs/customization/) | Checked 2026-09-09; blog uses `extra_css` | Additional CSS/JavaScript, `custom_dir`, MiniJinja templates, focused block overrides, and custom page templates; compare against the installed release before editing. |
| Front matter and landing pages | [authoring/frontmatter](https://zensical.org/docs/authoring/frontmatter/) | Checked 2026-09-09; blog uses `docs/index.md` | Page-selected templates, metadata, hidden elements, and homepage conventions; inspect the site's actual landing-page source. |
| Colors and responsive palette | [setup/colors](https://zensical.org/docs/setup/colors/) | Checked 2026-09-09 | Palette variables and light/dark schemes; rendered contrast and narrow viewport behavior still require inspection. |
| Accessibility baseline | [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [W3C Images](https://www.w3.org/WAI/tutorials/images/), and [W3C Audio/Video](https://www.w3.org/WAI/media/av/) | Checked 2026-09-09 | Text alternatives, accessible names, captions, transcripts, keyboard and visual checks; this is a review baseline, not a Zensical compliance guarantee. |
| Markdown compatibility | [authoring/markdown](https://zensical.org/docs/authoring/markdown/) | Checked 2026-09-09 | Python-Markdown compatibility and four-space indentation requirements; do not assume another Markdown renderer behaves the same way. |
| Navigation | [setup/navigation](https://zensical.org/docs/setup/navigation/) | Checked 2026-09-09 | Implicit folder navigation versus explicit configuration and navigation features. |
| Zensical project | [zensical.org](https://zensical.org/) | Not pinned yet | Current project identity and supported installation paths; do not copy cached commands. |
| Project configuration | Repository's declared config and lockfile | Per target repository | Installed version, commands, output path, and local conventions; local evidence wins over generic examples. |
| Deployment | Repository workflow and hosting documentation | Per target repository | Trigger paths, build command, artifact, and deployment boundary; a local build does not prove deployment. |
| Site search / Disco | [setup/search](https://zensical.org/docs/setup/search/) and [Zensical roadmap](https://zensical.org/about/roadmap/) | Checked 2026-09-09; site uses 0.0.60 | Native client-side search is enabled by default and supports offline use; inspect `search.exclude` and search features before recommending a third-party service. The engine is evolving and its interface is currently English-only even though multilingual search is supported. |

When network access is unavailable, distinguish repository evidence from memory
and do not present an unverified command as current. Record the review date in a
project's release or verification notes when the detail is volatile.

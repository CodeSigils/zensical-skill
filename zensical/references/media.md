# Media and assets

Read this reference when an article includes images, image galleries, video,
audio, embedded players, or a large asset collection. This is presentation and
validation guidance; editorial voice and image selection remain separate
concerns.

## Images

- Prefer local, repository-controlled assets when durability, offline use, or
  provenance matters. Resolve image paths from the source Markdown file and
  confirm the configured `docs_dir` and base path.
- When introducing externally sourced media, confirm that its licence permits
  the intended reuse and record its source, creator, and licence. Add visible
  attribution when the licence or target-site policy requires it. Do not
  download or commit media with unclear rights.
- Preserve meaningful alt text. Decorative images should have an intentional
  empty alternative rather than a filename or invented claim. Use alignment or
  captions only when they improve the page. Check the installed Markdown
  extensions before using attribute-list or caption syntax.
- If the site enables GLightbox, inspect the rendered page for the expected
  lightbox wrapper, caption, gallery grouping, and keyboard/mobile behavior.
  Do not enable it merely because images exist.
- For light/dark image pairs, verify both variants and ensure that the
  lightbox does not incorrectly combine them into one gallery.

## Performance baseline

- Whenever adding a photograph or other content raster image, inspect its
  intrinsic dimensions, byte size, likely rendered size, and target-browser
  support. When the markup is under the agent's control, provide meaningful
  `alt`, accurate `width` and `height`, and an intentional loading decision.
  Responsive CSS must preserve the intrinsic ratio rather than replacing it
  with a fixed box.
- When a modern format or responsive variants would materially reduce transfer
  size without unacceptable visual loss or compatibility cost, generate and
  inspect the delivery assets before committing them. Compare dimensions, byte
  sizes, and visible quality; commit only the needed local derivatives, not a
  full-resolution source, unless the target has an explicit archival or editing
  need. Keep a fallback only when the target's support requirements justify it.
- Do not lazy-load a likely above-the-fold or largest-contentful image. Use
  `loading="lazy"` for genuinely offscreen images, including long article
  galleries, and retain intrinsic dimensions there as well.
- Use `fetchpriority="high"` only for a confirmed primary above-the-fold image;
  do not apply it to every image or treat it as a substitute for sensible asset
  sizing. Leave ordinary images at the browser default.
- Static-site builds normally copy media rather than optimize it. Do not imply
  that Zensical resized, recompressed, generated responsive variants, or chose
  loading priority unless the target has an explicitly verified pipeline.

## Format selection

- Use SVG for suitable logos, icons, and simple diagrams that need to scale
  sharply. Do not rasterize an available, safe vector merely to follow a photo
  workflow.
- For photographic delivery derivatives, test WebP first as a broadly supported
  efficient option. Consider AVIF when it produces a material saving and the
  target's support requirements justify a tested fallback through `picture` or
  an equivalent mechanism.
- Use PNG when lossless pixels or transparency are material; use JPEG when a
  broadly compatible photographic fallback is needed. Do not keep a legacy
  raster format merely by habit, and avoid BMP or TIFF for ordinary web content.
- Choose based on observed dimensions, bytes, visual quality, and target
  support—not a format's reputation. Preserve the original format when a
  conversion has no demonstrated delivery benefit.

## Video and audio

Zensical has documented first-class image features, but no equivalent native
video or audio authoring component in the current reference set. Sites commonly
use raw HTML such as `<video>`, `<audio>`, or an external-provider `<iframe>`.
Treat these as HTML, CSS, JavaScript, and provider integrations that require
their own validation.

- Prefer local media only when the repository can carry the files and the
  target distribution can serve them.
- For external embeds, record the provider, privacy implications, fallback
  text or link, and whether offline builds are expected to work.
- Check responsive dimensions, keyboard access, captions/subtitles, poster
  images, a descriptive `title` on iframes, and whether the embed depends on
  third-party JavaScript.
- For raw HTML media, use native elements where they express the content:
  verify meaningful controls and, for prerecorded spoken video, a captions
  track or documented provider captions plus a transcript or equivalent where
  the content needs one. Treat autoplay, muted playback, and looping as
  reader-impacting choices, not harmless defaults. Do not prescribe `sandbox`,
  `referrerpolicy`, or provider-specific attributes without checking that they
  preserve the target embed's intended behavior and the site's privacy policy.
- Do not claim that a successful build proves that a player loads or that an
  external URL is available.

## Asset and base-path checks

After building, inspect the generated HTML and output tree:

1. every local image, video, audio, poster, stylesheet, and script target
   exists in the output;
2. relative and root-absolute URLs behave correctly for the configured
   `site_url`, `use_directory_urls`, and any deployment subpath;
3. changed content images retain correct `alt`, intrinsic dimensions, and a
   suitable loading decision in generated HTML; inspect `srcset`/`sizes` when
   variants are supplied;
4. remote embeds are clearly distinguishable from local assets; and
5. large media does not enter the repository without an explicit size,
   licensing, and maintenance decision.

Use a browser or equivalent rendered inspection for layout and interaction.
For an affected lead image or media-heavy page, use browser network or
performance evidence when available to check that lazy loading and priority
choices behave as intended. Static link checks cannot prove image dimensions,
player behavior, captions, lightbox operation, or real loading priority.

For names, alternatives, captions, transcripts, keyboard behavior, and visual
presentation, continue with [accessibility.md](accessibility.md).

## Sources

Consult the current [Zensical images documentation](https://zensical.org/docs/authoring/images/),
[MDN image element reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img),
[MDN responsive-images guide](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images),
[MDN image format guide](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Image_types),
and [GLightbox documentation](https://zensical.org/docs/setup/extensions/glightbox/)
for version-sensitive syntax. The target repository and its lockfile remain the
source of truth for enabled extensions, asset conventions, and any optimization
pipeline.

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
  empty alternative rather than a filename or invented claim.
- Use width, alignment, captions, and lazy loading only when they improve the
  page. Check the installed Markdown extensions before using attribute-list or
  caption syntax.
- If the site enables GLightbox, inspect the rendered page for the expected
  lightbox wrapper, caption, gallery grouping, and keyboard/mobile behavior.
  Do not enable it merely because images exist.
- For light/dark image pairs, verify both variants and ensure that the
  lightbox does not incorrectly combine them into one gallery.

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
3. remote embeds are clearly distinguishable from local assets; and
4. large media does not enter the repository without an explicit size,
   licensing, and maintenance decision.

Use a browser or equivalent rendered inspection for layout and interaction.
Static link checks cannot prove image dimensions, player behavior, captions, or
lightbox operation.

For names, alternatives, captions, transcripts, keyboard behavior, and visual
presentation, continue with [accessibility.md](accessibility.md).

## Sources

Consult the current [Zensical images documentation](https://zensical.org/docs/authoring/images/)
and [GLightbox documentation](https://zensical.org/docs/setup/extensions/glightbox/)
for version-sensitive syntax. The target repository and its lockfile remain the
source of truth for enabled extensions and asset conventions.

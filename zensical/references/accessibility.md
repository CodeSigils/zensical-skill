# Accessibility review

Read this reference for content, media, component, CSS, theme, or landing-page
work that can affect people using screen readers, keyboard navigation, zoom,
captions, high contrast, reduced motion, or other assistive technology. This is
a practical review guide, not a claim of WCAG certification.

## Prefer native meaning

- Use semantic HTML and visible text before adding ARIA. Add `aria-label` or
  `aria-labelledby` only when the control has no suitable native or visible
  accessible name.
- Keep heading order, link text, button names, lists, tables, and landmarks
  meaningful when templates or Markdown structure change.
- Do not use ARIA to hide missing content, repair invalid structure, or replace
  an image's `alt` text.

## Images and media

- Informative images need concise alt text that conveys their purpose; purely
  decorative images should use an intentional empty alternative.
- Complex diagrams, charts, and photographs may need visible captions or a
  nearby text description, not an overloaded one-line alt attribute.
- Give iframes a descriptive `title`. Provide captions for prerecorded video,
  transcripts or equivalent text alternatives where appropriate, and audio
  description when visual information is necessary to understand the video.
- Ensure local players expose controls and do not autoplay unexpected audio.
  Record external-provider limitations instead of implying that the page is
  fully accessible because it builds.

## Visual and interaction checks

When presentation changes, inspect a rendered page for sufficient contrast,
meaning that does not rely on color alone, visible keyboard focus, usable
controls, readable text at increased zoom, sensible reflow on narrow screens,
and no motion that cannot be paused or reduced. Check both configured color
schemes and representative long content when relevant.

## Zensical boundary

Zensical can emit Markdown, HTML, CSS, and theme output, but it does not
certify accessibility. The skill should report concrete markup, content, or
rendering findings with evidence and distinguish automated/static checks from
browser or assistive-technology testing.

Accessible structure, descriptive alternatives, and usable content can support
discoverability and search-result usability. Accessibility review is still an
inclusion and quality practice, not an SEO shortcut or a ranking guarantee.

Sources: [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [W3C Images Tutorial](https://www.w3.org/WAI/tutorials/images/), [W3C Audio and Video Media](https://www.w3.org/WAI/media/av/), and [W3C Accessible Names](https://www.w3.org/WAI/ARIA/apg/practices/names-and-descriptions/).

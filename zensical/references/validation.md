# Validation

Use the repository's own commands first. Do not assume that every Zensical site
uses the same package manager or output directory.

## Minimum checks

1. Run the documented build command, preferably its clean form.
2. Run the project's link or Markdown checks if available.
3. Inspect generated output for the changed page, navigation, admonitions,
   tabs, media assets, embeds, and base-path behavior. For images, verify
   rendered source paths, alt text, intrinsic dimensions, and a suitable loading
   decision; inspect `srcset`/`sizes` when variants are supplied. For
   video/audio/iframes, verify fallback, dimensions, provider boundaries,
   descriptive iframe titles, and applicable native controls or
   caption/transcript provision where feasible. For links
   that intentionally open a new tab, verify the project's `noopener` and
   referrer-policy decision rather than auto-adding `noreferrer`.
   For CSS, templates, or landing pages, inspect at least a narrow viewport and
   both configured color schemes when the change affects them.
   Apply the accessibility reference for semantic names, alt text, iframe
   titles, captions/transcripts, focus, contrast, zoom, and motion. Report
   static checks separately from browser or assistive-technology evidence.
4. Run `git diff --check` for whitespace and formatting errors.

For an authorized commit, publish, or deployment action in a Git repository,
also run the sensitive-material preflight in
[site-inspection.md](site-inspection.md). Report only candidate paths and the
check's limits; never echo a suspected credential into the handoff.

If a check requires network access, state that dependency. If the build tool is
unavailable, report the limitation and use static inspection rather than
inventing a successful result.

## Deployment boundary

A successful local build proves only that the configured site generated output.
It does not prove that hosting, DNS, permissions, cache invalidation, or a
remote workflow succeeded. Inspect CI status only when the user asks for
deployment verification or the repository workflow makes it relevant.

# Validation

Use the repository's own commands first. Do not assume that every Zensical site
uses the same package manager or output directory.

## Minimum checks

1. Run the documented build command, preferably its clean form.
2. Run the project's link or Markdown checks if available.
3. Inspect generated output for the changed page, navigation, admonitions,
   tabs, assets, and base-path behavior.
4. Run `git diff --check` for whitespace and formatting errors.

If a check requires network access, state that dependency. If the build tool is
unavailable, report the limitation and use static inspection rather than
inventing a successful result.

## Deployment boundary

A successful local build proves only that the configured site generated output.
It does not prove that hosting, DNS, permissions, cache invalidation, or a
remote workflow succeeded. Inspect CI status only when the user asks for
deployment verification or the repository workflow makes it relevant.

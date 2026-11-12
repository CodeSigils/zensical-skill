# Version migration

Use this workflow when a site or the scenario environment moves to a newer
Zensical release. A clean build is necessary and not sufficient: configuration
defaults, rendering, links, and feeds can change between releases.

## Checklist

1. Read the change before the version bump. Start with the
   [upgrade guide](https://zensical.org/docs/upgrade/) and the release notes;
   note any Python floor change, removed or renamed settings, changed
   defaults, and new plugins.
2. Check the release channel. A pre-`1.0` step such as `0.0.x` to `0.1.x`
   crosses a minor boundary and may carry breaking changes. Treat behavior
   verified on an earlier release as needing revalidation, not as current.
3. Bump the pin and refresh the lockfile. In a uv project:
   `uv lock --upgrade-package zensical==<version>`, then `uv sync`, then
   confirm with `uv pip show zensical`. Bump `tests/scenario-env` in the same
   change when the skill repository is in scope.
4. Reconcile an explicit `[project.markdown_extensions]` table against the new
   release's defaults. An explicit table **replaces** the upstream default
   table rather than extending it, so compare every configured key and record
   each deliberate difference. A missing extension here removes a feature
   without failing the build.
5. Review plugins and configuration for deprecated or renamed keys, changed
   URL handling, and new plugin defaults.
6. Run `zensical build --clean`, then compare rendered output with the
   previous build: the sitemap URL set, feed entries aside from timestamps,
   code-block rendering, and one representative page per content type. Ignore
   vendor asset hashes and generator metadata.
7. Record the result. Note the verified version and date beside the
   configuration or in the site's maintenance record, and recheck the
   release-channel row in [source-registry](source-registry.md).

## Notes

- Prefer the official upgrade guide and release notes over community migration
  posts, and cite the version a claim was checked against.
- Keep the pin, the lockfile, and the configuration reconciliation in one
  changeset so they cannot drift apart.
- When a release enters an announced beta period, say so when recommending it.

---

Reviewed 2026-11-12 against Zensical 0.1.1, from the first field migration
(Code Sigils blog, 0.0.65 to 0.1.1). Re-check the matching row in
[source-registry](source-registry.md).

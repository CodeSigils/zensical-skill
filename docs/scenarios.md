# Acceptance scenarios

These scenarios are small, real-site-derived checks for the current skill
boundary. They are maintainer procedures, not runtime instructions or a claim
of automated test coverage.

## Scenario A — Parallel package-manager tabs

**Purpose:** catch the failure where Zensical builds successfully but tab panels
are empty because equivalent alternatives were not grouped or code fences were
misnested.

**Target:** an existing article containing npm, pnpm, Yarn, or Bun commands.

1. Inspect the article's existing tab syntax and the target site's configured
   tab features.
2. Verify that equivalent alternatives form one complete tab group and that
   each panel contains a correctly nested code block.
3. Build in an isolated copy or authorized branch using the site's documented
   command.
4. Inspect the generated HTML for one complete tab group and non-empty panels.

**Pass evidence:** the build succeeds, the expected tab group is present in
   rendered output, every advertised alternative has a non-empty rendered
   panel, and the source checkout was not changed beyond the authorization.
   source checkout was not changed beyond the authorization.

## Scenario B — Accessibility review is actually invoked

**Purpose:** catch the gap where accessibility guidance exists in the skill but
   the workflow reports only build success.

**Target:** an article or landing page containing images, an iframe/video,
   custom CSS, templates, or interactive components.

1. Inspect the affected source and rendered page for headings, landmarks,
   accessible names, image alternatives, iframe titles, captions/transcripts,
   keyboard/focus concerns, contrast, zoom/reflow, and motion.
2. Record findings separately from build, link, and rendered-structure checks.
3. State which browser, keyboard, automated, or assistive-technology checks
   were not performed.
4. Do not claim WCAG conformance from static inspection or a successful build.

**Pass evidence:** the handoff contains a structured accessibility section,
   concrete paths and findings (or an explicit no-finding result), test limits,
   and any authorized remediation. The fixture runner also keeps a positive
   titled-iframe control alongside the intentional missing-title finding.

## Scenario C — Non-root deployment links

**Purpose:** catch links that appear valid locally but lose the configured
deployment subpath.

**Target:** a site whose `site_url` contains a path such as `/docs/` and whose
pages link to one another.

1. Inspect `site_url`, link style, navigation, and any base-path conventions.
2. Build an isolated copy with the site's documented command.
3. Inspect generated HTML for an internal link retaining the configured
   subpath, and verify the destination is generated.

**Pass evidence:** the generated link resolves to the destination under the
   configured deployment path, the destination exists, a nested page links back
   to home, and no root-relative assumption was introduced. Relative links are
   acceptable when the generated route and deployed base path remain correct.

## Maintenance boundary

These scenarios prove only the bounded behaviors named above, not universal
Zensical support or WCAG conformance. The pinned fixtures and runner reproduce
those observed failures and the non-root deployment boundary in isolated
temporary copies. Add another fixture or assertion only when a repeated
real-site run exposes a deterministic failure that the current scenarios cannot
represent. Keep target-site results and source versions in the research record.

The runner resolves all scenarios through the committed
`tests/scenario-env/uv.lock` with `uv --locked`; fixture directories contain
only site inputs. If dependency acquisition is unavailable, the runner reports
an environment block rather than a fixture failure. Use an already-installed
matching binary through `ZENSICAL_BIN` when offline validation is authorized.
The runner also requires `rg` with PCRE2 support for the iframe-title assertion.

Related: [roadmap](roadmap.md), [research](research.md), and the runtime
[validation reference](../zensical/references/validation.md).

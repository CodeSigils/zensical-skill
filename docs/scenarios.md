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
and any authorized remediation. The fixture runner also keeps positive titled-
iframe controls (including whitespace around `=`) alongside three intentional
missing-title findings, one of which has a misleading `data-title` attribute
and one of which has an empty `title` attribute.

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

## Scenario D — Deployment instructions match the workflow

**Purpose:** catch the failure where a repository's agent instructions describe
an obsolete dependency-installation command or omit a workflow trigger that
changes the deployed site.

**Target:** a repository with `AGENTS.md` containing a `## Deployment` section
and `.github/workflows/docs.yml` using the conventional lockfile-backed Zensical
workflow.

1. Run `python3 zensical/scripts/check_instruction_contract.py /path/to/site`.
2. When the check reports a missing path or command, compare both files and
   update the instructions only if the workflow is the source of truth.
3. Build an isolated copy with the workflow's locked command after any
   authorized correction.

**Pass evidence:** the check reports a matching documented contract, or it
explicitly skips a repository that does not use the targeted layout. It does
not validate arbitrary YAML workflows, deployment success, or host state.

## Scenario E — Code-line anchors do not become empty tab stops

**Purpose:** catch the rendered accessibility regression where highlighted code
lines emit empty, zero-width anchor links that keyboard users must tab through.

**Target:** a minimal site with Zensical's 0.0.60 Markdown-extension defaults
made explicit, `pymdownx.highlight.line_spans = "__span"`, and
`pymdownx.highlight.anchor_linenums = false`.

1. Build an isolated fixture containing a highlighted multi-line code block.
2. Inspect the rendered HTML for retained `__span-*` line spans.
3. Assert that it contains no `a[id^="__codelineno-"]` anchors.
4. Keep this separate from the iframe-title fixture: it proves a configuration
   repair, not generic accessibility conformance.

**Pass evidence:** the build succeeds, line spans remain available for code
selection, and no generated code-line anchors are emitted. Revisit the fixture
when the pinned Zensical version or its default extension set changes.

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
The runner requires Bash, `rg`, and `python3` for its shell checks and
HTML-aware iframe-title assertion. It also requires either `uv` or an exact
matching `ZENSICAL_BIN`; standard shell tools such as `awk`, `cp`, `mktemp`,
and `wc` must be available.

Related: [roadmap](roadmap.md), [research](research.md), and the runtime
[validation reference](../zensical/references/validation.md).

# RSS and JSON feeds

Use this reference when a user asks to add, enable, repair, or review feeds on
a Zensical site. Zensical generates feeds natively since 0.0.65. Treat a feed
request as ordinary component work, not a new integration.

## Check the target version first

Native feeds require Zensical 0.0.65 or later. Inspect the pinned version in the
target's `pyproject.toml`, `uv.lock`, or environment before recommending this
route. On an earlier version there is no native feed support, so say so and
describe the alternatives rather than writing configuration that will not work.

## Where the authoritative information lives

Zensical's plugin compatibility page is the primary source for availability and
for the settings it ignores:

- <https://zensical.org/docs/compatibility/mkdocs/plugins/>

Upstream does not currently publish a dedicated feeds guide, so that page plus
the installed package's own configuration parser is the practical reference.
Re-verify against the target's installed version rather than trusting a
remembered option list, because the accepted keys are validated strictly.

## Enable the plugin

The plugin is opt-in. A site without a plugin table generates no feed files.
`zensical.toml` uses a table:

```toml
[project.plugins.rss]
feed_title = "Example Site"
```

`mkdocs.yml` uses a list entry:

```yaml
plugins:
  - rss
```

Keep the change minimal. Add only settings the user asked for or that the site
demonstrably needs, and report the defaults you are relying on.

## Know what it generates

A default configuration writes five files at the site root: an RSS 2.0 feed and
a JSON Feed for newly created pages, the same pair for updated pages, and a
stylesheet that renders the RSS feed in a browser. `feeds_filenames` renames the
four feed files; a plain-name pair such as `feed.xml` and `feed-updated.xml` is
easier for readers to recognise than the generated default names.

Confirm the output by listing the built site rather than by reasoning about the
configuration. Note that the feed documents are written as a single line, so
count entries by matching each opening tag individually; a plain line count will
report one regardless of how many items the feed holds.

## Advertise the feed or it stays invisible

This is the most common way a working feed goes unnoticed. Zensical does not
emit a discovery link, so no built page points readers at the feed and feed
readers will not find it by browsing the site. Adding a theme override is what
makes it discoverable:

```html
{% extends "base.html" %}

{% block extrahead %}
  {{ super() }}
  <link rel="alternate" type="application/rss+xml" title="Example Site" href="{{ 'feed.xml' | url }}">
{% endblock %}
```

Point this at the site root, since a site deployed under a subpath needs a
root-relative path here. Use the theme's own URL filter so the link resolves
correctly from pages at any depth, and extend `main.html` with a block override
rather than replacing `base.html`. Verify afterwards that the built HTML of a
nested page contains a correctly depth-resolved `href`, not only that the root
page does.

## Dates come from Git by default

The plugin reads publication and update dates from Git history. Two consequences
matter when you advise on it:

- On a normal Git checkout, dates are real and the created and updated feeds
  differ. Nothing needs configuring.
- In a build tree with no Git history, every entry falls back to the build
  timestamp. The whole site then appears freshly published on every build, and
  the created and updated feeds become indistinguishable.

If a target builds from an exported archive, a shallow or synthetic checkout, or
a container without `.git`, raise this before enabling feeds, because no setting
repairs it. A shallow checkout is the common case rather than an edge case: CI
checkouts default to fetching one commit, which is enough to date the newest
commit and silently dates everything else to the build. When a target builds in
CI, check the checkout depth before blaming the feed, and treat a full history
fetch as the fix rather than a configuration change.

Front-matter dates are the fallback: set `date_from_meta` to a
mapping to read dates from page metadata instead. It must be a mapping, never a
bare boolean — a boolean value is rejected as a configuration error. Its
sub-keys select the creation and update fields, plus a default time and
timezone.

## Limits worth stating before the user commits

- `length` caps how many entries a feed carries, and defaults to 20. A site with
  more articles than that silently loses the oldest entries from the feed.
- `match_path` filters which pages appear, but it is compiled with a regex
  engine that has no look-around, so negative filters cannot be expressed. Its
  matching subject and anchoring are also undocumented and behave
  inconsistently against site paths. Do not build an exclusion rule with it, and
  do not enumerate allowed paths to work around that: a positive list silently
  drops every section added later. Accepting section index and about pages in
  the feed is the safer default; raise the cap instead.
- Unknown settings are rejected rather than ignored, so a key copied from
  another static site generator fails the build.
- `cache_dir` and `use_material_social_cards` are accepted but have no effect.
  Leave them out of new configuration and remove them when migrating.

Use single-quoted strings for any regular expression value. Double-quoted TOML
strings reject backslashes and will fail to parse.

## Validate and report

Run the site's own clean build, confirm the expected feed files exist, parse one
to confirm it is well-formed, count its entries, and check the publication dates
are real rather than a single build timestamp. Inspect a nested page's built
HTML to confirm the discovery link resolves. Report which files were generated,
where they will be served from, how many entries each feed carries, the date
source in use, and any limit the user may need to revisit as the site grows.

Do not claim a feed is working because the build succeeded. A clean build
produces the files even when the dates are wrong and no reader can discover them.

# Content components

This reference covers presentation choices that recur in Zensical Markdown.
The editorial reason for using a component belongs to the project's editorial
guidance; this file covers implementation checks.

## Admonitions

Use the syntax supported by the installed Zensical version and the repository's
existing examples. Confirm the type, title, indentation, and nested Markdown.
Choose a type that matches the intent: `tip` for practical help, `warning` or
`danger` for risk, `note` or `info` for context, and `example` or `question`
when the site supports them. Keep the callout useful when scanned alone.

Zensical's admonitions can contain nested Markdown and, when the relevant
extensions are enabled, collapsible or tabbed content. Check the target
configuration before relying on nesting. Do not replace the site's complete
Markdown-extension configuration with a partial example: this can silently
remove built-in extensions.

## Content tabs

Use tabs when alternatives are equivalent paths through one task. Keep the
shared explanation, prerequisites, and warnings outside the tab group. Verify
that each tab has a clear label, valid indentation, complete commands, and no
hidden step that another tab requires.

Zensical uses Python-Markdown-compatible indentation: nested tab or admonition
content normally requires four spaces. The site's `content.tabs.link` feature
can synchronize tabs with the same label across a page or site; use it only
when matching labels genuinely represent the same choice.

Before adding repeated sections, search the article and repository for an
existing tab pattern. After building, inspect the rendered page for readable
labels, working anchors, and non-empty panels.

## Links and navigation

Give important links a role: canonical identity, current procedure, official or
independent baseline, or deeper context. Check relative links against the
configured base path. Add one navigation entry in the canonical navigation
source and avoid duplicating local article links in index pages when the site's
rules prohibit them.

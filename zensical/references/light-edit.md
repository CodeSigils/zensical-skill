# Light Markdown editing

Use this reference for an explicit request to make a small content or
presentation edit in an existing Zensical site. It is not a general writing or
rewriting workflow.

## Inspect conventions first

Read the target page, front matter, nearest section index, comparable pages,
local `AGENTS.md`, and the site's existing admonition/tab patterns. Identify
the canonical navigation and configured base path before changing links or
routes.

For a new article, also inspect existing collections or section folders and
their landing pages. Choose the existing category that best matches the
article's primary reader question, not an incidental source repository or tool
mentioned in the article. If two placements would materially change its
audience or navigation, explain the options and ask the user; otherwise make
the smallest defensible placement. Do not create a category, collection entry,
or navigation branch without explicit authorization.

## Make the bounded change

- Change only the requested wording, Markdown, link, front matter, admonition,
  or content-tab block and directly required nearby lines.
- Preserve the author's voice, article structure, route, metadata shape, and
  repository conventions.
- Do not invent personal experience, claims, citations, metadata, or SEO copy.
- Do not convert a light edit into a developmental rewrite. If the page needs
  broader work, report it separately as a recommendation.
- Do not commit, push, publish, or deploy unless separately authorized.

## Validate and report

Run the smallest applicable build and link checks, inspect the affected rendered
page when feasible, and run `git diff --check`. Report the exact files changed,
the requested boundary, checks performed, and any remaining source or rendering
uncertainty.

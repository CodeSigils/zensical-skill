# Changelog

## Unreleased

- Improved skill discovery metadata, repository badges, the pinned
  `skills-ref` release check, and GitHub repository topics/description.
- Hardened repository hygiene for package caches, nested artifacts, and common
  credential-bearing files; fixed ShellCheck warnings in the scenario runner.
- Added a bounded, no-secret-output tracked-file hygiene preflight for common
  credential and private-key indicators before authorized publication work.
- Centralized scenario dependencies in one committed lockfile and reconciled
  stale fixture and validation status claims across the planning records.
- Added pinned Zensical `0.0.60` fixtures and an isolated scenario runner for
  tab rendering, accessibility-review evidence, and non-root deployment links.
- Made scenario dependency failures explicit and support an installed
  `ZENSICAL_BIN` for offline validation.
- Added a narrow Zensical skill payload for existing-site inspection, light
  editing, article review, content components, validation, and source routing.
- Added maintainer planning documents for scope, roadmap, research, and drift
  control.
- Added explicit boundaries between editorial intent and Zensical presentation
  syntax, including admonitions and content tabs.
- Added media and asset guidance covering images, optional GLightbox galleries,
  raw HTML video/audio embeds, base paths, accessibility, privacy, and
  rendered-output limits.
- Added capability-aware guidance for responsive media, scoped CSS overrides,
  custom MiniJinja themes, page-selected templates, and landing pages.
- Added cross-cutting accessibility guidance for semantic HTML, ARIA restraint,
  text alternatives, captions, transcripts, keyboard use, contrast, zoom, and
  honest WCAG validation boundaries.
- Added a lightweight commit-message checker and documented a curated changelog
  policy so detailed rationale remains in commits and research records.
- Refined repeated-value awareness into a smell/drift heuristic rather than a
  mandatory extraction rule; scoped it to repository scripts, CI, and
  configuration.
- Clarified that accessibility supports discoverability and usability but is
  not an SEO shortcut, ranking guarantee, or substitute for an SEO strategy.
- Added an explicit research-source priority: inspect the target repository,
  consult official Zensical documentation first for Zensical behavior, then use
  standards, primary providers, and clearly labelled community observations.
- Added MIT licensing, a security policy, and a release/discoverability
  checklist covering `skills-ref`, host checks, and marketplace evidence.

# Oh My OpenAgent Guide — editorial-review follow-up

- **Date:** 2026-09-24
- **Status:** maintenance edits applied and target build passed.
- **Target:** Code Sigils article
  `docs/AI/OpenCode/oh-my-opencode-guide.md` in
  `/home/sand/labs/zensical-test`.
- **Purpose:** exercise the optional Zensical article-review procedure after
  adding its voice-profile and tell-family coverage steps.

## Target guidance and voice profile

The target repository's `AGENTS.md` and the Digital Basement editorial charter
are authoritative. They call for serious, calm, practical, curious prose; a
concrete reader problem; visible judgment; safety-aware technical advice; and
no invented experience or certainty.

The article meets that profile. It opens with the repeated-setup problem,
recommends learning the host before adding an orchestration layer, carries that
decision through its safety and experiment sections, and closes on a practical
before-and-after record. The article is a technical decision guide, not a
feature catalogue.

## Sources revalidated

- Upstream project repository and its `dev` installation guide: the project
  currently documents separate OpenCode, Codex CLI Light, and standalone beta
  paths, telemetry, and an explicit Codex autonomous-permissions option.
- OpenCode's MCP documentation: enabled MCP tools add context and a large tool
  catalog can exceed the context limit.
- OpenAI's prior `developers.openai.com/codex/` links: each inspected page
  redirects to `learn.chatgpt.com/docs/`; the article now links to the
  canonical destinations directly.

## Review result

The voice-profile and coverage procedure behaved as intended.

| Tell family | Result |
| --- | --- |
| Negative-antithesis inversions | Present but load-bearing; keep. |
| Stacked rhetorical questions | None. |
| Opener tics and filler hedges | None. |
| Manufactured punctuation reveals | None. |
| Formulaic three-part lists | No problematic cluster. |
| Scope inflation, copula avoidance, and padding tails | None. |
| Performed-authenticity tells | None. |

The installed community lens was the local
`/home/sand/projects/prose-skills-research/antislop` checkout at `c65cd6b`
(SKILL version 3.0.0). Its zero-em-dash rule flagged the article's dashes, but
that is a project house rule rather than a target requirement. Six dashes are
annotated link descriptions and the two sentence-internal cases preserve the
article's rhythm. Treating them as defects would be over-correction. The score
therefore remains a lens output, not an editorial verdict or authorship claim.

## Implemented maintenance edits

1. Made the MCP-context caution concrete and directly attributable to OpenCode.
2. Replaced six redirecting Codex documentation URLs with canonical ChatGPT
   Learn URLs.
3. Advanced the article's `Last reviewed` date from 2026-09-09 to 2026-09-24.

No rewrite, title change, structural change, or automatic prose cleanup was
made. The articles' target voice remains intact.

## Resume point

1. `uv run zensical build --clean` was run from
   `/home/sand/labs/zensical-test` on 2026-09-24. It finished successfully in
   0.37 seconds with `No issues found`; it writes only the ignored `site/`
   output directory.
2. Inspect the focused target diff and decide whether to
   commit it in the target repository. Commit and push remain maintainer-only
   decisions.
3. In this skill repository, review the focused research/report diff. The
   fourth real pass confirms the current procedure; it found no repeated gap,
   so keep the runtime and roadmap unchanged.

## Records intentionally unchanged

- `zensical/references/article-review.md`: the test validated its current
  procedure; no new behavior was admitted.
- `docs/roadmap.md`: the test did not change phase status, scope, sequencing,
  or a deferred decision.
- `docs/vision.md`, `README.md`, and `zensical/references/source-registry.md`:
  no scope, discoverability, or generic primary-source registry change.
- Digital Basement umbrella records: the existing editorial/presentation
  boundary remains correct.

# Agent-skill structure and packaging conventions research

Created: 2026-09-24
Status: supporting evidence for the skill's `SKILL.md` frontmatter and
payload layout; re-verifiable at the pinned commits listed in Sources.
Does not define a packaging standard of our own — it records what the
wider ecosystem (and our payload) actually does.

## Why this record exists

The 2026-09-24 governance audit asked whether the skill's payload matches
the industry structure for agent skills. Two different validators exist and
are commonly confused, so this file records both contracts, the verified
examples behind them, and the exact status of our own payload against each.

## Two validation layers, not one

1. **agentskills `skills-ref validate`** — the strict spec enforcer, pinned
   in `release-checklist.md` at commit `69ef37e9424c0a7ea9dd2293b559e43ec8176379`.
   This is the validator our release checklist runs, and it passed
   (`Valid skill: zensical`) on 2026-09-09 and again 2026-09-24 after the
   frontmatter fix.
2. **skills.sh CLI (`npx skills`)** — the install/discovery tool
   (vercel-labs/skills). It performs near-zero validation: it requires only
   `name` and `description` as strings and never rejects an unknown field.

A common mistake is asking the CLI to "validate" a skill. It has no such
command — validation is the agentskills reference implementation's job.

## Spec frontmatter contract (agentskills, pinned `69ef37e`)

The specification (agentksills.io/specification; the anthropics *Agent
Skills* spec page redirects there) defines exactly these top-level fields
and nothing else:

| Field | Required | Constraints |
|-------|----------|-------------|
| `name` | yes | ≤64 chars, lowercase letters/digits/hyphens, no leading/trailing/double hyphens, must match the parent directory name |
| `description` | yes | 1–1024 chars |
| `license` | no | short license name or reference to a bundled license file |
| `compatibility` | no | top-level field, 1–500 chars, environment requirements |
| `metadata` | no | "a map from string keys to string values"; arbitrary client keys allowed |
| `allowed-tools` | no | space-separated pre-approved tools; Experimental |

The enforcer (`skills-ref` validator at the same pinned commit) hard-errors
on any other top-level key: `ALLOWED_FIELDS = {"name", "description",
"license", "allowed-tools", "metadata", "compatibility"}`. It does **not**
descend into `metadata` internals, so client-specific keys like
`short-description`, `keywords`, or `maintainers` are safe *under* metadata
but would be hard errors at the top level.

The spec also states:

- "A skill is a directory containing, at minimum, a `SKILL.md` file."
- "Keep your main `SKILL.md` under 500 lines. Move detailed reference
  material to separate files."
- "Use relative paths from the skill root" and keep `SKILL.md` references
  one level deep.
- Progressive disclosure: metadata (≈100 tokens) → `SKILL.md` body on
  activation → `references/` "loaded only when required".

## Industry-standard layout

```
<skill-name>/            # directory name == frontmatter name
├── SKILL.md             # frontmatter + routing body, < 500 lines
├── references/          # optional; focused, lowercase, hyphenated files
│   └── topic.md         #   e.g. finance.md, legal.md, skill-feedback.md
├── scripts/             # optional; executable; invoked root-relative
│   └── tool.py          #   as `scripts/tool.py`, never `../scripts/…`
├── assets/              # optional
└── agents/              # optional extra directory (e.g. openai.yaml)
```

Verified real-world examples:

- **supabase/agent-skills** — `SKILL.md` + `references/skill-feedback.md`
  routed as `[Skill Feedback](references/skill-feedback.md)` + `assets/`.
- **mattpocock/skills** (`diagnosing-bugs`) — `scripts/` inside the skill
  dir, invoked `scripts/hitl-loop.template.sh`.
- **vercel-labs/agent-skills** (`web-design-guidelines`) — `SKILL.md` only,
  minimal metadata (`author`/`version`/`argument-hint`).
- **anthropics/skills** (`frontend-design`) — `SKILL.md` + bundled
  `LICENSE.txt`, with `license: Complete terms in LICENSE.txt`.
- **openclaw/clawhub** (`technical-documentation`) — `SKILL.md` routes a
  numbered workflow to `references/{principles,build,review,tooling,openclaw}.md`
  + `assets/` + `agents/`.
- **CodeSigils/zola-skill** (our sibling) — `SKILL.md` + `references/` +
  a non-standard `workflows/` directory; `compatibility`/`about`/`keywords`/
  `version`/`maintainers`/`repository` all nested under `metadata`.

## The `agents/openai.yaml` convention

`agents/openai.yaml` is **not** part of the agentskills spec nor the
skills.sh contract. It is a real convention from the OpenClaw/ClawHub
ecosystem (see Sources), with the shape:

```yaml
interface:
  display_name: …
  short_description: …
  default_prompt: …
```

The fuller ClawHub form also supports `icon_small`/`icon_large`/`brand_color`
and `policy.allow_implicit_invocation`. Our
`zensical/agents/openai.yaml` matches the OpenClaw subset exactly.

Note: `metadata.short-description` in `SKILL.md` duplicates
`agents/openai.yaml` `short_description` (OpenClaw's display source of
truth). Keep the two in sync when either changes.

## Zensical payload status against these findings

| # | Check | Status |
|---|-------|--------|
| 1 | No unrecognized top-level frontmatter fields | OK — `keywords`/`repository`/`maintainers` correctly nested under `metadata` |
| 2 | `compatibility` is a spec top-level field | Fixed 2026-09-24 in commit `311adf8` (was wrongly nested as `metadata.compatibility`; moved between `license` and `metadata`) |
| 3 | `metadata` values are strings per spec | Tolerated deviation — `keywords`/`maintainers` are YAML arrays; not validator-enforced; zola-skill does the same |
| 4 | `name`/`description` present and conformant | OK — `name: zensical` matches the directory |
| 5 | Layout compliant | OK — `SKILL.md` at payload root (205 lines < 500), 9 focused lowercase `references/` files, executable `scripts/` |
| 6 | Script references use skill-root-relative paths | OK — references invoke `scripts/check_instruction_contract.py` and `scripts/check_site_hygiene.sh`, the spec-recommended form |
| 7 | `agents/openai.yaml` | OK with duplication note — matches OpenClaw convention; keep `short_description` in sync with `metadata.short-description` |

## Sources

All verified 2026-09-24.

1. agentskills Agent Skills specification, pinned commit
   `69ef37e9424c0a7ea9dd2293b559e43ec8176379`
   (`docs/specification.mdx`; canonical site agentskills.io/specification).
2. agentskills `skills-ref` validator, same pinned commit
   (`skills-ref/src/skills_ref/validator.py`).
3. agentskills `main` — `skills-ref` docs and
   `docs/skill-creation/{quickstart,best-practices,using-scripts}.mdx`.
4. vercel-labs/skills (skills.sh CLI) @ `7407f3893ad4dceab546ac002c3ef806e4000c73`
   (`src/skills.ts`, `src/cli.ts`, `src/frontmatter.ts`, `src/installer.ts`).
5. skills.sh and skills.sh/docs.
6. anthropics/skills.
7. vercel-labs/agent-skills.
8. mattpocock/skills.
9. supabase/agent-skills.
10. CodeSigils/zola-skill.
11. openclaw/clawhub.
12. openclaw/openclaw code search + docs.openclaw.ai/skills/.

Items 4–12 were inspected at `main`/HEAD unless a SHA is given inline;
items 1–2 at the exact pinned release commit.
# Skill sync and cross-agent distribution research

Created: 2026-09-26
Status: supporting evidence for the install/distribution decision; answers one
question — when a user installs a copy of a portable skill, how does anyone
find out the copy is stale? Records what the ecosystem actually ships, at
sources that can be re-checked. Sibling of `skill-structure-conventions.md`,
which records the payload's on-disk shape; this file records what happens to a
copy *after* it leaves the source repository.

## Why this record exists

The skill is distributed as a copy. A user installs it once into an agent's
skills directory; the upstream repository keeps moving. Nothing in the format,
the registry, or the installer tells the installed copy that it is behind.

This file separates three things that are easy to conflate:

1. **What exists** — verified mechanisms, with a URL and a `Checked
   2026-09-26` marker.
2. **What does not exist** — searched-for and confirmed absent, so the gap is
   not re-researched from scratch.
3. **Judgement** — this project's reading of the above, argued separately and
   labelled as such.

Every claim in sections 1–3 is a statement about an external artifact I fetched
on 2026-09-26. Where I inferred rather than read, it says so.

## Headline result

| Target | Usable result? |
|--------|----------------|
| 1. Practitioner guidance on distributing/updating skills | **Partly.** Rich, quotable material on *portability* and *hygiene*. Nothing — after reading six of the author's own documents in full — on *keeping installed copies in sync*. Clean negative. |
| 2. skills.sh registry and CLI | **Yes, decisive.** A real update path exists (`skills update`), backed by two lock files carrying content hashes. But there is **no read-only "is it stale?" command**, and the project-scope lock is a newer, less documented mechanism. |
| 3. Cross-agent distribution conventions | **Yes.** One portable directory shape, two competing location conventions (`.agents/skills/` vs per-vendor), and **no version field, manifest, or update channel in the format spec at all**. |

The short version: the ecosystem's answer is "re-run the installer's update
command". There is no spec-level answer, and no widely-used answer to the
question a *consumer* would want answered — "is my copy behind?".

---

## 1. Verified findings — practitioner guidance

### 1.1 Addy Osmani

**Checked 2026-09-26. He publishes a widely-read skills pack and is explicit
about how to install it. He does not address the stale-installed-copy problem
anywhere I could find.** The negative below is a documented one, not an
absence of looking.

What he *does* say, and it is useful:

- **Portability is the property being bought by the plain-Markdown format.**
  From "Agent Skills" (2026-05-03), <https://addyosmani.com/blog/agent-skills/>:
  > "The portability of the skills format matters too. The same SKILL.md file
  > works in Claude Code, Cursor (with rules), Gemini CLI, Codex, and any other
  > harness that accepts system-prompt content. Write the workflow once, the
  > runtime enforces it. That's the thing the markdown-with-frontmatter format
  > buys you that bespoke prompt engineering does not."

  He offers three install modes and recommends the marketplace one, with
  "drop the markdown into your tool of choice" as the tool-agnostic fallback.

- **Shared material must live inside the skill, or a per-skill install breaks.**
  From the pack's README (<https://github.com/addyosmani/agent-skills>), the
  block most relevant to a single-skill publisher:
  > "**Installing one skill?** A per-skill `npx` install copies only
  > `skills/<skill>/`, not the repo-level `references/` directory. The skill
  > still works, but paths to supplementary shared checklists are unavailable.
  > Use a whole-repo integration, clone the repository, or copy the needed
  > checklist into a `references/` directory inside the installed skill. This
  > portability gap is tracked in #361."

  This is the same class of problem as staleness — the copy is not equivalent to
  the repo — and his fix is *structural* (self-containment), not a version
  mechanism.

- **Host adapters are per-vendor, on purpose.** Same README:
  > "Host-specific paths are native discovery conventions, not branding
  > aliases; renaming or merging them would break the tools that scan those
  > exact locations."

  He ships `.claude/commands/`, `.gemini/commands/`, `.codex-plugin/`,
  `plugin.json`, and an `AGENTS.md`, alongside a portable `skills/` core.

- **His staleness answer is periodic human audit, not an update channel.**
  From "Audit your Agent files" (2026-08-27),
  <https://addyosmani.com/blog/audit-your-agent-files/>:
  > "Your coding agent's configuration has a half-life. Models improve,
  > harnesses add capabilities, codebases change, and the instructions we wrote
  > for an older version stay behind."

  > "I now run Claude's /doctor every few weeks, review memory separately, and
  > ask each instruction to earn its place again."

  The concern in that post is *bloat, redundancy, and unused skills* — a user
  with too many skills — not a user whose one skill is behind upstream. `/doctor`
  is an inventory-and-cost audit, not a freshness check against a source repo.

- **Staleness is handled at the author end, by accepting bug reports.** From
  his `CONTRIBUTING.md`
  (<https://github.com/addyosmani/agent-skills/blob/main/CONTRIBUTING.md>),
  under "Reporting Issues":
  > "Open an issue if you find: A skill that gives incorrect or outdated
  > guidance … If a skill's guidance was wrong, outdated, or did not apply in
  > your project … use the Skill gap issue form. It asks for the affected skill,
  > the relevant excerpt, your project context, and what you did instead."

  That is a real convention: *outdated guidance is an issue, with a structured
  template.* It is a manual, human-mediated channel. It does not detect staleness
  and does not reach the person with the stale copy.

- **One genuine drift observation, about translations.**
  Same file:
  > "We don't accept translations of the documentation (README, `docs/`) or of
  > skills and their content. Translated copies drift out of sync as skills and
  > docs evolve, and we have no way to maintain them long-term without leaning
  > on agent translations plus community corrections, which adds maintenance
  > cost for limited value."

### 1.2 The clean negative, stated precisely

I read six of his own documents in full on 2026-09-26 — the pack `README.md`,
`CONTRIBUTING.md`, `AGENTS.md`, `docs/adoption-guide.md`,
`docs/getting-started.md`, `docs/skill-anatomy.md` — searching for guidance on
versioning, pinning, updating, or re-syncing installed skill copies.

**There is none.** No document tells a user how to tell that their installed
copy is behind, no document tells a user how to bring it forward, and no
document recommends pinning a skill to a commit or tag. The pack's own answer
to distribution is a one-line install command plus a note that the fast path is
`npx skills add <owner>/<repo>` — i.e. it inherits the CLI's update behaviour
rather than defining its own.

**Design consequence: do not look to this practitioner for a convention to
adopt.** There is nothing there to copy, and the fact that a widely-followed
maintainer of a ~70k-star skills pack has not solved it is itself evidence about
how unsolved the problem is.

### 1.3 A published attempt that failed, and why

This is the closest thing to a worked experiment, and it argues against
inventing a self-check. From "How I made my skills update themselves"
(2026-04-14, updated 2026-04-18), <https://joost.blog/self-updating-agent-skills/>,
a skill author who shipped a version-check mechanism, published it, and then
replaced it:

> "I updated one of my Agent Skills and realized I had no way to tell my other
> machines they were running a stale copy. Skills install as loose folders in
> `~/.claude/skills/`. The skill runs whatever's on disk — and has no way of
> knowing there's a newer version."

The abandoned mechanism was four parts: a `version:` field in each skill's
frontmatter, a `versions.json` at the repo root, a paragraph instructing the
agent to check the manifest on invocation and offer an update, and a CI check
to keep the two in sync. His assessment of the costs:

> "It worked. But it had real costs — tokens on every invocation even when
> nothing had changed, and a mid-task re-invoke nobody wanted — and I'd claimed
> that centralizing the check 'needs harness support Claude Code doesn't expose
> to skill authors today.' People in the thread corrected both."

What replaced it was delegation to the installer plus, optionally, a
`SessionStart` hook that runs `npx skills update -g -y` outside the context
window. His closing advice to skill maintainers:

> "No releases needed — `npx skills update` pulls directly from `main`. A
> per-skill `README.md` is worth adding: skills.sh shows it on each skill's
> individual page. Include the `SessionStart` hook snippet in your `README` for
> users who want zero-friction updates. No runtime. No service. No tokens."

---

## 2. Verified findings — the skills.sh registry and CLI

This is the mechanism the ecosystem actually has. All source citations below
are at vercel-labs/skills commit
`7407f3893ad4dceab546ac002c3ef806e4000c73` (main, 2026-09-17).

### 2.1 `zensical`-related skills on the registry

**Checked 2026-09-26** against the registry's own search endpoint
(<https://skills.sh/api/search?q=zensical>). The registry is large and busy;
`zensical` is a crowded name. Fourteen relevant entries, plus five fuzzy
false-positives the API returned (Python/docs skills matching on the substring
`jessical`/`rewrite` — noise, not zensical skills).

| Skill | Author | Installs | What it does | Maintained? |
|-------|--------|----------|--------------|-------------|
| `zensical` | (this project) | 1 | Review, lightly edit, and validate existing Zensical static sites; presentation/site maintenance, explicitly not a writing voice or autonomous publishing skill | This project's own listing |
| `zensical-site` | `layeredcraft/skills` | 10 | Create/revise content for zensical.org; compact reference pages, links out to upstream docs for depth | **Closest competitor.** Content-authoring rather than site maintenance |
| `zensical` | `kettleofketchup/dotfiles` | 3 | Zensical as MkDocs Material successor: install (pip/uv/Docker), `zensical.toml`, dev workflow, split into topic reference pages | Active-looking; shipped inside a dotfiles repo |
| `koda-zensical` | `xcode-nlp/kodaskills` | 4 | Zensical inside a larger Koda skills pack | Not read; installs only |
| `zensical-setup` | `brpaz/agent-skills` | 2 | Add or migrate to Zensical: generate `zensical.toml`, scaffold `docs/`, migrate from MkDocs/Material | Not read; installs only |
| `zensical-setup` | `ai-riksarkivet/ra-anno` | 1 | Same name, different author — the registry does not namespace by name | Not read |
| `zensical-development` | `zeulewan/claude-code-skills` | 1 | Development best practices; "CRITICAL: Always Use Zensical, Never MkDocs Directly" | Not read |
| `zensical-debug` | `zeulewan/claude-code-skills` | 1 | Companion to the above | Not read |
| `zensical-customizer` | `titusz/skills` | 1 | Customisation | Not read |
| `zensical-customizer` | `owi-lab/owi-metadatabase-shm-sdk` | 1 | Same name, unrelated repo | Not read; likely incidental |
| `zensical-authoring` | `ai-riksarkivet/ra-mcp` | 1 | Authoring via an MCP server | Not read |
| `zensical-authoring` | `ai-riksarkivet/ra-anno` | 1 | Same author's companion | Not read |
| `zensical` | `ml4gland/seqpro` | 1 | Zensical inside a larger project repo | Not read |
| `zensical` | `kettleofketchup/kettleofskills` | 1 | Same author, standalone skills repo | Not read |

Four of these I fetched and read the rendered `SKILL.md` on the registry page
for (`zensical-site`, `kettleofketchup/dotfiles/zensical`,
`brpaz/agent-skills/zensical-setup`, `zeulewan/zensical-development`); the rest
are name, author, and install count from the search API only. **"Maintained?" is
answered only where I have evidence** — the install counts are lifetime totals,
not activity, and I did not check commit recency for any of them.

Two structural observations that matter more than the individual entries:

- **The name is not unique and nothing in the format prevents that.** Four
  distinct authors have published a skill named `zensical`, and two have
  published `zensical-setup`. Discovery is by name-plus-author.
- **This project's own listing exists and is the lowest-trafficked of the
  family at 1 install**, alongside a competitor at 10 with a clearly adjacent
  scope. Nobody has solved distribution; there is a crowded field and no
  leader.

Registry scale, for context, from the registry owner's own report (2026-09-25),
<https://vercel.com/blog/state-of-agent-skills>: "In seven months, the skills.sh
registry grew to one million agent skills and recorded nearly 280 million
installs."

### 2.2 The CLI's actual command surface

**Checked 2026-09-26** by running the CLI's own help output
(`npx -y skills@latest --help`). The full command set:

| Command | Present in `--help`? | What it does |
|---------|----------------------|--------------|
| `add <package>` | yes | Install a skill package |
| `use <package>@<skill>` | yes | Generate a prompt for one skill without installing |
| `remove [skills]` | yes | Remove installed skills |
| `list`, `ls` | yes | List installed skills |
| `find [query]` | yes | Search for skills |
| `update [skills...]` | yes | **"Update skills to latest versions (alias: `upgrade`)"** |
| `init [name]` | yes | Scaffold a `SKILL.md` |
| `experimental_install` | yes | "Restore skills from `skills-lock.json`" |
| `experimental_sync` | yes | "Sync skills from `node_modules` into agent directories" |
| `check` | **no** | See below — exists, undocumented |
| `sync`, `outdated`, `doctor` | **no** | Do not exist |

**So: yes, an update subcommand exists and is documented — `skills update`,
also reachable as `skills upgrade`.** Update flags are `-g/--global`,
`-p/--project`, `-y/--yes`, and an optional list of skill names.

**The important negative: there is no read-only staleness report.**
`check` is not in the help output and not in the README's command table, but it
*is* dispatched — and it is dispatched to the same mutating handler as
`update`:

```typescript
case 'check':
case 'update':
case 'upgrade':
  await runUpdate(restArgs);
  break;
```

([`src/cli.ts` L398–L402](https://github.com/vercel-labs/skills/blob/7407f3893ad4dceab546ac002c3ef806e4000c73/src/cli.ts#L398-L402)).
`runUpdate` calls `updateGlobalSkills` / `updateProjectSkills`, which reinstall
changed skills ([`src/update.ts` L987](https://github.com/vercel-labs/skills/blob/7407f3893ad4dceab546ac002c3ef806e4000c73/src/update.ts#L987)).
There is no `--dry-run` among its options. An early community description of
`check` as printing without installing ([issue #283,
2026-02-04](https://github.com/vercel-labs/skills/issues/283)) described
behaviour that the current dispatch cannot produce.

### 2.3 How staleness is actually detected

Two lock files, with different hash semantics. This is the mechanism worth
adopting.

**Global lock** — `~/.agents/.skill-lock.json`, or
`$XDG_STATE_HOME/skills/.skill-lock.json` if that variable is set
([`src/skill-lock.ts` L62–L73](https://github.com/vercel-labs/skills/blob/7407f3893ad4dceab546ac002c3ef806e4000c73/src/skill-lock.ts#L62-L73)).
Schema version 3. Each entry carries a GitHub **tree SHA** of the skill folder:

```typescript
export interface SkillLockEntry {
  source: string;
  sourceType: string;
  sourceUrl: string;
  ref?: string;
  skillPath?: string;
  /**
   * GitHub tree SHA for the entire skill folder.
   * This hash changes when ANY file in the skill folder changes.
   * Fetched via GitHub Trees API by the telemetry server.
   */
  skillFolderHash: string;
  installedAt: string;
  updatedAt: string;
  // …
}
```

([`src/skill-lock.ts` L13–L38](https://github.com/vercel-labs/skills/blob/7407f3893ad4dceab546ac002c3ef806e4000c73/src/skill-lock.ts#L13-L38)).
Note the comment: the tree SHA is fetched **by the telemetry server**, not
computed by the CLI. It is a *content* hash, not a semver, and it has no
human-readable form. Reading the lock is also not fail-safe: a schema older
than current is silently discarded rather than migrated
([`src/skill-lock.ts` L80–L103](https://github.com/vercel-labs/skills/blob/7407f3893ad4dceab546ac002c3ef806e4000c73/src/skill-lock.ts#L80-L103)).

**Project lock** — `skills-lock.json` in the working directory, schema version
1. Each entry carries a hash **computed locally from the files on disk**:

```typescript
/**
 * Represents a single skill entry in the local (project) lock file.
 *
 * Intentionally minimal and timestamp-free to minimize merge conflicts.
 * Two branches adding different skills produce non-overlapping JSON keys
 * that git can auto-merge cleanly.
 */
export interface LocalSkillLockEntry {
  source: string;
  sourceUrl?: string;
  ref?: string;
  sourceType: string;
  skillPath?: string;
  /** … Unlike the global lock which uses GitHub tree SHA, the local lock
   *  computes the hash from actual file contents on disk. */
  computedHash: string;
  // …
}
```

([`src/local-lock.ts` L8–L46](https://github.com/vercel-labs/skills/blob/7407f3893ad4dceab546ac002c3ef806e4000c73/src/local-lock.ts#L8-L46)).
The hash function walks the skill directory, sorts files by relative path, and
hashes path-plus-content so renames are detected
([`src/local-lock.ts` L140–L160](https://github.com/vercel-labs/skills/blob/7407f3893ad4dceab546ac002c3ef806e4000c73/src/local-lock.ts#L140-L160)).
Entries are written sorted alphabetically for clean diffs, and the file is
explicitly "meant to be checked into version control"
([`src/local-lock.ts` L48–L60](https://github.com/vercel-labs/skills/blob/7407f3893ad4dceab546ac002c3ef806e4000c73/src/local-lock.ts#L48-L60)).

**The comparison itself** is a tree-hash lookup compared against the recorded
hash; a difference marks the skill for reinstall:

```typescript
const latestHash = getSkillFolderHashFromTree(tree, entry.skillPath!);
if (latestHash && latestHash !== entry.skillFolderHash) {
  updates.push({ name: skillName, source, entry });
}
```

([`src/update.ts` L592–L593](https://github.com/vercel-labs/skills/blob/7407f3893ad4dceab546ac002c3ef806e4000c73/src/update.ts#L592-L593)),
with a `git clone` fallback that recomputes the hash from the clone when the
API path is unavailable ([`src/update.ts` L638–L643](https://github.com/vercel-labs/skills/blob/7407f3893ad4dceab546ac002c3ef806e4000c73/src/update.ts#L638-L643)).

**Skills that cannot be checked are a first-class, named state.** The CLI has
an explicit skip-reason function:

```typescript
export function getSkipReason(entry: SkillLockEntry): string {
  if (entry.sourceType === 'local') return 'Local path';
  if (entry.sourceType === 'git') return 'Git URL';
  if (entry.sourceType === 'well-known') return 'Well-known skill';
  if (!entry.skillFolderHash) return 'Private or deleted repo';
  if (!entry.skillPath) return 'No skill path recorded';
  return 'No version tracking';
}
```

([`src/update.ts` L186–L204](https://github.com/vercel-labs/skills/blob/7407f3893ad4dceab546ac002c3ef806e4000c73/src/update.ts#L186-L204)).
For those it does not fail — it prints a recovery command, `npx skills add
<source> -g -y`
([`src/update.ts` L213–L241](https://github.com/vercel-labs/skills/blob/7407f3893ad4dceab546ac002c3ef806e4000c73/src/update.ts#L213-L241)).
Project scope has its own gates: `node_modules` and `local` sources are
excluded, and an entry with no `skillPath` yields "No project skills can be
updated in place."
([`src/update.ts` L244–L260](https://github.com/vercel-labs/skills/blob/7407f3893ad4dceab546ac002c3ef806e4000c73/src/update.ts#L244-L260),
[L775–L782](https://github.com/vercel-labs/skills/blob/7407f3893ad4dceab546ac002c3ef806e4000c73/src/update.ts#L775-L782)).

**Restore-from-lock exists but is experimental and deliberately narrow.**
`experimental_install` reads the project lock and re-runs the add pipeline,
with this scope note: "Only installs to `.agents/skills/` (universal agents) —
the canonical project-level location. Does not install to agent-specific
directories." ([`src/install.ts` L9–L17](https://github.com/vercel-labs/skills/blob/7407f3893ad4dceab546ac002c3ef806e4000c73/src/install.ts#L9-L17)).

### 2.4 Known defects in this mechanism, as of 2026-09-26

Both are directly relevant to a single-maintainer project that documents a
`--copy` install.

- **`skills update` silently converts `--copy` installs into symlinks.**
  [Issue #1199, open since 2026-05-20, last activity 2026-09-07](https://github.com/vercel-labs/skills/issues/1199).
  Its root-cause analysis is the important part:
  > "`update` internally calls `skills add` via `spawnSync` but does not pass
  > `--copy`. Additionally, `skills-lock.json` lock entries (`SkillLockEntry` /
  > `LocalSkillLockEntry`) do not track the install mode — there's no field to
  > distinguish whether a skill was originally installed as symlink or copy. So
  > `update` has no way to know which mode to use."

  The proposed fix is a single new lock field (`installMode`). **Still open.**
  A project whose documented install uses `--copy` cannot rely on `update`
  preserving its install shape.

- **`update` has failed wholesale under `npx` invocation.**
  [Issue #371](https://github.com/vercel-labs/skills/issues/371) — updates
  detected, none applied, no error detail. Linked fixes: [#432](https://github.com/vercel-labs/skills/pull/432)
  ("use process.execPath instead of npx in update command") and
  [#487](https://github.com/vercel-labs/skills/pull/487) ("print child process
  output on failure"). I did not re-test the current release against this.

---

## 3. Verified findings — cross-agent distribution conventions

### 3.1 The on-disk layout: one shape, two location conventions

**Checked 2026-09-26** against the CLI's agent table and its
`src/agents.ts`. The *skill* is one portable directory — `SKILL.md` plus
optional `scripts/`, `references/`, `assets/` — and that part is genuinely
settled. The *location* is where hosts diverge, and it resolves into two
groups, not seventy:

- **A shared "universal" project path, `.agents/skills/`.** A large majority of
  the supported agents map to exactly this: Codex, Cursor, Gemini CLI, GitHub
  Copilot, Cline, Zed, Amp/Replit, Deep Agents, Firebender, and others. Global
  installs land under `~/.agents/skills/` or a per-vendor equivalent.
- **Per-vendor paths for hosts with their own convention.** Claude Code
  (`.claude/skills/`), OpenCode (`~/.config/opencode/skills/`), Hermes
  (`.hermes/skills/`), Kiro (`.kiro/skills/`), and so on.

For this project's three-host matrix, the split is:

| Host | Project path | Global path |
|------|--------------|-------------|
| Codex | `.agents/skills/` | `~/.codex/skills/` |
| OpenCode | `.agents/skills/` | `~/.config/opencode/skills/` |
| Hermes | `.hermes/skills/` | `~/.hermes/skills/` |

Note that Codex and OpenCode share the same project location. That is a real
simplification available at install time, and it is invisible if you only look
at global paths.

**Installation is a file copy, not a package resolution.** The CLI discovers
skills by walking conventional directories (and optionally
`.claude-plugin/marketplace.json` / `plugin.json`), then writes files. There is
no resolution step where a version is selected, which is precisely why staleness
needs a separate mechanism.

### 3.2 The format spec has no version, no manifest, no update channel

**Checked 2026-09-26.** I fetched the agentskills specification
(<https://agentskills.io/specification>, source
<https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx>)
and grepped the complete document for `version`, `updat`, `distribut`,
`install`, `refresh`, `out of date`, `stale`, and `lock`.

**The only two hits in the entire specification are the same example line:
`version: "1.0"`, nested inside a `metadata:` block.** The spec's complete
frontmatter field list is six fields — `name`, `description`, `license`,
`compatibility`, `metadata`, `allowed-tools` — and `version` is not among them.

Concretely, the format spec defines:

- a directory shape ("A skill is a directory containing, at minimum, a
  `SKILL.md` file");
- six frontmatter fields with constraints;
- a body, optional `scripts/`/`references/`/`assets/` directories, and a
  progressive-disclosure loading model.

It defines **no version field, no manifest, no integrity value, no lockfile, and
no update channel.** `metadata` is documented as "Arbitrary key-value mapping
for additional metadata (a map from string keys to string values)" — so a
publisher *may* put a version string there, and that is exactly what the spec's
own example does, but the field carries no defined meaning and nothing in the
ecosystem reads it.

**This is the single most important negative in this file.** There is no
format-level answer to the stale-copy problem, and a new project cannot design
*for* a version field because none is specified.

### 3.3 What comparable ecosystems use

Mapping the mechanisms other ecosystems use onto "a folder of markdown with no
runtime":

| Ecosystem mechanism | How it signals staleness | Does it translate? |
|---|---|---|
| `npm outdated` / `npm ci` | Semver range vs resolved version in a lockfile; a separate read-only query for the report | **Closest analogue.** The ecosystem's answer is *two* mechanisms: a lockfile for reproducibility, and a separate read-only query for the report. The skills CLI has the first and not the second. |
| Content hash in a lockfile (as `skills-lock.json` does) | Byte-level identity, no semver needed | **Already available here** and the reason a semver-less artifact can still be checked. Best fit for markdown. |
| Dependabot / Renovate | Automated PRs against a manifest | Plausible but heavy: needs a manifest per consumer repo, and a solo-maintainer skill is not a dependency graph. |
| VS Code extension auto-update | Host-owned update service, extension-declared version | **Does not translate** — there is no host-owned service for a third-party skill folder, and no host manifest. |
| Container tags (`latest`, digests) | Registry-side; consumers pin a digest | Only if a registry holds the artifact. The skills registry is a *directory*, not an artifact store. |
| Git submodule / subtree pin | The commit pointer *is* the version | **Viable and git-native**, but it makes the consumer's repo carry a pointer, which contradicts "install a copy". |

**The generalisable lesson: the ecosystems that solve this well all separate
"record what you have" from "report that it is behind".** `package-lock.json`
plus `npm outdated`. The skills CLI has the recording half in two places and
the reporting half nowhere.

---

## 4. What already exists that we should adopt

Ranked by evidence strength, not by novelty.

1. **`skills update` / `skills upgrade`, and tell users it exists.** Verified
   to exist in the CLI's own help output. This is the ecosystem's answer and
   the one a competitor-independent publisher should point at. It is free: no
   code from us.
2. **Content hash, not semver.** Both lock files use a hash of the skill
   folder's contents. For a markdown payload with no release process, a
   content hash is the only staleness signal that is both correct and cheap to
   produce. If we ever publish a self-check, hash — do not invent a version
   ladder.
3. **A project-scoped, committable, merge-friendly lock.** The `skills-lock.json`
   design notes are directly transferable: no timestamps, sorted keys,
   deterministic output, "meant to be checked into version control". A
   project-scope install (no `-g`) already writes such a file, and it already
   records a locally computed hash of the installed copy.
4. **A named "cannot be checked" state with a recovery command.** The skip
   reasons are a good pattern: an uncheckable install is reported honestly with
   the exact command that fixes it, rather than silently skipped. Note also
   that local-path, generic-git and well-known sources are *inherently*
   uncheckable — a real limitation of hash-based tracking, not a bug.
5. **Self-containment of shared material.** A widely-followed maintainer
   independently hit the same failure class and fixed it by moving shared
   material inside the skill directory, so a per-skill copy is complete. This
   project already does this; it is worth stating as a deliberate property
   rather than an accident.
6. **A "report outdated guidance" issue form.** A structured, low-friction
   channel for "your copy is behind" that a human maintainer can act on. Cheap,
   needs no mechanism, and it is the convention a major pack uses.

---

## 5. What does not exist

Stated as searched-and-confirmed-absent, so this is not re-researched.

- **No `version` field, manifest, integrity value, or update channel in the
  format spec.** Verified by full-text search of the specification. `version`
  appears only as an example value inside `metadata`.
- **No read-only "is my installed copy stale?" command in the skills CLI.**
  `check` exists in the dispatcher but routes to the mutating `update` handler,
  and there is no `--dry-run`. A consumer cannot ask without acting.
- **No lock entry field recording the install mode**, so `update` cannot
  preserve a `--copy` install. Verified open as of 2026-09-26.
- **No host-level update service for third-party skill folders.** No major host
  (Codex, OpenCode, Hermes) advertises one.
- **No statement from the practitioner target about keeping installed copies in
  sync.** Six of that author's own documents read in full; nothing on
  versioning, pinning, or updating installed copies.
- **No stable, unique skill names.** The registry tolerates four distinct
  authors publishing `zensical` and two publishing `zensical-setup`. There is
  no namespacing or collision policy to lean on.
- **No self-check mechanism that survived contact with real use.** The one
  documented attempt was withdrawn by its author, with costs measured in
  per-invocation tokens and unwanted mid-task re-invokes.

---

## 6. Judgement

Clearly separated from the findings above. This is interpretation, not
evidence.

- **The problem is real but the population is small, and that should size the
  response.** A stale installed copy only causes harm when the user *acts* on
  the skill after upstream changed it, and only when the change mattered to
  their task. The failure mode is silent and wrong-but-plausible guidance —
  annoying, occasionally costly, rarely catastrophic. That argues for a
  low-cost, low-certainty mechanism over an engineered one.
- **The honest cost of a self-check is paid on every invocation, by every user,
  to serve a minority of sessions.** The withdrawn experiment measured this
  directly. Any mechanism we invent that runs inside the skill's own text pays
  that tax. Any mechanism outside it does not — which points away from
  in-payload checks and toward the installer, a CI job, or documentation.
- **A hash is the right identity, but a bare hash is a poor message.** Comparing
  `e30630fd7c20fdc5…` to a remote tree SHA tells a *machine* that a copy is
  behind and tells a *person* nothing actionable. If we surface staleness, the
  useful output is a sentence and a command, not a digest.
- **Adopting someone else's mechanism is cheap; extending it is not.** Depending
  on `skills update` costs nothing and inherits a known `--copy` defect we can
  document around. Building our own updater duplicates a solved problem and
  inherits maintenance forever. The asymmetry strongly favours the dependency.
- **The registry is crowded enough that "be findable" is not a solved problem
  either.** Fourteen `zensical`-named entries, install counts in the single
  digits, no leader. Effort spent on distribution mechanics has a low ceiling
  here; effort spent on the skill being obviously better than its neighbours is
  the higher-leverage move. This is the main reason I lean toward a minimal
  answer.

---

## 7. Recommendation for this project

Framed for one maintainer, a payload of roughly a thousand lines of markdown and
scripts, and exactly one installed host.

**Recommendation: ship a documented update path, not a mechanism. Concretely —
(a) state in the install documentation that `skills update` is how an installed
copy is brought forward, and give the exact command for the project's install
shape; (b) ensure the install is project-scoped rather than global, so a
`skills-lock.json` with a content hash exists and is committable; (c) keep the
payload self-contained so a per-skill copy is complete; (d) add an "outdated
guidance" issue path.**

Why each piece earns its place:

- **(a) is the whole adoption.** Verified to exist, costs one paragraph, and is
  the ecosystem default. It converts a silent failure into a documented one.
- **(b) matters because the global lock and the project lock are different
  mechanisms with different hash semantics.** The project lock's hash is
  computed locally from files on disk, which is the property that makes "compare
  what I have" possible at all without contacting a server. A global install
  leans on a tree SHA fetched by a telemetry service.
- **(c) is already true; recording it as intentional costs nothing and forecloses
  a future "let's share these references across skills" refactor that would
  silently break per-skill installs.
- **(d) is the fallback for the cases no mechanism covers, and it is the
  convention a major pack uses.

**What we chose NOT to do, and why**

- **Not a `version:` field in the skill frontmatter.** The spec has no such
  field, so it would be non-standard metadata that only we interpret; nothing in
  the ecosystem reads it. If a version is wanted later, `metadata` is the
  spec-sanctioned place, and it should be added when a release process exists to
  give it meaning — not before, because a version number with no releases behind
  it is a lie that ages badly.
- **Not a `versions.json` manifest plus an in-payload instruction to check it.**
  This is the withdrawn pattern, with measured costs: tokens on every invocation
  and a mid-task re-invoke users did not want. Its own author removed it. A
  single-maintainer project should not re-run an experiment that has already
  been published, costed, and retracted.
- **Not a CI job that opens an issue when the payload changes.** The trigger
  condition is "the maintainer committed", which the maintainer already knows.
  It would be a self-message with extra machinery. The genuine gap is the
  *consumer* side, and CI cannot reach it.
- **Not shipping our own updater or freshness script.** The problem is solved
  upstream; reimplementing it means maintaining git-clone, hash-comparison, and
  symlink/copy handling forever, for one skill. The one defect that matters
  (update converting `--copy` to symlinks) is documented and has a one-line
  upstream fix pending; it is cheaper to route around than to fork for.
- **Not asking users to pin to a commit or tag.** There are no releases to pin
  to, and pinning converts a copy-based install into a git dependency in the
  consumer's repo — a real cost for a consumer who wants a skill, not a
  submodule. `npx skills update` pulls from the default branch, which is the
  right default for a payload this size.
- **Not a `SessionStart` hook as a *required* install step.** The documented
  hook pattern runs the updater outside the context window and costs no tokens,
  and it is worth *mentioning* as an option. It is host-specific (it was written
  for one host's settings format), it runs a network operation on session start,
  and making it required would mean the install experience depends on a
  mechanism a host may change. Optional and documented, not prescribed.
- **Not chasing a unique name in the registry.** Fourteen entries share the
  `zensical` stem and the name is already taken by several authors. Renaming
  would cost recognisability to fix a collision the ecosystem does not treat as
  one.

**Sequencing.** The install documentation and the project-scope decision are
small, immediate, and independent of anything else in flight. The rest of this
file is a record, not a work item: if a release process ever starts, the version
and manifest questions become real, and the honest default then is a
`skills-lock.json`-style content hash rather than a hand-maintained version
ladder.

---

## 8. Limits of this research

Named, so a later reader knows what to distrust.

- **I did not execute `skills update` or `skills check`.** The claims that
  `check` is a hidden alias for a mutating `update` and that there is no
  `--dry-run` rest on reading the command dispatcher and the help output, not
  on observing a run. The dispatch is unambiguous, but the observation is
  inferred.
- **I did not install this project, so I did not observe what its own install
  writes to disk.** Whether a given flag combination produces a
  `skills-lock.json` in the consumer's repo is inferred from the add/update
  source, not measured here.
- **Registry "maintained?" is unverified for ten of the fourteen entries.** I
  have name, author, and lifetime install count for all of them, and read the
  rendered `SKILL.md` for four. I did not check commit recency, open issues, or
  release activity for any of them; install counts are not a maintenance signal.
- **Addy Osmani's negative is scoped to what I found, not to everything he has
  ever said.** Six of his own documents, his two most substantial blog posts on
  skills, and a targeted search of his site. He may have said something in a
  talk, a podcast, or a social post that I did not surface. The negative is
  "nothing found across these sources", not "he has never said it".
- **The `skillFolderHash` provenance comment says the hash is fetched by the
  telemetry server.** I did not trace the server, and I did not test what
  happens to entries when telemetry is disabled. A user who sets
  `DISABLE_TELEMETRY` may end up with uncheckable global entries; the
  `getSkipReason` function suggests this degrades to a named skip state rather
  than a failure, but I did not verify it.
- **Two cited defects are open issues, not verified current behaviour.** I
  confirmed the issues exist and are open with the quoted text; I did not
  reproduce either against the current release.
- **The registry's discovery and ranking model is described here only from the
  registry owner's own report and one community analysis of the CLI source.**
  I did not independently verify the telemetry-driven-listing claim, and I have
  labelled it accordingly by not relying on it for any recommendation.
- **Only one host is installed and exercised.** Cross-host claims about
  discovery locations come from the CLI's agent table and `agents.ts`, not from
  observing each host load a skill.
- **Comparable-ecosystem analogies in section 3.3 are design reasoning, not
  measurements.** I did not test whether any of those mechanisms actually works
  when transplanted to a runtime-free folder of markdown.

---

## Sources

All checked 2026-09-26.

**Practitioner guidance**

1. <https://addyosmani.com/blog/agent-skills/> — "Agent Skills", 2026-05-03.
2. <https://addyosmani.com/blog/audit-your-agent-files/> — "Audit your Agent
   files", 2026-08-27.
3. <https://github.com/addyosmani/agent-skills> — pack `README.md`.
4. <https://github.com/addyosmani/agent-skills/blob/main/CONTRIBUTING.md> —
   "Reporting Issues" and "Translations".
5. <https://github.com/addyosmani/agent-skills/blob/main/AGENTS.md>
6. <https://github.com/addyosmani/agent-skills/blob/main/docs/adoption-guide.md>
7. <https://github.com/addyosmani/agent-skills/blob/main/docs/getting-started.md>
8. <https://github.com/addyosmani/agent-skills/blob/main/docs/skill-anatomy.md>
9. <https://joost.blog/self-updating-agent-skills/> — "How I made my skills
   update themselves", 2026-04-14, updated 2026-04-18.
10. <https://vercel.com/blog/state-of-agent-skills> — registry scale, 2026-09-25.

**skills.sh CLI** — all at commit
`7407f3893ad4dceab546ac002c3ef806e4000c73` (main, 2026-09-17)

11. `npx -y skills@latest --help` — command surface, executed locally.
12. [`src/cli.ts` L398–L402](https://github.com/vercel-labs/skills/blob/7407f3893ad4dceab546ac002c3ef806e4000c73/src/cli.ts#L398-L402) —
    `check` / `update` / `upgrade` dispatch.
13. [`src/cli.ts` L125, L133, L135](https://github.com/vercel-labs/skills/blob/7407f3893ad4dceab546ac002c3ef806e4000c73/src/cli.ts#L125) —
    help text for `update`, `experimental_install`, `experimental_sync`.
14. [`src/skill-lock.ts` L6–L8, L13–L38, L62–L73, L80–L103, L150–L172](https://github.com/vercel-labs/skills/blob/7407f3893ad4dceab546ac002c3ef806e4000c73/src/skill-lock.ts#L13-L38) —
    global lock shape, path resolution, schema wipe, tree-SHA fetch.
15. [`src/local-lock.ts` L5–L6, L8–L46, L48–L60, L140–L160](https://github.com/vercel-labs/skills/blob/7407f3893ad4dceab546ac002c3ef806e4000c73/src/local-lock.ts#L8-L46) —
    project lock shape, merge-safety notes, local content hash.
16. [`src/update.ts` L186–L204, L213–L241, L244–L260, L592–L593, L638–L643, L775–L782, L987](https://github.com/vercel-labs/skills/blob/7407f3893ad4dceab546ac002c3ef806e4000c73/src/update.ts#L592-L593) —
    skip reasons, recovery command, staleness comparison, `runUpdate`.
17. [`src/install.ts` L9–L17](https://github.com/vercel-labs/skills/blob/7407f3893ad4dceab546ac002c3ef806e4000c73/src/install.ts#L9-L17) —
    `experimental_install` scope.
18. [`src/add.ts` L1029–L1036, L2145–L2156](https://github.com/vercel-labs/skills/blob/7407f3893ad4dceab546ac002c3ef806e4000c73/src/add.ts#L2145-L2156) —
    project lock write sites.
19. [`src/agents.ts`](https://github.com/vercel-labs/skills/blob/7407f3893ad4dceab546ac002c3ef806e4000c73/src/agents.ts) —
    per-host skills directories.
20. <https://github.com/vercel-labs/skills> — `README.md`; agent table,
    install methods, command reference, compatibility matrix.

**Registry data**

21. <https://skills.sh/api/search?q=zensical> — entry list, names, authors,
    install counts.
22. Rendered skill pages read for four entries:
    <https://skills.sh/layeredcraft/skills/zensical-site>,
    <https://skills.sh/kettleofketchup/dotfiles/zensical>,
    <https://skills.sh/brpaz/agent-skills/zensical-setup>,
    <https://skills.sh/zeulewan/claude-code-skills/zensical-development>.

**Open issues (state as of 2026-09-26)**

23. <https://github.com/vercel-labs/skills/issues/1199> — `update` converts
    `--copy` to symlinks; lock lacks an install-mode field. Open.
24. <https://github.com/vercel-labs/skills/issues/371> — `update` failing
    silently under `npx`; linked fixes #432, #487.
25. <https://github.com/vercel-labs/skills/issues/283> — lock-file semantics
    discussion; early description of `check` behaviour that the current
    dispatcher contradicts.
26. <https://github.com/vercel-labs/skills/issues/165> — open proposal for a
    `skills.json` manifest with `integrity` hashes and a content-addressable
    cache.

**Format specification**

27. <https://agentskills.io/specification> and
    [`docs/specification.mdx`](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx) —
    six frontmatter fields; no `version`, manifest, or update channel.

Source 11 was executed locally on 2026-09-26. Sources 12–20 were read at the
pinned commit. Sources 21–22 were fetched live. Sources 23–26 are issue threads
whose text was read; their comments were not exhaustively reviewed. Source 27
was read in full and full-text searched.

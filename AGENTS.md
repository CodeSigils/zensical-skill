# Repository instructions

## Stale-state preflight

Before any implementation, recommendation, or other consequential action,
check whether the repository's instructions, roadmap, research, source
registry, session notes, and target-site state are current and mutually
consistent. Look for uncommitted changes, completed work still described as
pending, superseded decisions, stale versions or commands, and claims that
lack current evidence.

If stale or conflicting state is found, do not silently build on it. Report the
conflict, identify the canonical source, and either reconcile the records first
or clearly label the proposed action as provisional. Re-check volatile
external sources at the point of use. Record the freshness check and any
intentionally unchanged records in the handoff.

### Roadmap after-action gate

For every consequential implementation, research, review, or validation
action, read `docs/roadmap.md` before acting and identify the active phase or
gate it may affect. After the action, reopen the roadmap and compare the
result with that gate. Update the roadmap in the same work session when the
action changes status, evidence, sequencing, scope, or a deferred decision.
If it changes none of those, state explicitly in the handoff that the roadmap
was revisited and intentionally left unchanged. Never leave a completed gate
described as pending, or treat a review-only result as an implementation.

### Documentation freshness contract

Before handing off a meaningful change, perform this small review:

1. Classify affected statements as current claims or dated historical evidence.
2. Search for repeated affected terms, counts, versions, commands, and status
   words such as `current`, `latest`, `deferred`, or `pending`.
3. Compare each current claim with its canonical owner: runtime behavior in
   `zensical/`, user-facing scope in `README.md`, evidence in the registry or
   research record, and sequencing in the roadmap.
4. Revalidate only volatile or decision-critical external facts at the point of
   use, then record corrected, historical, or intentionally unchanged state.

This contract is a focused manual review, not a freshness score, recurring
schedule, or documentation linter. Add automation only after repeated,
observable drift shows that it would remove real maintenance work.

### Runtime distribution contract

The repository's `zensical/` directory is the canonical runtime payload.
Installed copies are distribution artifacts, not a second source of truth. Do
not assume a source commit updates an installed skill or a running host session.

Checking installed-copy freshness is a standing task, not an optional extra.
Before reporting any payload change as done, diff the payload against every
installed copy you can locate on this machine and say plainly which files are
stale. When the user works against an installed copy in the same session,
refreshing it takes priority over finishing other work: a correct source tree
that the active host never loads is not a delivered change. Refresh only the
payload files, never the host's own configuration, and report exactly which
files were copied. When no installed copy is in play, say so once and move on
rather than refreshing speculatively.

## Digital Basement umbrella alignment

When meaningful Zensical-skill work changes its maturity, scope, capability
admission, or relationship to editorial work, also inspect the corresponding
Digital Basement umbrella records when they are available at
`/home/sand/projects/digital-basement/`: `ARCHITECTURE.md`, `ROADMAP.md`,
`docs/editorial-core.md`, and the relevant session note. Reconcile a stale
description in the same session, keeping the editorial core separate from the
Zensical presentation-maintenance skill. If that workspace is unavailable or
the change does not affect the relationship, state that explicitly rather than
inventing a cross-project update.

## Documentation contract

The planning documents under `docs/` describe the skill's intended scope; the
portable runtime payload lives only under `zensical/`. Before changing scope,
workflow boundaries, source evidence, or release expectations, read
`docs/README.md` and the documents required by its reading matrix.

Before handoff, update every affected planning document or state why it remains
unchanged. Search for duplicate guidance and drift between `SKILL.md`,
references, and planning documents before adding a new rule.

Keep `docs/research/current-state.md` current rather than archival: it owns what
the project currently knows to be true, so every claim in it needs a check date.
Keep `docs/research/index.md` as the append-only dated field record: promote
evidence to the current-state file when it informs a decision, move detailed
session chronology to a session note, and never retro-edit a dated entry to
reflect a later finding. Neither file is a graveyard, and a claim that can no
longer be re-checked moves out of current state rather than being refreshed in
place.

### Canonical-owner rule

Every behavioral rule has exactly one owning file. Every other file that needs
the rule links to the owner instead of restating it, so a rule change is one
edit. When two files assert the same rule, one is wrong and the other is a
pointer that has drifted; fix the duplicate rather than reconciling the two
later. Search a claim and count the files that assert it rather than mention it.
This rule governs statements of a rule, not its application. A reference file
that applies a shared principle to its own domain states that application
rather than linking to the owner, because a reference may be read on its own and
a boundary the agent cannot see in the file it is reading is not enforced. Three
payload files each state that a passing build proves less than it appears to,
and that is correct: they bound authorization, verification scope, and media
behavior respectively.

### Meaningful-change documentation directive

After any meaningful change to the skill's scope, workflow, evidence, or
quality criteria, update the relative records in the same work session:

- `README.md` when discoverable scope or user-facing capability changes;
- `docs/vision.md` for boundaries or quality criteria;
- `docs/roadmap.md` for sequencing or acceptance expectations;
- `docs/research/current-state.md` for new evidence or volatile claims, and
  `docs/research/index.md` when the finding is a dated observation rather than
  a current fact;
- the affected `zensical/references/` file for operational detail; and
- the git commit body for a user-visible capability change, which is where
  release-facing history now lives.

If the change produces a durable decision, lesson, finding, or unresolved
question, add a concise session or decision note in the related project and
link it rather than copying the same prose into every file. State explicitly
which records were intentionally unchanged.

For research, inspect the target repository first and consult current official
Zensical documentation before general web search. Use standards bodies or
primary provider sources for accessibility, media, privacy, and embed claims;
label community observations as such and do not treat cached posts or snippets
as evidence.

For link work, evaluate effectiveness separately from existence. Check local
targets and fragments recursively, preserve stable identifiers, distinguish
navigation from semantic relationships, and give each important link a clear
role. Do not add cross-links merely to increase graph density; prefer one
canonical owner and link to it. Use the target site's configured checker when
available, and report external-link freshness separately from local integrity.

### Research-once protocol

Before starting new research, search the existing research record, source
registry, decisions, and session notes. Reuse an existing evidence entry when
its scope and freshness fit the claim. At the point of use, revalidate
volatile, version-sensitive, or decision-critical details rather than trusting
an old snapshot. Record whether evidence was reused, revalidated, superseded,
or newly discovered; do not silently repeat a search or silently carry stale
evidence forward.

### Repeated-value heuristic

During review, notice repeated semantic values as possible duplication or drift
smells. If a version, runner, operating system, path, SHA, feature flag, port,
or similar value is repeated and should change together, recommend a visible,
named canonical source. The count is a signal, not a doctrine: keep incidental
literals, examples, prose, fixtures, and repetition that improves clarity.
Report the evidence and trade-off before extracting anything.

At the end of each roadmap phase, update the roadmap status, acceptance
evidence, exact validation commands and outcomes, source dates, affected links,
and intentionally unchanged planning documents. A phase is not complete until
this documentation gate is satisfied.

Use an imperative commit subject and include these body fields in every commit:

```text
what: Describe the files or behavior changed.
why: Explain the user need, evidence, or design reason.
```

Run `python3 scripts/check_commit_messages.py HEAD` before handoff. To review a
batch, pass a range such as `HEAD~5..HEAD`. The checker enforces a concise
subject plus non-empty `what:` and `why:` fields; add validation details when
they affect confidence or future maintenance.

Do not keep a changelog file. Release-facing history lives in the git commit
body: record user-visible or maintainer-significant changes there, in the
`what:` and `why:` fields the commit policy already requires, and use the
subject line as the one-line summary a reader would have wanted from a release
note. A separate changelog was removed because it duplicated the commit log,
drifted from it, and grew without changing a decision. Research, decisions, and
session notes still hold detailed rationale; use those, not a running list.

### Runtime source-registry boundary

`zensical/references/source-registry.md` is an agent-facing runtime reference,
not an experiment log or target inventory. Keep its rows limited to current
primary-source pointers, review dates or versions, and generic caveats that
change an agent decision. Do not put repository names, local paths, commits,
digests, page counts, or test results in it. Record target-specific observations
and historical evidence in `docs/research/index.md`, `docs/roadmap.md`, or a linked
session note instead.

## Change boundaries

- Keep Zensical-specific implementation separate from editorial voice and
  generic frontend guidance.
- Do not claim a version-sensitive behavior without repository or primary-source
  evidence.
- Do not add tests, scripts, or release automation until a repeated workflow
  makes their value concrete.
- When an authorized edit leaves a focused, validated Git diff, identify it as
  ready to commit and offer that next step. Do not infer commit, push, publish,
  or deployment authorization.
- Do not commit, push, publish, or deploy unless the user authorizes it.

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
Installed copies are distribution artifacts, not a second source of truth. When
a change affects that payload, verify or refresh an installed copy only when
the user requests active-host use or a release/install check requires it;
otherwise report that existing sessions may still use an older copy. Do not
assume a source commit updates an installed skill or a running host session.

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

Keep `docs/research.md` active rather than archival: every entry must have a
current purpose, source/date, or explicit historical disposition. Promote only
evidence that informs a workflow, decision, or roadmap gate; move detailed
session chronology to a session note and mark superseded claims instead of
silently leaving them to drift.

### Meaningful-change documentation directive

After any meaningful change to the skill's scope, workflow, evidence, or
quality criteria, update the relative records in the same work session:

- `README.md` when discoverable scope or user-facing capability changes;
- `docs/vision.md` for boundaries or quality criteria;
- `docs/roadmap.md` for sequencing or acceptance expectations;
- `docs/research.md` and the source registry for new evidence or volatile
  claims;
- the affected `zensical/references/` file for operational detail; and
- `CHANGELOG.md` for a user-visible capability change.

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

Keep `CHANGELOG.md` curated: record user-visible or maintainer-significant
changes, group related work under `Unreleased`, and periodically consolidate it
into release notes. Commit history, research, decisions, and session notes hold
the detailed implementation and rationale; do not mirror every commit in the
changelog.

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

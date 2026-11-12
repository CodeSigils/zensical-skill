# Repository instructions

## Stale-state preflight

Before any implementation, recommendation, or other consequential action,
check whether the repository's instructions, vision, roadmap, research,
source registry, reports, and target-site state are current and
mutually consistent. Look for uncommitted changes, completed work still described as
pending, superseded decisions, stale versions or commands, and claims that
lack current evidence.

If stale or conflicting state is found, do not silently build on it. Report the
conflict, identify the canonical source, and either reconcile the records first
or clearly label the proposed action as provisional. Re-check volatile
external sources at the point of use. Record the freshness check and any
intentionally unchanged records in the handoff.

## Research map

- [docs/research/current-state.md](docs/research/current-state.md) holds
  current, review-dated decisions.
- [docs/research/index.md](docs/research/index.md) holds dated field
  observations and applications.
- [docs/reports/](docs/reports/) holds completed audits and implementation
  records.

Use [docs/README.md](docs/README.md) to select the smallest relevant record
set.

### Roadmap after-action gate

For every consequential implementation, research, review, or validation
action, read [docs/roadmap.md](docs/roadmap.md) before acting and identify the
active phase or gate it may affect. After the action, reopen the roadmap and compare the
result with that gate. Update the roadmap in the same work session when the
action changes status, evidence, sequencing, scope, or a deferred decision.
If it changes none of those, state explicitly in the handoff that the roadmap
was revisited and intentionally left unchanged. Never leave a completed gate
described as pending, or treat a review-only result as an implementation.

At the end of each roadmap phase, update the roadmap status, acceptance
evidence, exact validation commands and outcomes, source dates, affected links,
and intentionally unchanged planning documents. A phase is not complete until
this documentation gate is satisfied.

### Documentation freshness contract

Before handing off a meaningful change, perform this small review:

1. Classify affected statements as current claims or dated historical evidence.
2. Search for repeated affected terms, counts, versions, commands, and status
   words such as `current`, `latest`, `deferred`, or `pending`.
3. Compare each current claim with its canonical owner: runtime behavior in
   [zensical/](zensical/), user-facing scope in [README.md](README.md),
   boundaries and quality criteria in [docs/vision.md](docs/vision.md),
   evidence in the registry or research record, and sequencing in the roadmap.
4. Revalidate only volatile or decision-critical external facts at the point of
   use, then record corrected, historical, or intentionally unchanged state.

A claim search finds statements that exist and are wrong. It cannot find an
entry that should exist and does not. When a change adds or removes an item in
an enumerated surface, check every surface that enumerates that inventory. The
router in [zensical/SKILL.md](zensical/SKILL.md) and the `## Current scope`
list in [README.md](README.md) are a matched pair: a new or removed route
needs a matching scope bullet in
the same change. The `How to use it` table in `README.md` is a curated sample
of common asks, so it gains a row only when the change introduces a task a
user would name by request.

This contract is a focused manual review, not a freshness score, recurring
schedule, or documentation linter. Add automation only after repeated,
observable drift shows that it would remove real maintenance work.

### Runtime distribution contract

The repository's [zensical/](zensical/) directory is the canonical runtime
payload. Installed copies are distribution artifacts, not a second source of
truth. Do not assume a source commit updates an installed skill or a running
host session.

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
[docs/README.md](docs/README.md) and the documents required by its reading
matrix.

Before handoff, update the canonical owner and only the planning records whose
current claim actually changed. For a consulted record that plausibly appears
affected but is intentionally unchanged, say so in the handoff. Search for
duplicate guidance and drift between [zensical/SKILL.md](zensical/SKILL.md),
references, and planning documents before adding a new rule.

Keep [docs/research/current-state.md](docs/research/current-state.md) current
rather than archival: it owns what the project currently knows to be true, so it
carries an overall review date and gives a claim its own date when its freshness
differs from that review. Keep [docs/research/index.md](docs/research/index.md)
as the append-only dated field record: promote evidence to the current-state
file when it informs a decision, move detailed session chronology to a session
note, and never retro-edit a dated entry to reflect a later finding. Neither
file is a graveyard, and a claim that can no longer be re-checked moves out of
current state rather than being refreshed in place.

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
quality criteria, update the canonical owner and then only the applicable
records in the same work session:

- [README.md](README.md) when discoverable scope or user-facing capability
  changes;
- [docs/vision.md](docs/vision.md) for boundaries or quality criteria;
- [docs/roadmap.md](docs/roadmap.md) for sequencing or acceptance expectations;
- [docs/research/current-state.md](docs/research/current-state.md) for new
  evidence or volatile claims, and [docs/research/index.md](docs/research/index.md)
  when the finding is a dated observation rather than a current fact;
- the affected [zensical/references/](zensical/references/) file for operational
  detail;
- [docs/reports/](docs/reports/) for a completed audit, migration, or
  implementation whose method and evidence deserve a durable record beyond a
  dated index entry, registered in the dated reports table in
  [docs/README.md](docs/README.md); and
- the git commit body for a user-visible capability change, which is where
  release-facing history now lives.

Do not add a second summary merely because a record was consulted. If a change
produces a durable decision, lesson, finding, or unresolved question, add one
concise dated record and link it rather than copying the same prose into every
file. Capture is part of the change and does not wait for a separate
instruction. An audit, migration, or implementation with reusable evidence is
not finished until its record exists. State the intentionally unchanged records
only when their omission would otherwise be surprising.

### Research-once protocol

Before starting new research, search the existing research record, source
registry, decisions, and reports. Reuse an existing evidence entry when
its scope and freshness fit the claim. At the point of use, revalidate
volatile, version-sensitive, or decision-critical details rather than trusting
an old snapshot. Record whether evidence was reused, revalidated, superseded,
or newly discovered; do not silently repeat a search or silently carry stale
evidence forward.

### Research sources

For research, inspect the target repository first and consult current official
Zensical documentation before general web search. Use standards bodies or
primary provider sources for accessibility, media, privacy, and embed claims;
label community observations as such and do not treat cached posts or snippets
as evidence.

### Link work

For link work, evaluate effectiveness separately from existence. Check local
targets and fragments recursively, preserve stable identifiers, distinguish
navigation from semantic relationships, and give each important link a clear
role. Do not add cross-links merely to increase graph density; prefer one
canonical owner and link to it. Use the target site's configured checker when
available, and report external-link freshness separately from local integrity.

### Repeated-value heuristic

During review, notice repeated semantic values as possible duplication or drift
smells. If a version, runner, operating system, path, SHA, feature flag, port,
or similar value is repeated and should change together, recommend a visible,
named canonical source. The count is a signal, not a doctrine: keep incidental
literals, examples, prose, fixtures, and repetition that improves clarity.
Report the evidence and trade-off before extracting anything.

Use an imperative commit subject and include these body fields in every commit:

```text
what: Describe the files or behavior changed.
why: Explain the user need, evidence, or design reason.
```

Run `python3 scripts/check_commit_messages.py HEAD` before handoff. To review a
batch, pass a range such as `HEAD~5..HEAD`. The checker enforces a subject of
at most 72 characters plus non-empty `what:` and `why:` fields; add validation
details when they affect confidence or future maintenance.

Do not keep a changelog file. Release-facing history lives in the git commit
body: record user-visible or maintainer-significant changes there, in the
`what:` and `why:` fields the commit policy already requires, and use the
subject line as the one-line summary a reader would have wanted from a release
note. A separate changelog was removed because it duplicated the commit log,
drifted from it, and grew without changing a decision. Research records,
decisions, and reports still hold detailed rationale; use those, not a running
list.

### Runtime source-registry boundary

[zensical/references/source-registry.md](zensical/references/source-registry.md)
is an agent-facing runtime reference, not an experiment log or target
inventory. Keep its rows limited to current
primary-source pointers, review dates or versions, and generic caveats that
change an agent decision. Do not put repository names, local paths, commits,
digests, page counts, or test results in it. Record target-specific observations
and historical evidence in [docs/research/index.md](docs/research/index.md),
[docs/roadmap.md](docs/roadmap.md), or a completed report in
[docs/reports/](docs/reports/) instead.

### Local check contract

Every script under `scripts/` and `zensical/scripts/` returns the same three
codes, so a caller can tell a finding from a broken environment without parsing
prose: `0` clean, `1` findings, `2` the check could not run. A check must not
exit `1` for an environmental problem, and must not let a subprocess failure
escape as a traceback. When adding a check, follow the existing scripts rather
than inventing a new convention.

Before handoff, run the check that covers what changed: `bash
scripts/run_scenarios.sh` for payload rendering or scenario-environment
changes, `python3 scripts/check_readme_inventory.py` after a payload tree
change, `python3 zensical/scripts/check_instruction_contract.py --self-test`
after an instruction change, and `bash zensical/scripts/check_site_hygiene.sh
.` before a commit.

### Separate environmental failure from repository failure

Before treating a failed command as a finding about the repository, rule out the
reviewer's own environment: an unavailable network, an unwritable temporary
directory, a missing binary, or a sandbox restriction. Compare the configured CI
workflow before concluding the repository is at fault. Report a command that
could not run as an environment limit, not as a defect, and do not spend
another pass retrying the same unavailable capability.

### Review budget

Default to one discovery pass and one post-fix verification pass. The
verification pass checks the applied fixes and looks for regressions the fixes
introduced. Continue past those two only when verification exposes a new,
concrete behavioral risk. Do not repeat an unchanged review to seek more
confidence: reasoning that changed no decision belongs in the commit body, the
same rule the documentation admission gate applies to new documents.

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

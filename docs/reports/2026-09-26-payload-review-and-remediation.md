# Payload review and remediation (2026-09-26)

Date: 2026-09-26 10:40 EEST
Status: The findings below were produced by a review-only pass and have since
been remediated in the same session. This record is the after-action report,
not a plan. Two items are deliberately left open for the maintainer: the
installed-copy sync strategy and the documentation ratio.

## Why this record exists

A review of the whole repository, not just the payload, was run before any
change was made. It read every file in `zensical/`, all four scripts, the CI
workflow, the fixtures, and the planning documents, and it executed the full
validation gate rather than assuming it worked. Nine findings came out of it,
one of which was serious enough to change what the skill is allowed to claim.

The review was read-only. `docs/roadmap.md` was read first, as the roadmap
after-action rule requires, and was left unchanged at that point because a
review is not an implementation. It was updated later, when remediation began.

## The finding that mattered

`docs/roadmap.md` said: "Keep feeds deferred. The current Zensical
compatibility roadmap lists RSS as planned, so no native-feed workflow is
admitted without upstream support." The same claim appeared in `docs/vision.md`,
`README.md`, `docs/research/index.md`, and `zensical/references/source-registry.md`.

Zensical shipped a native `rss` plugin in `0.0.65` on 2026-09-24. The
deferral's own escape clause had fired and nobody noticed.

This was worse than ordinary staleness. The deferral was a *decision*, and
the decision was justified by a premise that had become false. In the payload
the claim was also a **negative capability** claim — "Do not claim native feed
generation" — so an agent reading it would actively refuse a valid user
request rather than merely stay silent.

The root cause is worth recording. The 2026-09-24 version-drift work correctly
collapsed the version *pin* to one canonical source, but it treated "version"
as a repeated literal to be deduplicated. It never asked which **decisions**
had been justified by the old version. The feeds gate was exactly such a
decision, so the `0.0.60` → `0.0.64` bump sailed straight past it.

The general lesson: deduplicating a fact does not re-examine the arguments
built on top of it.

## What else the review found

| # | Finding | Severity |
| --- | --- | --- |
| 1 | Feeds asserted "planned" in five files, including as a negative capability in the payload | High |
| 2 | Target-specific content leaked into the portable payload: `source-registry.md` rows carried a target's observed version, and `accessibility.md` named a specific repository inside a code-anchor caveat | High |
| 3 | Version baseline five releases stale; a scheduled breaking boundary (`0.1.0`, announced for 2026-11-05) appeared nowhere in the payload | Medium |
| 4 | A fixture's own revisit trigger had fired and nothing happened: `scenarios.md` says to revisit the code-anchor fixture when the pinned version changes, and the pin moved | Medium |
| 5 | Fixture coverage was asymmetric — two of four fixtures assert the runner's own logic or a config choice rather than Zensical behaviour | Medium |
| 6 | `CHANGELOG.md` was a single `## Unreleased` bucket with 35 flat bullets and no release ever cut | Low |
| 7 | Structural defects in the research record: an orphaned heading with no body, and an undated entry resting on the word "latest" | Low |
| 8 | Two scripts had real defects: a field-presence test that disagreed with its own extraction, and a duplicated assertion loop | Low |
| 9 | The installed copy at `~/.codex/skills/zensical` was stale in six files | Low |

Findings 2 and 6 deserve a note on how they happened. The source-registry
boundary — the registry holds pointers, dates, and generic caveats, never
target observations — was written into `AGENTS.md` and restated in the
changelog at the time. The payload then violated it. Tightening a rule in
writing does not tighten it in the file the rule governs.

## What changed

**The feeds gate is gone, and feeds are admitted.** The false premise was
removed from all five files. `docs/vision.md` now records feeds as an admitted
bounded capability. `docs/roadmap.md` deferral item 5 now covers authoring,
i18n, and theme authoring instead, and the revision history records why.

**The payload gained `references/rss.md`.** It is routed from `SKILL.md`,
named in the capability-admission paragraph, and listed as a component that
commonly needs care. It covers the version gate, both config syntaxes, what
the plugin generates, the discovery-link requirement, the Git-date behaviour,
and the limits worth stating before a user commits — including that
`match_path` cannot express exclusions.

**Target-specific content was removed from the payload.** The registry rows
dropped their observed-version clauses; `accessibility.md`'s code-anchor caveat
now describes observed behaviour generically and tells the reader to verify it
on the target version. Both findings cleared in one pass, because the stale
version literal and the boundary violation were the same text.

**Two upstream behaviours were added** because they change what an agent
should check: the `0.0.63` exclusion of dot-prefixed files from built output,
recorded in `media.md`, and the pre-`1.0` release channel, recorded as a new
source-registry row. Neither appeared in the payload before.

**`CHANGELOG.md` was deleted.** Release-facing history now lives in commit
bodies, in the `what:` and `why:` fields the commit policy already required.
The rationale is recorded in `AGENTS.md`. The file was removed because it
duplicated the commit log, drifted from it, and grew without changing a
decision — it was 124 lines after a week of work and no release had ever been
cut from it. Dated historical records that mention it were left as they were.

**The scenario pin moved to `0.0.65`** and the local environment was re-synced,
because `run_scenarios.sh` cross-checks the pin against the installed version.

**The installed copy was refreshed**, and the runtime distribution contract in
`AGENTS.md` was rewritten so that checking installed-copy freshness is a
standing part of reporting a payload change, not an optional courtesy.

**Two repository scripts were hardened, and one new fragility was found while
verifying them.** `check_commit_messages.py` had a presence test that matched
the field name anywhere in the body while extraction required the name to start
a line, so a commit that merely mentioned `what:` mid-sentence was reported as
having an empty field. It also read the subject and body as one string, which
let a subject satisfy a body field, and it would surface a raw git traceback on
an unresolvable ref. All three are fixed, and the awkward single-`HEAD` case is
now explicit: a bare `HEAD` must mean one commit, because `git log HEAD` would
otherwise walk all of history and fail on older commits that predate the policy.

`run_scenarios.sh` had two tab-label loops checking the same thing with
different casing, and both passed only because the fixture contains both
casings. It also had an error branch for an unreadable version pin that could
never run, because `set -e` killed the script at the assignment first. Fixing
that exposed a third defect: a relative `ZENSICAL_BIN` was resolved after the
script had already changed directory, so the documented invocation failed with
a missing-file error even though the binary existed. The path is now made
absolute at the point of assignment.

**CI gained a concurrency group, per-job timeouts, and a job that runs the two
payload checks.** The payload scripts were already written, already bounded,
and already passing locally, but nothing ran them automatically; wiring them in
is finishing existing automation rather than adding new. The shallow checkout
in the scenario job is deliberate and is now commented, because the same
default depth produced a real date bug in a target repository this session.

## How the admitted capability was verified

Admission required primary-source evidence and a real target, per the
capability-admission rule. Both were obtained.

Primary source: `0.0.65` was installed into a scratch environment and its
configuration parser read directly. That established what the plugin accepts,
what it rejects, and what it ignores — including two settings that are
accepted and then discarded, and the fact that `date_from_meta` must be a
mapping rather than a boolean. The compatibility page was also read, and it
lists `rss` under supported plugins. Upstream publishes no dedicated feeds
guide, which is precisely why the payload needs its own reference file.

Real target: the maintainer's live blog was upgraded to `0.0.65`, feeds were
enabled, and the output was inspected. That produced the discovery-link
requirement, the `length` cap behaviour, and the `match_path` limitation, none
of which are documented upstream.

### A defect the local build could not have found

The first deployment succeeded and the feed was live with all 19 items. The
dates were wrong: every entry claimed to be published on the deploy date.

`use_git` defaults to true, so item dates come from Git history, and
`actions/checkout` defaults to a depth of one commit. CI could date the newest
commit and silently dated everything else to the build. A shallow clone
reproduced the symptom exactly, which confirmed the cause. Fetching full
history fixed it, and the live feed now carries 13 distinct real dates spanning
April to September 2026.

The lesson was written back into `references/rss.md`. The reference already
warned about a checkout with no Git history, but shallow CI checkouts are what
every hosted build actually does, and that case had no actionable remedy.

## What was deliberately not done

**No `VERSION.md` was created.** It was proposed as the fix for the drift. It
was rejected because it would have reintroduced the exact problem the 2026-09-24
work closed: a second hand-edited location for a value that already has one
canonical owner. There is also no single version to record. Two different
things are tracked — the version the fixtures validate against, and the version
each registry row was last checked against, which is a per-row date rather than
a global constant. The drift lived entirely in the second.

**No feed fixture was added.** Admission required a bounded validation path,
and the live target supplied the evidence. A synthetic RSS fixture would assert
the runner's own logic, which is the weakness finding 5 already identified.

**No version-freshness automation was added.** The roadmap defers it, and the
defence is a dependency manifest rather than a new mechanism. If it is ever
built, `.github/dependabot.yml` is the natural home; it currently covers
GitHub Actions only.

**The live blog's `origin` was not changed silently.** Pushing a workflow-file
change over HTTPS was rejected because the active token lacks workflow scope.
A one-off SSH push delivered the fix without altering repository
configuration, and the durable fix was left to the maintainer.

## Limits of this record

The upstream behaviour cited here was verified on `0.0.65` specifically.
Zensical is pre-`1.0` and announces `0.1.0` for 2026-11-05, after which
configuration semantics may change without a deprecation cycle.

The RSS findings come from one target site. The plugin's behaviour on a
different content shape, or with front-matter dates, was not exercised.

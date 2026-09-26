# Documentation mechanism: from a size limit to a duplication rule (2026-09-26)

Date: 2026-09-26 11:20 EEST
Status: records a decision about maintainer documentation and the mechanism
that replaces the previous one. No payload behavior changed. Committing and
pushing the repository were authorized separately.

## Why this record exists

The previous session adopted a documentation admission rule and then, in the
same session, added 983 lines of new documentation to a 963-line markdown
payload: a 787-line research file and a 196-line remediation report. The rule
was satisfied rather than broken, which is the more useful failure. Its third
ground admitted anything "required by an external constraint", and a user
request for research was treated as exactly that. Asking for something is a
preference, not a constraint, so any agent could clear the bar by noting the
topic came up.

The rule also had no notion of size, so 787 lines was never a violation.

This record exists to state the replacement mechanism and the evidence behind
it, so the next reader inherits a decision rather than rediscovering the
problem.

## The diagnosis: the ratio is a symptom

Maintainer documentation is 4152 lines across 15 files. The runtime payload is
1130 lines, of which 972 are markdown across 11 files. That is roughly 3.7 to 1.

The tempting conclusion is to consolidate. The evidence says otherwise. Every
serious finding this project has recorded was a duplication failure, not a size
failure:

| Finding                                    | The duplicate that drifted                                                        |
| ------------------------------------------ | --------------------------------------------------------------------------------- |
| RSS deferral asserted on a false premise   | the deferral's premise was restated in 5 files; the version bump passed all of them |
| Target observation inside the payload      | a target-specific claim was asserted in `accessibility.md` and in 3 registry rows   |
| `0.0.60` reached an agent                  | one version literal, 4 files, none owning it                                       |

In each case a rule was stated in more than one place, no file owned it, and a
change to one copy did not reach the others. Rewriting files to reduce the ratio
would not have prevented any of them.

The 2026-09-24 version-drift fix already demonstrated the correct mechanism: it
collapsed the version pin to a single canonical location, and the pin has not
drifted since. What it did not do is apply the same treatment to decisions. The
pin was a fact with an obvious owner. The feeds deferral was a decision, and no
file owned the premise it rested on, so the bump sailed past it.

Deduplicating a fact does not re-examine the arguments built on top of it.

## What replaced the admission rule

Three mechanisms, stated in full in `docs/roadmap.md` and `AGENTS.md`.

**Canonical-owner rule.** Every behavioral rule has exactly one owning file.
Every other file that needs the rule links to the owner rather than restating
it, so a rule change is one edit. This is the mechanism that would have caught
all three findings above, and it is mechanically checkable: search a claim and
count the files that assert it rather than mention it.

**Expiry rather than a size limit.** Every maintainer document carries a
`Reviewed <date>` marker. A document that has not been re-checked against
primary sources and that no current decision depends on has expired and should
be archived rather than refreshed. The harm this project actually suffered was
stale claims reaching an agent, not volume. Expiry is also self-limiting in a
way a ceiling is not: a document nobody needs stops being updated, which is what
makes its own obsolescence visible.

**Split by audience, not subject.** Agent-facing content must be current and
canonical; history must be append-only and never retro-edited. A single file
cannot be both, because a dated record cannot be refreshed and a current fact
cannot stay append-only. `docs/research/index.md` was doing both jobs at once.

## The split, as the first test of the rule

`docs/research/index.md` held 957 lines and 43 top-level sections. Six were
undated current-state material; the rest were dated field observations. The
undated six moved to `docs/research/current-state.md` (107 lines), which now
owns current facts and carries the review date. The field record kept its name
and its 37 dated sections, because every existing citation wanted the evidence
rather than the current state, and renaming it would have churned 27 references
to point at the same content.

The two files now state their own jurisdiction: the field record says it is
evidence and must not be consulted for what is true now, and the current-state
file says a claim that can no longer be re-checked moves out rather than being
refreshed in place.

The split is deliberately low-churn. It relocates six sections and rewires the
references that meant current state; the references that meant dated evidence
were already correct and were left alone.

## A carve-out the rule needed on first application

Applying the rule to the payload immediately produced a false positive worth
recording, because the naive form of the rule would have damaged the payload.

Searching for rules stated in more than one file returned three payload
references claiming that a passing build proves less than it appears to. Two
different readings were possible. The first treats them as duplicates to be
collapsed into one owner. The second treats them as one principle applied to
three domains, which is what they are: `SKILL.md` bounds authorization, since a
successful build is not deploy permission; `validation.md` bounds verification
scope, since static output is not hosting, DNS, or cache behavior; and
`media.md` bounds media claims, since a passing build does not prove a player
loads. Collapsing them would have removed a boundary from a file an agent might
read alone, which is the failure the payload is designed to prevent.

The rule therefore governs statements of a rule, not its application. A
reference file that applies a shared principle to its own domain states that
application rather than linking to the owner. Both `AGENTS.md` and the roadmap
record this, and the next audit should apply it before collapsing anything.

## Deliberately not built

- **No line-count ceiling.** It measures volume rather than duplication and
  relocates growth under the limit rather than preventing it.
- **No ratio gate in CI.** Same reason, and a ratio that can be gamed is worse
  than no gate because it reads as a control.
- **No mechanism aimed at a single past instance.** Machinery built to prevent
  one occurrence is the failure this section exists to stop. A single judgment
  call belongs to the reviewer.
- **No consolidation pass.** The largest files are dated evidence that is still
  load-bearing, and rewriting it would cost more than it returns. The split
  addresses the same mass more cheaply because it separates the two audiences
  rather than rewriting either.

## The freeze, restated honestly

The freeze on new governance documents stands, and it is a default rather than
a gate. The previous revision of this section could be satisfied by noting that
the user had asked for research; this one cannot, because the canonical-owner
rule and the expiry marker both apply to an existing document as readily as to a
new one. A request for research justifies extending the owner of the relevant
subject, which is what happened to the six relocated sections.

## Limits of this record

This measures documentation volume and attribution, not whether any documented
decision was correct. The canonical-owner rule has been applied to the research
files and the reading matrix in this change; it has not yet been audited across
the whole repository, and duplicate statements of the same rule may remain in
`docs/vision.md`, `docs/roadmap.md`, and the runtime payload. That audit is
real work and is not claimed here.

The expiry marker is recorded in `AGENTS.md` and required by
`docs/release-checklist.md`, but only `docs/research/current-state.md` carries a
`Reviewed` marker today. The remaining maintainer documents acquire one when
they are next re-checked against primary sources, not in bulk.

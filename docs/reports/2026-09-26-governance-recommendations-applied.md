# Documentation recommendations applied (2026-09-26)

Date: 2026-09-26 14:20 EEST
Status: Records the application of four documentation recommendations. No
payload behavior changed, and no commit, push, publication, or deployment is
authorized by this record.

## Why this record exists

The governance-mechanism report in this directory recorded a set of
duplication and staleness findings. Applying its own canonical-owner rule to
the rule that motivated it produced a further audit, which found four more
problems of the same kind. All four are now fixed. This record states what the
audit measured, what changed, and what was verified, so the numbers can be
re-checked rather than taken on trust.

It is a new record rather than an edit to the governance-mechanism report
because that report is dated evidence of what the audit found. Rewriting it
would destroy the finding it exists to preserve, and this repository does not
retro-edit dated reports.

## What the audit measured

| Problem                                                           | Measurement                                                                     |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| The capability-admission rule was restated, not owned              | 10 wordings across 7 files, 4 of them inside `roadmap.md` itself                 |
| The expiry model had no data to expire on                           | 14 of 15 maintainer documents carried no review marker                           |
| The source registry governed nothing                                | `SKILL.md` cited it 3 times; all 10 reference files cited it 0 times              |
| Documentation link defects                                          | 1 broken relative link and 3 reports reachable from nowhere                      |
| Payload files with version-sensitive claims and no recorded check  | 4 files, last touched 2026-09-09 to 2026-09-13                                   |

The audit also produced two false positives that were deliberately left
alone. A `skill-feedback.md` reference in `skill-structure-conventions.md` is
an example inside a directory-tree block describing another project's layout,
not a link to this one. A `../index.md` link in the base-path fixture is the
fixture's own subject. Correcting either would have broken working evidence.

## What changed

### The admission rule gained one owner

`docs/roadmap.md` `## Capability-admission rule` is now the single statement.
It carries an explicit ownership note recording why the runtime payload keeps
its own wording: an agent may read `SKILL.md` without the roadmap.

The other statements became one-clause links. Restatements of the conditions
fell from 10 to 2, the canonical list and the payload copy. Nine pointer
locations across six maintainer documents now resolve to the owner.

The audit missed one instance. `research/editorial-voice.md` already pointed at
the rule while still restating two of its conditions inline, which a search for
the conditions' wording did not surface. It was fixed with the rest.

### Review markers were standardized and given coverage

Four conventions for one concept were reduced to two. Documents under review
carry `Reviewed:`; dated reports keep `Date:`, because a report's date records
when it was written and reports are never retro-edited.

Eight payload references gained a footer recording a verification that had
happened but been written down nowhere:

> Reviewed 2026-09-26 against Zensical 0.0.65. Re-check the matching row in
> [source-registry.md](source-registry.md) before relying on a version-sensitive
> detail here.

Two were excluded. `article-review.md` makes no Zensical behavior claim at all
and is version-independent, so a version date would imply a dependency that does
not exist. `source-registry.md` is the registry and already carries a stronger
per-row check date.

The registry pointer in that same footer is what closed the third finding. The
registry can now reach the files that make the claims it records, so a stale
row has somewhere to propagate.

### Link defects were closed

The broken relative link in the 2026-09-24 implementation report was
corrected. The three orphaned reports were made reachable through an index in
`docs/README.md` that names each one and says what it is for, because the
roadmap links the `reports/` directory and no individual report was findable.

### README drift was corrected

A separate stale sweep against the README found six further defects: the
payload tree omitted the feeds reference, the payload file count was 13 when it
is 14, the repository map omitted two research documents, the routing table had
no feeds row, the CI description named two checks when there are three jobs, and
the opening restated the admission rule in a fourth wording. All six were fixed
in the same session.

The opening was the same class of defect the admission-rule fix addressed, in
the most-read file in the repository. A rule that is restated in the first
paragraph a visitor reads is not owned anywhere.

## What was verified

- Restatements of the admission-rule conditions: 10 to 2.
- All 9 pointer locations resolve; the anchor matches the real heading.
- Relative-link audit across every touched document: no broken links.
- Orphan report count: 3 to 0.
- Review markers: 3 `Reviewed:` in maintainer documents, 6 `Date:` in reports,
  and no remaining `Last reviewed:` anywhere.
- Payload inventory re-counted from the index rather than trusted: 14 files,
  10 references, 5 research documents.
- Commit policy, instruction-contract self-test, site hygiene, and the four-fixture
  scenario suite on Zensical 0.0.65 all pass.

## Deliberately not done

No consolidation pass over the research record. The mass is dated evidence that
is still load-bearing, and rewriting it would cost more than it returns.

No version field was added to the payload. The agent specification has no
version field and no update channel, so a value in frontmatter would be
maintainer trivia shipped to every target repository, and the audit already
rejected a separate version file for the same reason.

No new enforcement mechanism was built. A line-count ceiling measures volume
rather than duplication, and a ratio gate in CI reads as a control while
measuring the wrong thing.

## Limits of this record

The cross-repository canonical-owner audit was not performed. The payload scan
that produced the carve-out covered this repository's ten reference files, not
the sibling repositories whose documents describe the same boundaries.

The measurements here are a point-in-time count, not a maintained score. They
are recorded so a later reader can tell whether the same search still finds the
same duplication, and a search that now returns nothing is evidence the fix
held rather than evidence the problem was never real.

This record does not claim that documentation duplication is solved. It claims
that four measured instances are fixed and that the mechanism to find the next
one is a search rather than an argument.

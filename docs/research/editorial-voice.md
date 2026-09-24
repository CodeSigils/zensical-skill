# Editorial voice and machine-typical prose research

Created: 2026-09-24. Status: supporting evidence for the portable prose-tell
guidance in [article-review](../../zensical/references/article-review.md). This
file records external findings only; it does not define a house voice for the
skill. Community tooling and blog observations are labelled as such.

## Why this record exists

A maintainer request asked for a broader catalogue of machine-typical prose
patterns ("AI tells") and a discussion of how others work toward a more human
editorial voice. No prior human-voice research entry existed in this
repository, so this file was created. The findings justify the expanded
checklist bullet in the article-review reference and stay out of the runtime
source registry because they are community observations, not primary Zensical
sources.

## What the tell catalogues converge on

Several independently maintained open catalogues of machine-typical prose
agree on the same pattern families (community tooling, reviewed 2026-09-24):

- **Negative-antithesis inversions** — "It was not X. It was Y.", "Not just
  X, but Y", "It's not about X, it's about Y". The `crypdick/unslop`
  taxonomy calls the not-just-X construction "almost pathognomonic of AI
  writing"; the `wernerkasselman-au/llm-tips` style policy cites a
  Washington Post analysis (Merrill et al., 13 Nov 2025) finding such
  variants in about 6% of a large July 2025 ChatGPT message sample, and
  caps them at one per 2,000 words.
- **Opener and closer tics** — "Here's the thing", "Imagine...", "Let's
  dive in", "In this article...", "Picture this", "At its core", "In
  conclusion", "Without further ado".
- **Filler hedges** — "It's worth noting", "That said", "At the end of
  the day", "It goes without saying".
- **Manufactured reveal punctuation** — colon-heavy and em-dash-heavy
  constructions, artificial suspense ("Here's what blew my mind", "The
  crazy part?"), and stacked rhetorical questions ("The result?
  Devastating.").
- **Formulaic scaffolding** — rule-of-three abuse, "First... Second...
  Third...", symmetrical bullet runs, uniform paragraph length, and
  paragraph-end summaries.
- **Lexical and grammatical markers** — a focal-word cluster (delve,
  tapestry, pivotal, robust, seamless, leverage, harness) and copula
  avoidance ("serves as", "stands as", "features" for "is" or "has"),
  plus present-participle padding tails ("...highlighting the need for
  further research").

Anchor reference: Wikipedia's descriptive
[Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
project page (verified URL 2026-09-24; note it is a Wikipedia project page,
not an article). It explicitly frames these as "potential signs of a problem,
not the problem itself" and states that one or two watched words may be
coincidental — density across an edit is the signal. The `style_policy.toml`
community policy attributes frequency claims to Juzek & Ward (COLING 2025),
Kobak et al. (2024), and Brown et al. (2025); those originals were not
re-verified here and are recorded as second-hand citations.

## The density rule

Every catalogue repeats the same caveat: a single flagged word or one
three-item list proves nothing. The signal is clusters, repetition, and
mismatch with the surrounding voice. Quoted phrases, titles, and code where a
watched phrase is under discussion rather than used must be left alone, and
accurate uncertainty must be preserved. One practitioner formulation: "Don't
mangle a sentence or delete real information just to purge one banned word."

## Detection tools

An overview of detection methods and tool classes — SciSpace's
[How to Detect AI-Generated Writing](https://scispace.com/resources/how-to-detect-ai-generated-text-methods-tools/)
(2025-09-26, verified link 2026-09-24) — pairs commercial detectors with
linguistic red flags and fact-checking as complementary checks. Popular
detector homepages verified live on 2026-09-24:

- [GPTZero](https://gptzero.me) — free AI-content detector aimed at
  educators, with writing-quality feedback and human-verification replay.
- [Originality.ai](https://originality.ai) — accuracy-focused detector
  used by content teams, with free scans and Chrome/Google Docs
  integration.
- [Copyleaks](https://copyleaks.com) — enterprise content-authenticity
  platform spanning text, code, and video.
- [Winston AI](https://www.winston.ai) — commercial detector positioned at
  editors and publishers.
- [Turnitin](https://www.turnitin.com) — academic-integrity platform whose
  AI-writing detection ships with originality checking.
- [Sapling](https://sapling.ai/ai-content-detector) — free per-text
  probability score for AI-generated content.
- [Writer](https://writer.com/ai-content-detector/) — enterprise AI
  platform offering a detector alongside agent tooling.

The triage caveat above applies to all of them: per-sentence signals beat
whole-document scores, and false positives on technical human writing are
repeatedly reported. A detector verdict is a reason to look closer, not a
conclusion.

## How others keep a human editorial voice

Reported practices from editorial teams and newsroom standards (community
observers unless noted; reviewed 2026-09-24):

- **Named human accountability.** The Associated Press newsroom standards
  update (July 2026, as reported) permits AI for headline ideation,
  summarization, transcription, and grammar work while keeping reporting,
  sourcing, and verification human, with every AI output reviewed by a
  journalist. The EU AI Act's rules, as described in the same reporting,
  turn on a person or organisation taking editorial responsibility.
- **First-hand artifacts.** Quality-checklist advice (Vantaige, 2026-07-15)
  requires each draft to contain at least one fact only the team could
  produce — a test result, metric, screenshot, or real-project observation —
  tying human voice to experience rather than phrasing.
- **Editing passes over rewrites.** Practitioner checklists edit in layers:
  cut filler, vary sentence rhythm by reading aloud, replace formal
  transitions or delete them, add concrete numbers instead of "many" or
  "most", and allow genuine false starts or self-corrections that show
  thinking in progress (`antislop.io` editor's checklist, 2026-04-22). The
  same source warns that fake anecdotes make copy less credible and that
  adding fake slang or hype to "sound human" is its own tell.
- **The coffee test.** "Would you say this to a colleague over coffee?"
  replaces detector-chasing as the pass/fail question (`antislop.io`).
- **Numeric pre-publish gates used sparingly.** One published pipeline (Metaflow
  CV-5 gate, 2026-06-16) checks sentence-length variance, em-dash density,
  tell-pattern matches, filler counts, and readability before publishing,
  while stating that "manual burstiness edits beat detector-chasing
  rewriters" and that a high detector score does not mean the post sounds
  like the company.
- **Detectors as triage only.** Multiple observers note detector false
  positives on technical human writing; per-sentence signals beat whole-document
  scores, and the goal is a knowledgeable reader finding the piece useful,
  not passing a detector.

## Strategies and popular skills for more human prose

The remedy advice repeats across the sources above: judge density rather
than single words; edit in layered passes (word choice, rhythm, transition
style, specificity, thinking patterns); read drafts aloud and vary sentence
starts; add first-hand facts only the team could produce; keep genuine
false starts and uncertainty; never fake slang, typos, hype, anecdotes, or
confidence; treat load-bearing contrasts as legitimate; and prefer one
flowing sentence over a period-stopped inversion.

Popular humanizing skills encoding similar rules (repos verified live via
GitHub on 2026-09-24; community-maintained, not audited here):

- [`jalaalrd/anti-ai-slop-writing`](https://github.com/jalaalrd/anti-ai-slop-writing)
  — a Claude Code and universal SKILL.md that eliminates statistically
  detectable AI writing patterns.
- [`crypdick/unslop`](https://github.com/crypdick/unslop) — a Claude Code
  plugin that detects and rewrites AI-sounding text as a human copyeditor
  would.
- [`drunkrhin0/antislop`](https://github.com/drunkrhin0/antislop) — two
  SKILL.md writing skills for human-style output.
- [`haidrrrry/humanize-ai-writing`](https://github.com/haidrrrry/humanize-ai-writing)
  — a free anti-AI-slop system prompt and skill covering ChatGPT, Claude,
  Gemini, Grok, and Kimi.
- [`stephenturner/grampan`](https://github.com/stephenturner/grampan) — an
  in-browser LLM cliché highlighter (one self-contained HTML page) that
  marks sentences matching known tells.
- [`eric-sabe/slop-lint`](https://github.com/eric-sabe/slop-lint) — a
  zero-dependency CLI that fails on the em-dash and warns on other LLM
  tells, with a corpus harness for discovering new ones.
- [`wernerkasselman-au/llm-tips`](https://github.com/wernerkasselman-au/llm-tips)
  — evidence-based writing notes and tooling for high-signal prose; its
  policy file cites an authority for each rule.

Which to prefer: `drunkrhin0/antislop` is the most style-preserving of the
set because it builds in exception discipline (load-bearing contrasts are
not violations; one flagged word is not proof), which makes it the best
primary choice. `jalaalrd/anti-ai-slop-writing` is the most complete
catalogue and a solid baseline, but heavier-handed. `wernerkasselman-au/llm-tips`
is the most evidence-grounded when calibrating why a rule exists.
`stephenturner/grampan` and `eric-sabe/slop-lint` are triage tools —
paste-and-check highlighting, never verdicts. Apply any of them at
sentence level with the density rule: a skill is a lens, not a gate.

## Transferable implications for this skill

1. The article-review reference can name pattern families as portable,
   opt-in suggestions when the user asks for a more human style — never as
   a gate, house voice, or automatic rewrite, consistent with
   [vision](../vision.md).
2. Density and voice-mismatch are the judgment criteria; single instances
   are not evidence, and quoted or discussed phrases are out of scope.
3. Human voice in practice comes from accountability, first-hand specifics,
   and layered editing — not from sprinkling imperfections. The skill keeps
   voice and substantive editorial judgment with the target repository's
   own policy and the user.

## Adopted guidance (2026-09-24)

After inspecting the cloned skills above, three light behavioral ideas were
adopted into the runtime article-review reference — framing, not new tell
lists:

- Over-correction guard — from `crypdick/unslop` ("Avoid over-correction",
  "Unslop ≠ minimize", "Preserve voice and register"): removing connectives,
  flattening register, or deleting structure that serves the content can read
  worse than the tell it removed. Pair it with "rewrite, don't just swap
  words."
- Authority precedence — from `drunkrhin0/antislop` `profiles.md` and
  `preservation-contract.md`: target's published rules, then the user's
  explicit instruction, then a supplied sample, then defaults; a sample lends
  style traits only, never facts or experiences.
- Second-generation "performed authenticity" tells — from
  `wernerkasselman-au/llm-tips` §5.14: philosophical mic drops, forced casual
  asides, and invented informality, the overshoot when prose is pushed to
  "sound human."

Deliberately not adopted: absolute bans, numeric gates and risk scores, and
bundled detector scripts — they conflict with the portable, opt-in,
non-gating boundary in [vision](../vision.md).

## Real-world audit pass (2026-09-24)

The installed `drunkrhin0/antislop` lens (registry 3.0.0) was run in audit
mode over a published article (`agent-instruction-drift.md`, 978-word prose
body) to inspect behavior, not to gate. Its Formulaic Writing Risk Score was
92/100; the only scored findings were four em-dashes from its zero-em-dash
house rule. Vocabulary and phrase rules produced no false positives, and
output integrity was clean.

Two conclusions:

- The lens is precise on clean, specific prose: it invented no findings and
  left the article's load-bearing contrast and quoted terms alone.
- Its absolute formatting rule conflicts with our house style. The four
  em-dashes are legitimate, so under antislop's own `over-correction` status
  they are not defects. This confirms the decision not to adopt absolute
  bans.

Adopted from the pass: a light, density-based dash preference rather than a
ban. The article-review reference now suggests keeping dash density low and
reserving em-dashes for genuine asides, since a dash that only joins two
clauses usually reads the same with a comma or a period.

## Second review pass: coverage check (2026-09-24)

A checklist pass with the article-review guidance was run over a second
published article (`agent-memory-surfaces.md`, 1,291-word prose body), this
time applying the tell families as a coverage list instead of reading only
the lens output.

- Dash density: about eleven body em-dashes (roughly one per 117 words),
  mostly joining two clauses or opening an appositive — the case the
  dash-density guidance targets. Four or five could become a comma, colon,
  or period.
- `comprehensive` (line 51) is on the antislop forbidden list but used
  precisely, in a deliberate contrast with "well-understood"; optional.
- The five-beat anaphora and "Nothing preserves *why*." are deliberate and
  on-voice; keep.
- The antithesis / inversion family: no period-stopped reveals. Only inline
  `X, not Y` contrasts, all load-bearing (a map not a benchmark; words not
  understanding; position not just size). One, "it records what was said,
  not what was understood", was softened to "it keeps the words and loses
  the understanding behind them" for consistency.

Coverage lesson: the first pass over this article reported only the lens's
scored findings and missed the inversion family until asked. A pass should
walk every tell family in the article-review checklist and report each as
found or none, so omissions are visible. This is a review-procedure
observation, not yet a change to the runtime guidance; the editorial charter
asks for several observations before a process rule changes.

## Structured passes: memory-surfaces and awesome-list (2026-09-24)

Two published articles were combed with the same two-lens workflow: first the
installed `drunkrhin0/antislop` audit lens, then the article-review tell
families walked as a coverage list, plus the dash-density guidance and the
target's editorial charter.

`agent-memory-surfaces.md` (1,288-word prose body; 11 body em-dashes, about
one per 108 words):

- antislop: Formulaic Writing Risk Score about 80/100. The scored items were
  the em-dashes and one `comprehensive` (line 52), used precisely against
  "well-understood". No banned phrases, no opener, filler, copula, or
  participle tells, output integrity clean.
- Tell families: no period-stopped inversions; four load-bearing inline
  `X, not Y` contrasts (map not benchmark; words not understanding; snapshot
  not the system; position not just size). No stacked questions, opener tics,
  or filler hedges. A few natural tricolons (preferences/corrections/identity;
  versions/links/APIs).
- Target guidance: point of view present, examples real and linked with
  reasons, one admonition used as a signpost, reflective close.

`agent-maintained-awesome-list.md` (2,241-word prose body; 22 body em-dashes,
about one per 100 words):

- antislop: Formulaic Writing Risk Score about 86/100. The scored items were
  the em-dashes only. No banned vocabulary or phrases, output integrity clean.
- Tell families: no period-stopped inversions; one load-bearing "not because
  X, but because Y" (line 243); benign "rather than" and "instead of". One
  single rhetorical question as a section lead (line 140). No opener tics or
  filler hedges. The closing three-part parallel ("whether its checks fail
  closed...; whether its state files...; and whether its freshness ritual...")
  is the closest thing to a formulaic three-part list.
- Target guidance: concrete real-repository examples with annotated links,
  visible judgement, honest framing, one admonition.

## Emerging patterns and voice suggestions (2026-09-24)

Across the three Agent-Work notes (drift 92/100; memory about 80/100;
awesome-list about 86/100):

1. Dash density is the only recurring scored item. Every article sits near one
   em-dash per 100-120 words; the lens flags all of them and our light
   guidance targets the clause-joining ones. This is the one place worth
   spending editing effort.
2. No false positives anywhere. The lens never invented a vocabulary, phrase,
   opener, filler, copula, or participle finding on our prose; its only
   over-fire is the absolute em-dash rule.
3. Load-bearing contrasts recur and are legitimate. Inline `X, not Y` is a
   house habit, not a tell, and stays protected.
4. Punchy short declaratives ("Nothing preserves *why*.", "And false
   confidence compounds.") are deliberate and unflagged.
5. Structural uniformity is the emerging voice risk. All three notes share the
   same skeleton: an opening hook, body sections, a `!!! tip` near the close, a
   "## What I look for now" three-item list, "## Related reading", and a
   reflective last line. The editorial charter names repeated headings and
   predictable callout placement as a uniformity smell, so this is the pattern
   to watch.

Suggestions for the voice guidance (proposals, not yet adopted):

- Vary the closing shape. The "## What I look for now" plus three-item formula
  has now appeared three times; the next article should close differently or
  drop it.
- Vary or omit the admonition when it is not a genuine signpost, rather than
  placing one near the close by habit.
- Treat dash density as a soft target (roughly under one em-dash per 150
  words) and prefer a comma or colon for a dash that only joins two clauses.
- Keep walking every tell family and reporting each as found or none, so the
  pass stays complete.

## How the downloaded skills approach the problem (2026-09-24)

Detail behind the ranking above — each skill's actual method, read from the
cloned checkouts (community tooling, reviewed 2026-09-24):

- `drunkrhin0/antislop` — a mode-routed system. It declares an activation
  boundary (prose artifacts only; not code, config, data, or facts), then
  routes between a writing mode and an audit mode. Audit mode produces a
  Formulaic Writing Risk Score out of 100 with a violations table and a
  separate output-integrity check, and states plainly that it cannot prove AI
  authorship. Its load-bearing ideas are its rules precedence (voice wins,
  structure outranks word swaps, positive guidance outranks a single ban), its
  preservation contract (a Draft/Revise/Audit/Transform edit-authority model
  that forbids strengthening claims or certainty beyond the source), and its
  `over-correction` status for cases where applying a rule would flatten valid
  voice. Its heavy parts are the score, the large reference and eval payload,
  and its absolute zero-em-dash rule.
- `crypdick/unslop` — a copyeditor's process. It keeps strong exception
  discipline ("Unslop ≠ minimize"; "a single em dash in a paragraph is fine"),
  rewrites rather than swapping words, and runs a private second pass. Its
  maxims are concrete editing moves (say it straight, name actors and
  mechanisms, let things be small, use "is" and "has", cut scaffolding, do not
  hedge-stack, let paragraphs breathe). Its heavy part is a bundled Python
  detector.
- `jalaalrd/anti-ai-slop-writing` — a prescriptive directive. It carries a
  large banned list, punctuation quotas, structural bans, a "what to do
  instead" section, and an explicit voice-calibration step ("match *their*
  voice"). The calibration idea is adoptable; the absolute bans and quotas are
  the heavy, over-firing parts.
- `wernerkasselman-au/llm-tips` — an evidence-cited policy. Each rule names an
  authority, and its §5.14 names the second-generation tells that appear when
  prose is pushed to "sound human" (philosophical mic drops, forced casual
  asides). Its numeric gates and absolute bans are the heavy parts.

## Adoptable without heavy lifting

The ideas worth taking are framing and edit discipline, not tooling:

| Idea | Source | Why it is cheap |
|---|---|---|
| Preservation contract — keep claims, facts, quotes, numbers, attribution; never strengthen certainty | antislop | A rule about what not to change; no payload |
| Rules precedence — voice > structure > word choice | antislop | Three lines; already implied by target-guidance-first |
| "Rewrite, don't swap words" | unslop | One instruction; prevents cosmetic edits |
| Over-correction guard | unslop | One instruction; already adopted |
| Voice calibration — match the author's register | anti-ai-slop-writing | Already the authority-precedence rule |
| Performed-authenticity tells | llm-tips | One tell family; already adopted |

Deliberately left out (heavy lifting for little gain): risk scores, numeric
gates, absolute bans, bundled detector scripts, and large reference or eval
payloads.

## Using a lens without replacing the author's voice

The line between "a lens" and "a rewriter" is the whole point:

- Follow the target repository's published rules first, then the user's
  instruction, then a supplied sample, then defaults.
- Treat every finding as a candidate, reported with
  `severity | path | evidence | reader impact | suggestion | validation`; the
  author decides.
- Judge density, not single instances; leave quoted, titled, and load-bearing
  material alone.
- Never add slang, typos, or invented personality to "sound human."
- Keep the lens optional and sentence-level; it is a second opinion, never a
  gate or an automatic rewrite.

## Possible separate editorial-voice skill (proposal, not decided)

A lightweight `editorial-voice` skill could wrap the best community lens plus
the portable principle above, so the capability travels to repositories that
are not Zensical sites. It would stay a thin orchestrator: read the target's
guidance, optionally load an installed lens, apply the density rule and
preservation contract, and report suggestions without rewriting. It must not
reimplement tell lists or impose a house voice, or it duplicates the seven
community skills already recorded here. Per the capability-admission rule it
still needs a bounded fixture and a named owner, so this is flagged as a
future decision, not adopted.

## Runtime guidance promoted (2026-09-24)

Two procedural ideas from this research were promoted into the runtime
article-review reference, because they change how a review is conducted rather
than adding another tell list:

- **Voice-profile step** — before flagging anything, name the voice traits worth
  keeping (formality, rhythm, punctuation habits, and whether warmth or humor is
  genuine) from the draft and any supplied sample, and state them in the report.
  This makes "honor and improve" actionable; it borrows the voice-calibration
  idea from `jalaalrd/anti-ai-slop-writing` and the sample-lends-traits-only rule
  from `drunkrhin0/antislop`.
- **Coverage line** — walk every tell family and report each as found or none.
  This promotes the coverage lesson recorded after the second review pass, where
  the antithesis family was missed until it was asked about.

The runtime reference stays a compact principle; exhaustive tell lists remain in
the installed lens and in this file.

## Fourth published-article pass: Oh My OpenAgent Guide (2026-09-24)

The optional article-review workflow was tested against the Code Sigils
`oh-my-opencode-guide.md` (title: "Oh My OpenAgent Guide"), a 1,463-word
technical decision guide. Target guidance describes the desired voice as calm,
practical, curious, and human; the pass identified that profile before making
any findings.

The tell-family coverage was clean: no stacked rhetorical questions, opener
tics, filler hedges, formulaic three-part clusters, copula avoidance,
present-participle padding, or performed-authenticity tells. The article's
inline negative contrasts are load-bearing decision criteria, so they stayed.
The installed `drunkrhin0/antislop` checkout at `c65cd6b` still surfaced its
absolute em-dash rule; most dashes were annotated link descriptions, and the
two sentence-internal dashes fit the target's voice. They were correctly
treated as an `over-correction`, not a cleanup target.

The pass produced three small maintenance edits rather than a rewrite:

- Replaced the vague claim that a large MCP catalogue consumes "significant
  context" with OpenCode's concrete warning that it can exceed the context
  limit.
- Replaced six redirecting `developers.openai.com/codex/` links with their
  canonical `learn.chatgpt.com/docs/` destinations.
- Updated the article's review date after revalidating the upstream project,
  its installation guide, OpenCode's MCP documentation, and the redirected
  Codex pages.

This is evidence that the voice-profile and coverage-line additions work as
intended: they preserve a strong target voice, make no tell-family omission
invisible, and let factual/link maintenance emerge separately from style.
It does not justify another runtime change or a scoring gate.

## Sources

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
  — descriptive detection field guide (primary descriptive source).
- SciSpace, "How to Detect AI-Generated Writing: 6 Methods to Spot AI
  Text" (2025-09-26) — detection-methods overview (verified link
  2026-09-24).
- Detector homepages: GPTZero, Originality.ai, Copyleaks, Winston AI,
  Turnitin, Sapling, Writer — commercial tooling; links verified
  2026-09-24, accuracy claims not independently tested.
- Humanizing-skills repositories: `jalaalrd/anti-ai-slop-writing`,
  `crypdick/unslop`, `drunkrhin0/antislop`, `haidrrrry/humanize-ai-writing`,
  `stephenturner/grampan`, `eric-sabe/slop-lint`,
  `wernerkasselman-au/llm-tips` — community writing skills; repositories
  verified live 2026-09-24.
- `crypdick/unslop` `ai-writing-patterns.md`, `stephenturner/grampan`,
  `eric-sabe/slop-lint`, `wernerkasselman-au/llm-tips`
  `tools/style_policy.toml`, `jalaalrd/anti-ai-slop-writing`,
  `drunkrhin0/antislop`, `haidrrrry/humanize-ai-writing` — community tell
  catalogues (reviewed 2026-09-24; not independently audited).
- Donatas Simkus, "How to Tell If Content Is AI-Written (And How to Fix
  It)" (2026-03-27) — density rule formulation.
- Vantaige, "AI Content Quality Control" (2026-07-15); Metaflow, "The CV-5
  Editorial Gate" (2026-06-16); `antislop.io`, "An Editor's Checklist"
  (2026-04-22); Proven Media Solutions (2026-02-27); Orwellix 12-step
  checklist (2026-08-02); Mohab Abdelkarim, "The Authenticity Audit"
  (2026-09-16) — practitioner/editorial-voice guidance (community).

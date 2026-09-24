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

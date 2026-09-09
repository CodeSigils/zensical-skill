# Repository instructions

## Documentation contract

The planning documents under `docs/` describe the skill's intended scope; the
portable runtime payload lives only under `zensical/`. Before changing scope,
workflow boundaries, source evidence, or release expectations, read
`docs/README.md` and the documents required by its reading matrix.

Before handoff, update every affected planning document or state why it remains
unchanged. Search for duplicate guidance and drift between `SKILL.md`,
references, and planning documents before adding a new rule.

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

At the end of each roadmap phase, update the roadmap status, acceptance
evidence, exact validation commands and outcomes, source dates, affected links,
and intentionally unchanged planning documents. A phase is not complete until
this documentation gate is satisfied.

Use an imperative commit subject and include these body fields in every commit:

```text
what: Describe the files or behavior changed.
why: Explain the user need, evidence, or design reason.
```

## Change boundaries

- Keep Zensical-specific implementation separate from editorial voice and
  generic frontend guidance.
- Do not claim a version-sensitive behavior without repository or primary-source
  evidence.
- Do not add tests, scripts, or release automation until a repeated workflow
  makes their value concrete.
- Do not commit, push, publish, or deploy unless the user authorizes it.

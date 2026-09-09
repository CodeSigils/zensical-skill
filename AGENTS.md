# Repository instructions

## Documentation contract

The planning documents under `docs/` describe the skill's intended scope; the
portable runtime payload lives only under `zensical/`. Before changing scope,
workflow boundaries, source evidence, or release expectations, read
`docs/README.md` and the documents required by its reading matrix.

Before handoff, update every affected planning document or state why it remains
unchanged. Search for duplicate guidance and drift between `SKILL.md`,
references, and planning documents before adding a new rule.

## Change boundaries

- Keep Zensical-specific implementation separate from editorial voice and
  generic frontend guidance.
- Do not claim a version-sensitive behavior without repository or primary-source
  evidence.
- Do not add tests, scripts, or release automation until a repeated workflow
  makes their value concrete.
- Do not commit, push, publish, or deploy unless the user authorizes it.

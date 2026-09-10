# Release and discoverability checklist

This checklist applies only when the project has a configured public remote
and a reviewed release candidate. A local build or a catalog listing is not a
release guarantee.

## Preconditions

- [ ] `LICENSE` is present and the runtime `SKILL.md` declares the same license.
- [ ] `SECURITY.md` describes private reporting and payload boundaries.
- [ ] `CHANGELOG.md` records the user-facing change.
- [ ] `docs/vision.md`, `docs/roadmap.md`, and `docs/research.md` reflect the
      release scope and current evidence.
- [ ] The source registry has current primary-source dates and version caveats.
- [ ] No credentials, generated output, agent runtime state, or private data is
      included in the payload.

## Local validation

- [x] Run the official Agent Skills validator from a clean environment using
      the pinned command below; record the exact commit and result.

      `uvx --from git+https://github.com/agentskills/agentskills.git@69ef37e9424c0a7ea9dd2293b559e43ec8176379#subdirectory=skills-ref skills-ref validate zensical`

      Result (2026-09-09): `Valid skill: zensical`.
- [ ] Check relative references and front matter.
- [ ] Run `bash zensical/scripts/check_site_hygiene.sh .` and resolve or
      explicitly review any candidate before release.
- [ ] Run `python3 scripts/check_commit_messages.py <release-range>` and verify
      every commit has a concise subject plus non-empty `what:` and `why:`
      fields.
- [ ] Keep `CHANGELOG.md` limited to user-visible or maintainer-significant
      changes; detailed rationale belongs in commits and research/decision
      records.
- [ ] Review repeated semantic values (versions, runners, OS names, paths,
      SHAs, ports, and feature flags) as possible duplication/drift smells;
      centralize only when the values should change together and the trade-off
      improves clarity.
- [ ] Apply the accessibility reference to affected media, components, CSS,
      templates, or landing pages; record browser/assistive-technology limits.
- [ ] Run the shared locked scenario/fixture suite.
- [ ] Review the final payload tree and confirm only `zensical/` is distributed.
- [ ] Record unresolved network, version, rendering, or deployment uncertainty.

## Host compatibility

Verify from clean, project-scoped temporary directories. Do not install into a
working repository and do not infer one host's behavior from another.

| Host     | Evidence required                                                  | Status                      |
| -------- | ------------------------------------------------------------------ | --------------------------- |
| Codex    | Skill is discoverable and all referenced files are present         | Pass (project-scoped smoke) |
| OpenCode | Documented skill directory is recognized and references resolve    | Pass (project-scoped smoke) |
| Hermes   | Documented external directory is recognized and references resolve | Pass (project-scoped smoke) |

Record the host, source commit, CLI/tool version, observed installation path,
command output, and cleanup result. Host checks should be small discovery and
file-availability checks; they should not duplicate the behavioral suite.

Smoke result (2026-09-10): an isolated temporary root was populated with the
portable `zensical/` payload at each documented host path: `.agents/skills/zensical`
for Codex, `.opencode/skills/zensical` for OpenCode, and `.hermes/skills/zensical`
for Hermes. Each copy had a non-empty `SKILL.md` and resolved
`references/site-inspection.md` and `references/validation.md`. The temporary
root was removed after the checks; no live host skill directory was changed.

## skills.sh and market discoverability

Treat skills.sh or another marketplace as a distribution index, not a quality
authority. Before announcing discoverability:

- [x] Confirm the canonical repository and payload path are publicly resolvable.
- [x] Verify the provider's current install command and agent identifiers from
      its documentation; do not copy cached commands.
- [x] Run a clean, project-scoped install using the current documented command.
- [x] Confirm the `zensical` skill is listed and its complete referenced tree is
      present.
- [x] Record the provider response, source commit/ref, CLI version, and any
      unauthenticated or stale-catalog limitation.
- [ ] Do not claim “featured”, “verified”, or “supported” from ranking or
      install counts alone.

If the provider cannot be queried or the canonical path is stale, report
discoverability as pending and do not install or recommend the package.

Current evidence (2026-09-10): Skills CLI `1.5.25` ran the documented command
`npx --yes skills add CodeSigils/zensical-skill --skill zensical --agent codex
--copy --yes` in an isolated temporary directory. It cloned public
`CodeSigils/zensical-skill` at `main` ref `23de5a7d01de6467133976cfd9c968b9f7404a6c`,
found one skill, and copied `zensical` to `.agents/skills/zensical`. The full
runtime tree was present: `SKILL.md`, `agents/openai.yaml`, nine references, and
`scripts/check_site_hygiene.sh`; the temporary directory was removed. A broad
`npx --yes skills find zensical` query still returned related third-party
skills without surfacing this repository. Direct source installation is
verified; Skills.sh search indexing and public release claims remain pending.

## Release handoff

The handoff must include the source ref, validation commands and outcomes,
host matrix, marketplace status, known limitations, and the next review trigger
(for example, a Zensical upgrade or provider contract change). GitHub Releases,
semver tags, and CI automation are optional until the manual process becomes a
demonstrated bottleneck.

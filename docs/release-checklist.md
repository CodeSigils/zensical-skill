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

- [ ] Run the official Agent Skills validator (`skills-ref validate zensical`)
      from a clean environment using a source pinned to an immutable
      `agentskills/agentskills` commit; record the exact commit and result.
- [ ] Check relative references and front matter.
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
- [ ] Run the shared scenario/fixture suite once it exists.
- [ ] Review the final payload tree and confirm only `zensical/` is distributed.
- [ ] Record unresolved network, version, rendering, or deployment uncertainty.

## Host compatibility

Verify from clean, project-scoped temporary directories. Do not install into a
working repository and do not infer one host's behavior from another.

| Host | Evidence required | Status |
| --- | --- | --- |
| Codex | Skill is discoverable and all referenced files are present | Pending |
| OpenCode | Documented skill directory is recognized and references resolve | Pending |
| Hermes | Documented external directory is recognized and references resolve | Pending |

Record the host, source commit, CLI/tool version, observed installation path,
command output, and cleanup result. Host checks should be small discovery and
file-availability checks; they should not duplicate the behavioral suite.

## skills.sh and market discoverability

Treat skills.sh or another marketplace as a distribution index, not a quality
authority. Before announcing discoverability:

- [ ] Confirm the canonical repository and payload path are publicly resolvable.
- [ ] Verify the provider's current install command and agent identifiers from
      its documentation; do not copy cached commands.
- [ ] Run a clean, project-scoped install using the current documented command.
- [ ] Confirm the `zensical` skill is listed and its complete referenced tree is
      present.
- [ ] Record the provider response, source commit/ref, CLI version, and any
      unauthenticated or stale-catalog limitation.
- [ ] Do not claim “featured”, “verified”, or “supported” from ranking or
      install counts alone.

If the provider cannot be queried or the canonical path is stale, report
discoverability as pending and do not install or recommend the package.

## Release handoff

The handoff must include the source ref, validation commands and outcomes,
host matrix, marketplace status, known limitations, and the next review trigger
(for example, a Zensical upgrade or provider contract change). GitHub Releases,
semver tags, and CI automation are optional until the manual process becomes a
demonstrated bottleneck.

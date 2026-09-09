# Discovery evidence

This record captures a bounded external discovery check. It is evidence of
what the provider returned at one time, not a permanent catalog snapshot.

## Skills CLI Zensical query (2026-09-09)

Command, run from an isolated temporary directory after explicit authorization:

```bash
npx --yes skills find zensical
```

Observed status: successful. The CLI displayed 21 results, including these
Zensical-related candidates:

- `layeredcraft/skills@zensical-site` (9 installs)
- `xcode-nlp/kodaskills@koda-zensical` (4 installs)
- `kettleofketchup/dotfiles@zensical` (3 installs)
- `brpaz/agent-skills@zensical-setup` (2 installs)
- additional setup, authoring, customization, and debugging candidates

The query surfaced candidates that the earlier local/direct-source discovery
pass missed. Each serious candidate still requires canonical repository,
revision, license, payload-path, and complete-reference inspection. Install
counts and result ordering are retrieval signals only.

## Dependency boundary

`npx` and the Skills CLI are optional discovery-time tools. They are not runtime
dependencies of `zensical-skill`, are not required to inspect or validate a
target site, and should not be added to the payload's package dependencies.
Because `npx --yes` downloads and executes external code, use it only with
explicit authorization and an isolated working directory. If unavailable,
report the provider as unavailable and continue with canonical source-host
search rather than silently bootstrapping it.

## Limits

- The provider did not expose a stable full-catalog total in the CLI output;
  “21 results” means results displayed by this invocation.
- Results and install counts can change; rerun the query before a release or
  recommendation.
- This record does not certify candidate quality, safety, compatibility, or
  marketplace indexing for `CodeSigils/zensical-skill`.

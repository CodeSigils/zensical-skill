# Site inspection

Use this reference when orienting yourself in a Zensical repository or when
the requested change may affect more than one source file.

## Inspect first

- `pyproject.toml`, `uv.lock`, `requirements.txt`, or other dependency files
- `zensical.toml` and any compatibility or theme configuration
- `docs/` content tree and section indexes
- navigation declarations and generated-site settings
- theme overrides, CSS, JavaScript, and static assets
- `.github/workflows/` or other build/deployment automation
- repository `AGENTS.md`, README, and local check scripts

## Questions to answer

1. What command builds the site, and where does it write output?
2. Which file is the canonical source for navigation?
3. How are article metadata and section landing pages represented?
4. Which Zensical version is declared or installed?
5. Does CI build, validate links, or deploy on a specific path change?
6. Are there local rules about article style, admonitions, tabs, or index links?

Record uncertainty rather than inferring a Zensical convention from a different
site or from a cached example.

## Deployment-instruction drift

When a repository documents deployment in `AGENTS.md` and uses
`.github/workflows/docs.yml`, compare the documented trigger paths and build
commands with the workflow before a deployment-sensitive change. The bundled
check covers the observed lockfile-backed Zensical contract without reading or
printing secrets:

```bash
python3 scripts/check_instruction_contract.py /path/to/site
```

It checks only the conventional `docs.yml` layout and skips repositories that
do not have both files or a `## Deployment` section. A failure is a
documentation-drift finding, not proof that the workflow itself is broken.

## Sensitive-material preflight

Before an authorized commit, publish, or deployment action in a Git repository,
run the bundled check from the skill directory:

```bash
bash scripts/check_site_hygiene.sh /path/to/site
```

It checks tracked paths for common secret-bearing names and tracked content for
a small set of high-confidence private-key and token signatures. It prints only
candidate paths and finding types, never matched values. A nonzero result means
stop and ask the maintainer how to proceed; do not add a secret to `.gitignore`
and call the exposure fixed, rotate credentials, rewrite Git history, or bypass
GitHub protection without explicit authorization.

This is a bounded preflight, not a comprehensive secret scanner. It does not
scan ignored or untracked files, Git history, provider dashboards, generated
deployment artifacts, or every secret format. A real exposure needs provider
rotation/revocation before any history-removal plan. See GitHub's
[secret-scanning guidance](https://docs.github.com/en/code-security/concepts/secret-security/secret-scanning)
and [sensitive-data removal guidance](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository).

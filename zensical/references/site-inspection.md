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

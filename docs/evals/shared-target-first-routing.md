# Shared target-first routing evals

Reviewed: 2026-11-23

These are lightweight activation/boundary scenarios for the shared target-first
routing contract. They are maintainer review aids, not runtime instructions,
automation, or proof of model behavior. Run them as manual prompt reviews when
changing `zensical/SKILL.md`, routed reference links, or routing boundaries.

## Positive: inspect before choosing a reference

**Prompt:** "The tabs on my Zensical docs page look broken after I edited the
Markdown. Can you fix them?"

**Expected behavior:**

- Establish scope and authority before editing; confirm the target repository
  and whether edits are authorized.
- Perform a bounded target scan: inspect relevant config, the affected page,
  existing tab conventions, and target build commands before selecting a fix.
- Frame one affected outcome (the broken tabs/rendered tab surface), not a
  site-wide audit.
- Reuse target records, then load only the smallest relevant reference set
  (typically `site-inspection` context already gathered plus
  `content-components`/`validation` as needed).
- Make the smallest coherent change, validate proportionately, and report the
  validation boundary: build verifies generation, rendered inspection verifies
  affected presentation, neither verifies deployment or indexing.

**Failure signal:** agent jumps directly to generic tab syntax advice or edits
without target inspection/authorization.

## Boundary: ordinary prose request does not activate Zensical maintenance

**Prompt:** "Can you rewrite this paragraph to sound clearer and more
confident?"

**Expected behavior:**

- Do not activate the Zensical maintenance workflow merely because the file may
  live in a docs site.
- Treat as ordinary prose editing unless the user explicitly asks for
  Zensical/site maintenance, component validation, build/render checks, or
  target-repo governed article review.
- If context suggests a Zensical article review may be relevant, ask or state
  the boundary briefly; do not load site-maintenance references by default.

**Failure signal:** agent performs site inspection, loads Zensical references,
or runs/build-checks without a Zensical maintenance request.

## Boundary: deployment claim stays separate

**Prompt:** "The site builds locally, so can you confirm it's deployed and
indexed?"

**Expected behavior:**

- Report that local build/rendered checks verify generation/presentation only.
- Do not claim deployment, hosting, crawler access, or search-engine indexing
  without separate authorized evidence.

**Failure signal:** agent treats a clean build as deployment/indexing proof.

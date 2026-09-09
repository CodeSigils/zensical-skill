#!/usr/bin/env bash
set -euo pipefail

expected_version="0.0.60"
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
fixture_root="$repo_root/tests/fixtures"
run_root="$(mktemp -d "${TMPDIR:-/tmp}/zensical-skill-scenarios.XXXXXX")"
trap 'rm -rf "$run_root"' EXIT

zensical_bin="${ZENSICAL_BIN:-}"
if [[ -n "$zensical_bin" ]]; then
  actual_version="$($zensical_bin --version | awk 'NR == 1 { print $NF }')"
  [[ "$actual_version" == "$expected_version" ]] || {
    printf 'Expected Zensical %s; found %s from %s\n' "$expected_version" "$actual_version" "$zensical_bin" >&2
    exit 1
  }
  run_build() {
    local fixture="$1"
    local output="$2"
    local work="$run_root/$(basename "$fixture")-work"
    cp -a "$fixture" "$work"
    (cd "$work" && "$zensical_bin" build --clean)
    cp -a "$work/site" "$output"
  }
else
  if ! command -v uv >/dev/null 2>&1; then
    printf 'uv or ZENSICAL_BIN is required to run the pinned scenarios\n' >&2
    exit 2
  fi
  run_build() {
    local fixture="$1"
    local output="$2"
    local work="$run_root/$(basename "$fixture")-work"
    cp -a "$fixture" "$work"
    local log="$run_root/$(basename "$fixture")-uv.log"
    if ! (cd "$work" && UV_CACHE_DIR="$run_root/uv-cache" uv run --project "$work" zensical build --clean) >"$log" 2>&1; then
      cat "$log" >&2
      if rg -qi 'pypi|dns|network|fetch|resolution' "$log"; then
        printf 'Environment blocked dependency acquisition; rerun with ZENSICAL_BIN or restore package access.\n' >&2
        exit 2
      fi
      printf 'Zensical fixture build failed; see the diagnostic above.\n' >&2
      exit 1
    fi
    cat "$log"
    cp -a "$work/site" "$output"
  }
fi

for fixture in tabbed-site accessibility-site base-path-site; do
  printf '%s: Zensical %s build\n' "$fixture" "$expected_version"
  run_build "$fixture_root/$fixture" "$run_root/$fixture-output"
done

tab_output="$run_root/tabbed-site-output/index.html"
for label in npm pnpm Yarn Bun; do
  rg -F "$label" "$tab_output" >/dev/null
done
tab_count="$(rg -o 'data-tabs="[^"]+"' "$tab_output" | wc -l)"
if [[ "$tab_count" -lt 1 ]]; then
  printf 'tabbed-site: no rendered tab group found\n' >&2
  exit 1
fi
printf 'tabbed-site: rendered tab group with all four alternatives\n'

a11y_output="$run_root/accessibility-site-output/index.html"
if ! rg -F '<iframe ' "$a11y_output" >/dev/null; then
  printf 'accessibility-site: iframe fixture missing from output\n' >&2
  exit 1
fi
if rg -P '<iframe\b(?:(?!title=)[^>])*>' "$a11y_output" >/dev/null; then
  printf 'accessibility-site: expected iframe-title finding is reproducible\n'
else
  printf 'accessibility-site: fixture no longer reproduces missing-title finding\n' >&2
  exit 1
fi

base_output="$run_root/base-path-site-output/index.html"
if rg -F 'href="about/"' "$base_output" >/dev/null && [[ -f "$run_root/base-path-site-output/about/index.html" ]]; then
  printf 'base-path-site: generated relative link resolves under /docs deployment path\n'
else
  printf 'base-path-site: generated link lost configured deployment path\n' >&2
  exit 1
fi

printf 'PASS: Zensical scenario builds, rendered tabs, a11y finding, and base-path link assertions\n'

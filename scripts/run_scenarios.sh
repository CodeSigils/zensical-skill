#!/usr/bin/env bash
set -euo pipefail

expected_version="0.0.60"
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
fixture_root="$repo_root/tests/fixtures"
scenario_root="$repo_root/tests/scenario-env"
run_root="$(mktemp -d "${TMPDIR:-/tmp}/zensical-skill-scenarios.XXXXXX")"
trap 'rm -rf "$run_root"' EXIT

count_iframes_missing_titles() {
  python3 - "$1" <<'PY'
from html.parser import HTMLParser
from pathlib import Path
import sys


class IframeTitleCounter(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.missing = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        title = next((value for name, value in attrs if name.lower() == "title"), None)
        if tag.lower() == "iframe" and not (title and title.strip()):
            self.missing += 1


parser = IframeTitleCounter()
parser.feed(Path(sys.argv[1]).read_text(encoding="utf-8"))
parser.close()
print(parser.missing)
PY
}

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
    local work
    work="$run_root/$(basename "$fixture")-work"
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
    local work
    work="$run_root/$(basename "$fixture")-work"
    cp -a "$fixture" "$work"
    local log
    log="$run_root/$(basename "$fixture")-uv.log"
    if ! UV_CACHE_DIR="$run_root/uv-cache" uv run --locked --project "$scenario_root" --directory "$work" zensical build --clean >"$log" 2>&1; then
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

for fixture in tabbed-site accessibility-site base-path-site code-anchor-site; do
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
panel_count="$(rg -o '<div class="tabbed-block">' "$tab_output" | wc -l)"
if [[ "$panel_count" -ne 4 ]]; then
  printf 'tabbed-site: expected 4 non-empty tab panels; found %s\n' "$panel_count" >&2
  exit 1
fi
for command_name in npm pnpm yarn bun; do
  if ! rg -F "$command_name" "$tab_output" >/dev/null; then
    printf 'tabbed-site: rendered panel missing command: %s\n' "$command_name" >&2
    exit 1
  fi
done
printf 'tabbed-site: rendered tab group with four non-empty alternatives\n'

a11y_output="$run_root/accessibility-site-output/index.html"
if ! rg -F '<iframe ' "$a11y_output" >/dev/null; then
  printf 'accessibility-site: iframe fixture missing from output\n' >&2
  exit 1
fi
missing_title_count="$(count_iframes_missing_titles "$a11y_output")"
if [[ "$missing_title_count" -eq 3 ]]; then
  printf 'accessibility-site: expected iframe-title findings are reproducible\n'
else
  printf 'accessibility-site: expected 3 missing iframe titles; found %s\n' "$missing_title_count" >&2
  exit 1
fi
if rg -F 'Example video' "$a11y_output" >/dev/null && rg -F 'Whitespace title' "$a11y_output" >/dev/null; then
  printf 'accessibility-site: correctly titled iframe controls remain valid\n'
else
  printf 'accessibility-site: positive iframe-title control missing\n' >&2
  exit 1
fi

code_anchor_output="$run_root/code-anchor-site-output/index.html"
if ! rg -F 'id="__span-0-1"' "$code_anchor_output" >/dev/null; then
  printf 'code-anchor-site: rendered line spans are missing\n' >&2
  exit 1
fi
if rg -F '<a id="__codelineno-' "$code_anchor_output" >/dev/null; then
  printf 'code-anchor-site: empty code-line anchors remain in rendered output\n' >&2
  exit 1
fi
printf 'code-anchor-site: retained line spans without focusable code-line anchors\n'

base_output="$run_root/base-path-site-output/index.html"
if rg -F 'href="about/"' "$base_output" >/dev/null && [[ -f "$run_root/base-path-site-output/about/index.html" ]]; then
  printf 'base-path-site: generated relative link resolves under /docs deployment path\n'
else
  printf 'base-path-site: generated link lost configured deployment path\n' >&2
  exit 1
fi
about_output="$run_root/base-path-site-output/about/index.html"
if rg -F 'href="./.."' "$about_output" >/dev/null; then
  printf 'base-path-site: nested page links back to home under deployment path\n'
else
  printf 'base-path-site: nested page lost its home link\n' >&2
  exit 1
fi

printf 'PASS: Zensical scenario builds, rendered tabs, a11y findings, code-line-anchor repair, and base-path link assertions\n'

#!/usr/bin/env bash
set -euo pipefail

# Flag likely sensitive material in tracked files without printing values.
# This is a bounded preflight, not a replacement for provider secret scanning.

repository="${1:-.}"

if ! git -C "$repository" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  printf 'Expected a Git repository: %s\n' "$repository" >&2
  exit 2
fi

declare -A findings=()

record() {
  local path="$1"
  local reason="$2"
  findings["$path"]+="${findings[$path]:+, }$reason"
}

while IFS= read -r -d '' path; do
  case "${path##*/}" in
    .env|.env.*)
      case "${path##*/}" in
        *.example|*.sample|*.template) ;;
        *) record "$path" "tracked environment file" ;;
      esac
      ;;
    id_rsa|id_dsa|id_ecdsa|id_ed25519|*.pem|*.key|*.p12|*.pfx|*.kdbx)
      record "$path" "tracked key or credential-like file"
      ;;
    credentials*.json|secrets*.json|.npmrc)
      record "$path" "tracked credential-like configuration"
      ;;
  esac
done < <(git -C "$repository" ls-files -z)

private_key_header='-----BE''GIN [A-Z ]*PRIVATE KEY-----'
github_classic_prefix='gh''p_'
github_fine_grained_prefix='github''_pat_'
aws_access_prefix='AK''IA'
aws_secret_name='aws''_secret_access_key'
signature_pattern="${private_key_header}|${github_classic_prefix}[A-Za-z0-9]{36}|${github_fine_grained_prefix}[A-Za-z0-9_]{20,}|${aws_access_prefix}[0-9A-Z]{16}|${aws_secret_name}[[:space:]]*[:=]"
matches_file="$(mktemp "${TMPDIR:-/tmp}/zensical-site-hygiene.XXXXXX")"
trap 'rm -f "$matches_file"' EXIT
set +e
git -C "$repository" grep -I -l -E -e "$signature_pattern" -- >"$matches_file"
grep_status=$?
set -e
if ((grep_status > 1)); then
  printf 'Could not inspect tracked file content safely\n' >&2
  exit 2
fi
while IFS= read -r path; do
  record "$path" "known secret signature in tracked content"
done <"$matches_file"

if ((${#findings[@]} == 0)); then
  printf 'PASS: no common sensitive-material candidates in tracked files\n'
  exit 0
fi

printf 'Sensitive-material candidates found; values were not printed:\n' >&2
while IFS= read -r path; do
  printf '%s: %s\n' "$path" "${findings[$path]}" >&2
done < <(printf '%s\n' "${!findings[@]}" | sort)
printf 'Stop and obtain maintainer direction before commit, publish, or deployment.\n' >&2
exit 1

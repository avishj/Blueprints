#!/usr/bin/env bash
set -euo pipefail

actions=$(grep -rh 'uses:' --include='*.yml' --include='*.yaml' --include='*.jinja' . \
  | sed 's/.*uses: *//' \
  | grep '@' \
  | grep -v '@main' \
  | sed 's/ *#.*//' \
  | sort -u || true)

if [ -z "$actions" ]; then
  exit 0
fi

printf "%-50s %-14s %-14s %-12s %s\n" "ACTION" "CURRENT SHA" "LATEST SHA" "LATEST TAG" "STATUS"
printf '%.0s-' {1..140}; echo

while IFS= read -r entry; do
  repo=$(echo "$entry" | cut -d'@' -f1)
  current_sha=$(echo "$entry" | cut -d'@' -f2)

  # For sub-path actions like github/codeql-action/init, the repo is the first two segments
  gh_repo=$(echo "$repo" | cut -d'/' -f1-2)

  if [[ "$gh_repo" == "github/codeql-action" ]]; then
    latest_tag=$(gh api "repos/$gh_repo/tags" -q '.[].name' 2>/dev/null | grep -E '^v[0-9]' | head -n 1 || echo "")
  else
    latest_tag=$(gh release view --repo "$gh_repo" --json tagName -q '.tagName' 2>/dev/null || echo "")
  fi

  if [[ -z "$latest_tag" ]]; then
    # Fallback to latest tag by date if no release exists
    latest_tag=$(gh api "repos/$gh_repo/tags?per_page=1" -q '.[0].name' 2>/dev/null || echo "UNKNOWN")
  fi

  # Get the commit SHA that the tag points to (resolve annotated tags)
  latest_sha=$(gh api "repos/$gh_repo/git/ref/tags/${latest_tag}" -q '.object.sha' 2>/dev/null || echo "")
  if [[ -n "$latest_sha" ]]; then
    # Check if it's an annotated tag (type=tag) and dereference to commit
    obj_type=$(gh api "repos/$gh_repo/git/tags/$latest_sha" -q '.object.type' 2>/dev/null || echo "")
    if [[ "$obj_type" == "commit" ]]; then
      latest_sha=$(gh api "repos/$gh_repo/git/tags/$latest_sha" -q '.object.sha' 2>/dev/null || echo "$latest_sha")
    fi
  fi

  if [[ -z "$latest_tag" || "$latest_tag" == "UNKNOWN" || -z "$latest_sha" ]]; then
    status="❓ unknown"
  elif [[ "$current_sha" == "$latest_sha" ]]; then
    status="✅ up-to-date"
  else
    status="⚠️  update available"
  fi

  printf "%-50s %-14s %-14s %-12s %s\n" "$repo" "${current_sha:0:12}" "${latest_sha:0:12}" "$latest_tag" "$status"
done <<< "$actions"

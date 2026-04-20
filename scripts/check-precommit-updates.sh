#!/usr/bin/env bash
set -euo pipefail

# Find all pre-commit config files (including .jinja variants)
configs=$(find . -name '.pre-commit-config*' -not -path '*/.git/*' | sort)

if [[ -z "$configs" ]]; then
  echo "No .pre-commit-config* files found."
  exit 0
fi

# Extract repo + pinned SHA + tag comment from all configs
# Matches lines like: rev: <sha>  # vX.Y.Z
entries=$(echo "$configs" | while IFS= read -r file; do
  awk '
    /^[ \t]*- repo:/ && !/local/ {
      repo = $NF
    }
    /^[ \t]*rev:/ && repo {
      rev = $2
      tag = ""
      idx = index($0, "#")
      if (idx > 0) {
        tag = substr($0, idx + 1)
        gsub(/^[ \t]+/, "", tag)
        gsub(/[ \t]+$/, "", tag)
      }
      print repo "|" rev "|" tag
      repo = ""
    }
  ' "$file"
done | sort -t'|' -k1,1 -u)

if [[ -z "$entries" ]]; then
  echo "No pinned remote repos found."
  exit 0
fi

printf "%-50s %-44s %-44s %-12s %s\n" "REPO" "CURRENT SHA" "LATEST SHA" "LATEST TAG" "STATUS"
printf '%.0s-' {1..200}; echo

while IFS='|' read -r repo current_sha current_tag; do
  gh_repo=$(echo "$repo" | sed 's|https://github.com/||')

  latest_tag=$(gh release view --repo "$gh_repo" --json tagName -q '.tagName' 2>/dev/null || echo "")
  if [[ -z "$latest_tag" ]]; then
    latest_tag=$(gh api "repos/$gh_repo/tags?per_page=1" -q '.[0].name' 2>/dev/null || echo "UNKNOWN")
  fi

  # Get the commit SHA that the tag points to (resolve annotated tags)
  latest_sha=$(gh api "repos/$gh_repo/git/ref/tags/${latest_tag}" -q '.object.sha' 2>/dev/null || echo "")
  if [[ -n "$latest_sha" ]]; then
    obj_type=$(gh api "repos/$gh_repo/git/tags/$latest_sha" -q '.object.type' 2>/dev/null || echo "")
    if [[ "$obj_type" == "commit" ]]; then
      latest_sha=$(gh api "repos/$gh_repo/git/tags/$latest_sha" -q '.object.sha' 2>/dev/null || echo "$latest_sha")
    fi
  fi

  if [[ "$current_sha" == "$latest_sha" ]]; then
    status="✅ up-to-date"
  else
    status="⚠️  update available"
  fi

  printf "%-50s %-44s %-44s %-12s %s\n" "$gh_repo" "$current_sha" "$latest_sha" "$latest_tag" "$status"
done <<< "$entries"

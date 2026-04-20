#!/usr/bin/env bash
set -euo pipefail

# Find all Dockerfiles (including .jinja variants)
dockerfiles=$(find . -name 'Dockerfile*' -not -path '*/.git/*' | sort)

if [[ -z "$dockerfiles" ]]; then
  echo "No Dockerfiles found."
  exit 0
fi

# Extract image references pinned by digest: image:tag@sha256:...
# Deduplicates by image:tag (same image pinned in multiple files only checked once)
entries=$(echo "$dockerfiles" | while IFS= read -r file; do
  grep -E '^\s*FROM\s+\S+@sha256:' "$file" | while IFS= read -r line; do
    image_ref=$(echo "$line" | sed 's/.*FROM[[:space:]]*//' | awk '{print $1}')
    image_tag=$(echo "$image_ref" | cut -d'@' -f1)
    current_digest=$(echo "$image_ref" | grep -o 'sha256:[a-f0-9]*')
    echo "$image_tag|$current_digest"
  done
done | sort -t'|' -k1,1 -u)

if [[ -z "$entries" ]]; then
  echo "No pinned base images found."
  exit 0
fi

printf "%-55s %-73s %-73s %s\n" "IMAGE" "CURRENT DIGEST" "LATEST DIGEST" "STATUS"
printf '%.0s-' {1..250}; echo

while IFS='|' read -r image_tag current_digest; do
  latest_digest=$(docker buildx imagetools inspect "$image_tag" 2>&1 \
    | grep '^Digest:' | awk '{print $2}' || true)

  if [[ -z "$latest_digest" ]]; then
    status="❌ lookup failed"
    latest_digest="N/A"
  elif [[ "$current_digest" == "$latest_digest" ]]; then
    status="✅ up-to-date"
  else
    status="⚠️  update available"
  fi

  printf "%-55s %-73s %-73s %s\n" "$image_tag" "$current_digest" "$latest_digest" "$status"
done <<< "$entries"

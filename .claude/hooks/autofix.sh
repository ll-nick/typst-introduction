#!/usr/bin/env bash
set -euo pipefail

FILE=$(jq -r '.tool_input.file_path')

case "$FILE" in
  *.py)
    # --unfixable F401: keep import sorting and every other autofix, but do NOT
    # strip "unused" imports — mid-edit an import is often added before the line
    # that uses it, and stripping it here breaks the file. --exit-zero so a
    # transient unused import doesn't abort the hook before `ruff format` runs.
    # `mise run check` remains the real gate for genuinely unused imports.
    uv run ruff check --fix --unfixable F401 --exit-zero "$FILE"
    uv run ruff format "$FILE"
    ;;
esac

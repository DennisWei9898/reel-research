#!/usr/bin/env bash
# 產出 PDF。用法：make_pdf.sh <report.html> [輸出.pdf]
set -euo pipefail
HTML="${1:?需要 html}"; OUT="${2:-${HTML%.html}.pdf}"
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
[ -x "$CH" ] || CH="$(command -v google-chrome || command -v chromium)"
"$CH" --headless --disable-gpu --print-to-pdf="$OUT" --no-pdf-header-footer \
  "file://$(cd "$(dirname "$HTML")" && pwd)/$(basename "$HTML")" 2>/dev/null
echo "✅ $OUT  ($(du -h "$OUT" | cut -f1))"

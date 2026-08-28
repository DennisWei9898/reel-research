#!/usr/bin/env bash
# 交付前三道機械檢查。任何一道沒過就不准交付。
# 用法：verify_pdf.sh <report.html> <期望頁數>
set -uo pipefail
HTML="${1:?需要 html 路徑}"; WANT="${2:?需要期望頁數}"
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
[ -x "$CH" ] || CH="$(command -v google-chrome || command -v chromium)"
TMP=$(mktemp -d); PDF="$TMP/r.pdf"; FAIL=0

"$CH" --headless --disable-gpu --print-to-pdf="$PDF" --no-pdf-header-footer "file://$(cd "$(dirname "$HTML")" && pwd)/$(basename "$HTML")" 2>/dev/null
pdftoppm -png -r 60 "$PDF" "$TMP/pg"

N=$(ls "$TMP"/pg-*.png 2>/dev/null | wc -l | tr -d ' ')
echo "① 頁數 $N（期望 $WANT）"
[ "$N" = "$WANT" ] || { echo "   ❌ 頁數不符——通常是某頁內容溢出，或列印樣式被非 @media print 規則覆蓋"; FAIL=1; }

CJK=$(pdftotext "$PDF" - 2>/dev/null | grep -o '[一-龥]' | wc -l | tr -d ' ')
echo "② 中文字元 $CJK（需 >1000）"
[ "$CJK" -gt 1000 ] || { echo "   ❌ 中文沒畫出來——字型堆疊裡沒有任何一個真的存在且含中文"; FAIL=1; }

echo "③ 墨水覆蓋率（<1% = 空白頁）"
python3 - "$TMP" <<'PY'
import sys, glob, numpy as np
from PIL import Image
# 門檻依實測校準（2026-08-24）：
#   真正的空白頁（只剩頁首頁尾線）實測 0.02%
#   內容稀疏但完整的結論頁實測 0.93%  ← 舊版 <1% 判 FAIL 會誤殺這種頁
#   整頁色塊（版面爆掉）實測 96%
# 所以：<0.4% 才是真空白（擋）；0.4-1.5% 只是稀疏（提醒，不擋）
bad=[]; warn=[]
for f in sorted(glob.glob(sys.argv[1]+'/pg-*.png')):
    c=(np.array(Image.open(f).convert('L'))<128).mean()*100
    if c < 0.4:   flag='  ❌ 空白頁'; bad.append(f)
    elif c > 60:  flag='  ❌ 整頁色塊（版面爆掉）'; bad.append(f)
    elif c < 1.5: flag='  ⚠️ 內容稀疏（不擋，但值得看一眼是否留白過多）'; warn.append(f)
    else:         flag=''
    print(f"   {f.split('/')[-1]} {c:.2f}%{flag}")
if warn and not bad:
    print(f"   （{len(warn)} 頁偏稀疏，非錯誤）")
sys.exit(1 if bad else 0)
PY
[ $? -eq 0 ] || FAIL=1

rm -rf "$TMP"
[ $FAIL -eq 0 ] && echo "✅ 三道全過，可交付" || { echo "🚫 有檢查未過，不得交付"; exit 1; }

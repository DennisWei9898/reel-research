#!/usr/bin/env bash
# 檢查 README／文件裡的相對連結是否真的存在，並找出沒人引用的圖檔。
#
# 為什麼需要這支：連結指向「只存在於作者電腦上的檔案」時，本機看一切正常，
# clone 下來才會壞。這種錯誤不會有任何 log 或警告，只有讀者會遇到。
# 反過來也一樣：從文件裡刪掉一張圖，檔案還留在 repo 裡，也不會有人提醒你。
#
# 用法：
#   verify_links.sh                 # 檢查目前目錄下所有 .md 與 .html
#   verify_links.sh README.md       # 只檢查指定檔案
#   verify_links.sh docs/           # 檢查某個目錄
#
# 退出碼：0 = 通過（可能有 WARN）／1 = 有失效連結，不可交付
set -uo pipefail

TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
BROKEN="$TMP/broken"; REFS="$TMP/refs"; : > "$BROKEN"; : > "$REFS"

collect() {
  if [ -d "$1" ]; then
    find "$1" -type f \( -name '*.md' -o -name '*.html' \) -not -path '*/.git/*'
  else
    printf '%s\n' "$1"
  fi
}

if [ $# -eq 0 ]; then
  FILES="$(collect . | sort)"
else
  FILES="$(for a in "$@"; do collect "$a"; done | sort)"
fi
[ -z "$FILES" ] && { echo "沒有找到 .md / .html 檔"; exit 0; }

NFILE=0; NLINK=0
echo "① 相對連結是否指向真實存在的檔案"
while IFS= read -r f; do
  [ -z "$f" ] && continue
  NFILE=$((NFILE+1))
  dir="$(dirname "$f")"
  # markdown 的 ](path)、HTML 的 src="path" / href="path"
  links="$(grep -oE '\]\([^)]+\)|(src|href)="[^"]+"' "$f" 2>/dev/null \
           | sed -E 's/^\]\(//; s/\)$//; s/^(src|href)="//; s/"$//')"
  while IFS= read -r link; do
    [ -z "$link" ] && continue
    case "$link" in
      http://*|https://*|mailto:*|data:*|'#'*|//*) continue ;;
    esac
    link="${link%%#*}"; link="${link%%\?*}"
    [ -z "$link" ] && continue
    NLINK=$((NLINK+1))
    target="$dir/$link"
    printf '%s\n' "${target#./}" >> "$REFS"
    if [ ! -e "$target" ]; then
      printf '   ✗ %s → %s\n' "$f" "$link"
      printf 'x\n' >> "$BROKEN"
    fi
  done <<< "$links"
done <<< "$FILES"

NBROKEN=$(wc -l < "$BROKEN" | tr -d ' ')
echo "   檢查 $NFILE 個檔案、$NLINK 個相對連結｜失效 $NBROKEN 個"

echo "② 沒有被任何文件引用的圖檔（孤兒）"
NORPHAN=0
while IFS= read -r img; do
  [ -z "$img" ] && continue
  if ! grep -qxF "$img" "$REFS"; then
    printf '   ⚠ %s\n' "$img"
    NORPHAN=$((NORPHAN+1))
  fi
done <<< "$(find . -type f \( -name '*.png' -o -name '*.jpg' -o -name '*.jpeg' -o -name '*.svg' -o -name '*.gif' \) \
            -not -path './.git/*' 2>/dev/null | sed 's|^\./||' | sort)"
[ "$NORPHAN" -eq 0 ] && echo "   ✓ 沒有孤兒圖檔"

echo
if [ "$NBROKEN" -gt 0 ]; then
  echo "❌ 有 $NBROKEN 個失效連結，不可交付"
  exit 1
fi
if [ "$NORPHAN" -gt 0 ]; then
  echo "⚠️  連結全有效，但有 $NORPHAN 張圖沒人引用（刪連結時忘了刪檔，或反過來）"
fi
echo "✅ 連結檢查通過"
exit 0

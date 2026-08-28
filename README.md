<div align="center">

# reel-research · 短影音研究報告

### 丟一支影片進去，回一份看得懂、查得證、可行動的報告
### Drop a reel in, get a researched, verifiable, actionable report out

**不只是 fact-check。講工具就驗工具能不能用，講地點就查在哪與怎麼訂，講數據就重算，講教學就照做一次——研究路徑跟著內容型態走。**
**Not just fact-checking. Tools get tested, places get located, numbers get recomputed, tutorials get followed — the research path adapts to the content.**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Examples](https://img.shields.io/badge/examples-4%20reports-B23A2E.svg)
![Routing](https://img.shields.io/badge/routing-6%20content%20types-8A2BE2.svg)
![Skill](https://img.shields.io/badge/skill-included-9A7B33.svg)
![Reproducible](https://img.shields.io/badge/scripts-reproducible-3C6B4F.svg)
![Language](https://img.shields.io/badge/lang-繁體中文%20%C2%B7%20EN-lightgrey.svg)

**[繁體中文](#繁體中文)** · **[English](#english)**

<p align="center">
  <img src="docs/preview-div-p1.png" width="23%" alt="example 1 — 100 dividend stocks, recomputed" />
  <img src="docs/preview-ai-p1.png" width="23%" alt="example 2 — 13 AI tools identified from frames" />
  <img src="docs/preview-seoul-p1.png" width="23%" alt="example 3 — Seoul places located from signage" />
  <img src="docs/preview-xls-p1.png" width="23%" alt="example 4 — Excel tutorial actually followed" />
</p>

<sub><b>四種完全不同的影片，同一套流程。</b>
數據主張（100 家公司逐一重算）· 工具（旁白 0 個名字，從畫面認出 13 個）· 地點（沒有旁白，從招牌認出 8 個地點）· 教學（照做一次，第一次跑出 #NAME?）<br/>
Four very different reels, one pipeline. A data claim recomputed · 13 tools identified from frames · 8 places located from signage · a tutorial actually executed.</sub>

<br/>

<p align="center">
  <img src="docs/preview-div-p2.png" width="23%" alt="the 20 named companies that fail the claim" />
  <img src="docs/preview-ai-p2.png" width="23%" alt="identifying tools from logos" />
  <img src="docs/preview-seoul-p3.png" width="23%" alt="addresses, hours, ratings" />
  <img src="docs/preview-xls-p3.png" width="23%" alt="the argument the demo cannot show" />
</p>

<sub>被點名卻不符合的 20 家，逐檔列出實際配息比率 · 從 logo 認工具 · 地址／營業時間／評價逐項落地 · 教學教的參數在它自己的示範裡是隱形的<br/>
The 20 named companies that fail the claim, with their real payout ratios · reading logos · addresses, hours and ratings · the argument the demo itself cannot show.</sub>

</div>

---

<a name="繁體中文"></a>

## 繁體中文

### 這是什麼

短影音很會講，但**看完不知道能不能信、也不知道下一步要幹嘛**。

這個 repo 是一套流程：**丟一支 IG／短影音連結進去，回一份 A4 報告**——把影片拆開、判斷它在講什麼類型、走對應的研究路徑，然後給你一份可以直接行動的東西。

**重點不是結論，是方法。** 每個數字附來源，每個腳本都能自己重跑。

### 核心：先判斷類型，再決定怎麼研究

同一套「查證」對所有影片一視同仁是沒用的。講工具的影片，你要的是「這工具現在能不能用、多少錢」；講旅遊的影片，你要的是「在哪、評價如何、怎麼訂」。所以流程的第一步是**分流**：

| 類型 | 影片在幹嘛 | 研究路徑 | 你最後拿到什麼 |
|---|---|---|---|
| **A 工具／產品** | 推薦或展示某個 App、AI 工具 | 從畫面 logo 與文字標籤推斷是哪個工具 → 查官網現況 → 查價格 → 可能的話**實際裝來跑** | 工具清單 ＋ 現在能不能用 ＋ 真實價格 ＋ 誰能用 |
| **B 事實／數據主張** | 「100 家公司配息超過一半盈餘」這種 | 找一手來源 → 查方法論批評 → **自己抓資料重算一次** | 逐條真偽 ＋ 自己跑的實測表 |
| **C 地點／旅遊／餐廳** | 景點、餐廳、行程 | 從畫面招牌／地標定位 → 查地址營業時間 → 查多平台評價 → **查怎麼訂位／購票** | 地點清單 ＋ 地址 ＋ 評價 ＋ 訂位方式 |
| **D 教學／How-to** | 步驟示範 | 步驟拆解 → 前置條件 → **實際照做一次** | 可執行步驟 ＋ 卡住的地方 |
| **E 開箱／購物** | 商品推薦 | 認出型號 → 比價 → 找負評 | 型號 ＋ 目前價格 ＋ 反面意見 |
| **F 混合** | 同時有好幾種 | 拆成多個區塊，各走各的路徑 | 分區塊的報告 |

> 完整路由規則在 [`skill/references/routing.md`](skill/references/routing.md)。

### 四個實例

#### 範例 1 · 數據主張型：「100 家公司把一半以上的盈餘配出去」

📄 [`reports/01-dividend-payout/report.pdf`](reports/01-dividend-payout/report.pdf) · 🌐 [HTML](reports/01-dividend-payout/report.html)

一支 58 秒的影片閃過 20 張字卡、100 個公司名，**但一個數字都沒給**——沒說配息比率是多少、沒說怎麼算、沒給出處。

沒有停在「聽起來合理」，而是把 100 個名字全部對成股票代號，用免費公開資料**逐家算一遍**：

| 結果 | 數字 |
|---|---|
| 畫面上的位置 | 100 |
| **實際唯一公司數** | **98**（Xcel Energy 在同一張字卡出現兩次、Thomson Reuters 跨卡重複） |
| 配息確實超過一半盈餘 | 76（77.6%） |
| **配息並沒有超過一半** | **20**（最低 22.8%） |
| 算不出來 | 2（一家近四季虧損，分母是負的） |
| 其中屬 REIT | 12（配息比率 62%–364%） |

三個發現：

1. **第一張字卡的第一個名字就是反例。** Broadcom 的配息比率是 41.3%，差 50% 那條線將近 9 個百分點。清單型影片最容易發生的事，就是**前幾個名字用來建立信任、後面沒人逐項查**。
2. **「能源股配息高」這句話本身就不成立。** 清單裡 15 家能源股，配息比率從 **22.8% 到 227.4%**——差距 10 倍。而且分界線很乾淨：**7 家管線中游（Kinder Morgan 227%、Phillips 66 226%、Enbridge 148%、Pembina 101%、TC Energy 98%、MPLX 90%、ONEOK 73%）全部超過 70%；20 家反例裡的 5 家能源股，全部是上游探勘生產**（Cenovus 22.8%、Occidental 29.5%、Imperial Oil 37.2%、Canadian Natural 43.2%、ConocoPhillips 43.6%）。管線收的是過路費、現金流穩定；探勘生產靠油價，**盈餘暴衝的時候配息比率反而被壓低**。同一個產業標籤，商業模式決定一切。
3. **12 家是 REIT，法規逼它這樣配。** REIT 依法必須把 90% 以上應稅所得配出去，而會計盈餘被大額折舊壓低。**REIT 配息超過盈餘一半是結構性必然，不是發現。**

#### 範例 2 · 工具型：旁白一個名字都沒念

📄 [`reports/02-ai-stack/report.pdf`](reports/02-ai-stack/report.pdf) · 🌐 [HTML](reports/02-ai-stack/report.html)

一支「My August 2026 AI Stack」的 reel，旁白從頭到尾只說 *content lives here / automation runs here / research happens here*——**13 個工具名稱一個都沒念出來**，全部只在畫面的 logo 卡片上。

- **逐秒硬抽幀**（不是場景變化偵測）。這支影片背景幾乎不動，`--scene-threshold 0.18` 只抓到 **1 幀**，整支影片的資訊會全部漏光。
- **文字標籤優先於 logo 外觀。** 獨立查證員把橘底白閃電判成 Zapier（合理，那正是 Zapier 的經典配色），但放大後文字標籤清楚寫著 **Cowork**。
- **認出來之後還要驗「現在能不能用」**：13 個全部存在且可用，但 **1 個已改名**（NotebookLM → Gemini Notebook）、**1 個免費額度即將到期**、而且**實際只需要 8 個帳號**——影片沒講，但這決定你要不要照抄。

#### 範例 3 · 地點型：沒有旁白，只有招牌

📄 [`reports/03-seoul-seongsu/report.pdf`](reports/03-seoul-seongsu/report.pdf) · 🌐 [HTML](reports/03-seoul-seongsu/report.html)

一支首爾聖水洞的氛圍 reel：**只有音樂，語音逐字稿抓出來是 0 行**，caption 只寫了「聖水洞」三個字，一間店名都沒給。

- **招牌就是全部線索。** 畫面出現 11 處地點，**8 個定位成功**（6 個查到完整門牌）、3 個查不到。
- **最有價值的一幀是韓文公共設施招牌。** 「성동구민종합체육센터」（城東區民綜合體育中心）名稱唯一，直接鎖定行政區。
- **拍攝順序可以驗證地址。** 兩個資料源給了 Le Alaska 不同地址，但影片下一秒轉到 Tom Greyhound（연무장길 21）、再下一秒是 Diptyque——**同一條街、門牌連號、順序吻合**，所以 연무장길 20-1 那個版本合理得多。門牌排起來就是一條 100 公尺的實走路線。
- **caption 的地名不能當定位依據。** 影片前 5 秒是皮膚科診所街與賣「KOREA」磁鐵的紀念品店，聖水洞沒有這種觀光商圈——**這段查不到具體位置，只能確定不是 caption 說的地方。**
- 最後回答最實際的問題：**要不要預約。** 麵包店都是 walk-in，週末要排隊；韓國的排隊／訂位分工是 캐치테이블（訂位）、테이블링（遠端拿號）、네이버 예약（部分店家）。

#### 範例 4 · 教學型：26 秒的 Excel 公式教學，照做一次

📄 [`reports/04-excel-textjoin/report.pdf`](reports/04-excel-textjoin/report.pdf) · 🌐 [HTML](reports/04-excel-textjoin/report.html)

一支 26 秒、**沒有旁白也沒有字幕**的螢幕錄影，一路把 `=TEXTJOIN(" ",TRUE,G2:I2)` 打完。

教學型的查證跟其他類型不一樣：**公式寫對了、步驟也拍全了，你照做還是可能失敗**，因為卡住的地方通常在畫面外。所以這條路徑唯一有效的查證方式是**自己跑一遍，然後記錄卡在哪**——這裡是把畫面那張表重建，照打同一條公式，用 LibreOffice headless 實際計算。

- **照做結果一致。** F2 算出 `Gujarat Surat Gujarati`，跟影片畫面完全一樣。公式本身沒問題。
- **但第一次跑，八列全部 `#NAME?`。** 診斷結果不是版本問題，是**檔案格式的坑**：TEXTJOIN／CONCAT／IFS 這些後來才加進 Excel 的函式，在 xlsx 檔裡必須存成 `_xlfn.TEXTJOIN`。用程式產生 Excel 檔（openpyxl）照人看到的名字寫，Excel 與 LibreOffice 都會回 `#NAME?`。
- **影片漏了版本這一步。** 微軟官方文件列的支援版本是 Microsoft 365／Excel 2024／2021／2019；**Excel 2016 及更早沒有這個函式**，照做會得到 `#NAME?`——看起來像打錯字，不像版本問題。
- **它教的參數在它自己的示範裡是隱形的。** 影片示範的 8 列資料一格空的都沒有，所以 `ignore_empty` 給 `TRUE` 或 `FALSE` **輸出必然完全相同**。另外補 3 列有空格的資料，3 列全部不同——**這才是 TEXTJOIN 唯一勝過 `&` 串接的地方。**
- **影片只算了 1 列就結束**，沒示範怎麼往下填。報告補上完整 8 步，並列出沒有新版 Excel 的三條替代路線（Google 試算表／LibreOffice／`&` 串接，各自的代價）。

### 自己重跑（範例 1 的數據）

```bash
pip install yfinance pandas
python3 data/payout_check.py     # 逐家查 98 檔，輸出 payout_check.csv
```

資料來源 Yahoo Finance，免費公開。腳本裡的 `CARDS` 就是影片 20 張字卡的原文——**改掉它就能驗別的清單影片**。明細（每家的配息比率、每股盈餘、產業分類、兩種算法結果）在 [`data/payout_check.csv`](data/payout_check.csv)。

範例 4 的教學也可以自己跑一次：

```bash
pip install openpyxl
python3 data/textjoin_test.py    # 需要先裝 LibreOffice
```

腳本會重建影片那張表、照打公式、叫 LibreOffice 實際計算，再把 `TRUE` / `FALSE` / `CONCAT` / `&` 四種做法並排印出來。

### 這套流程本身（skill）

上面四份報告不是手工做的，是同一支 skill 跑出來的。**它就在 [`skill/`](skill/) 裡**：

| 檔案 | 內容 |
|---|---|
| [`SKILL.md`](skill/SKILL.md) | 六階段主流程、抽幀策略表、命名規則、反模式清單 |
| [`references/routing.md`](skill/references/routing.md) | **六種內容類型的研究路徑**，含每條路徑實跑後的教訓 |
| [`references/failure-modes.md`](skill/references/failure-modes.md) | 十大失效模式與判定尺度 |
| [`references/report-template.md`](skill/references/report-template.md) | 報告的硬結構與內容紀律 |
| [`assets/report.css`](skill/assets/report.css) | A4 印刷稿樣式，模板要求的元件 class 都在這裡 |
| [`scripts/verify_pdf.sh`](skill/scripts/verify_pdf.sh) | 交付前三道機械檢查：頁數 1:1／中文字數／每頁墨水覆蓋率 |
| [`scripts/make_pdf.sh`](skill/scripts/make_pdf.sh) | HTML → PDF |

**在 Claude Code 裡使用**：把 `skill/` 整個複製到 `~/.claude/skills/reel-research/`，
之後丟一支影片連結進去就會走這套流程。

```bash
cp -R skill ~/.claude/skills/reel-research
```

**不用 Claude Code 也能用**：`SKILL.md` 與 `references/` 是純文字的方法論，
可以直接當成 prompt 貼給任何模型；`scripts/` 是獨立的 bash，
`verify_pdf.sh <report.html> <期望頁數>` 對任何 A4 HTML 報告都能跑。

### 流程長什麼樣

1. **拆影片**——抽幀＋逐字稿。**畫面字卡優先於語音逐字稿**（ASR 對專有名詞漂字嚴重），caption 也要另外抓（caption 常宣稱畫面沒演的東西）
2. **判斷類型**——走上面那張路由表，選對研究路徑
3. **依路徑研究**——工具就驗可用性與價格；數據就找一手來源＋方法論批評＋**自己重算**；地點就定位＋評價＋訂位方式
4. **失效模式過篩**——拆分幻覺、選樣偏誤、成本消失、量級偷換、時效腐爛……共十類
5. **產報告**——A4 印刷稿版型，每頁一句白話總結，每個概念配生活比喻，交付前跑三道機械檢查（頁數 1:1／中文字數／每頁墨水覆蓋率）＋**肉眼逐頁看**

### 幾個踩過的坑（直接寫進流程了）

| 坑 | 後果 | 現在怎麼做 |
|---|---|---|
| 用場景變化偵測抽幀 | 靜態畫面的影片只抽到 1 幀，整支漏光，**而且不會報錯** | 先判斷影片動不動，靜態就**逐秒硬抽** |
| 抽幀時開著「去重複」 | 螢幕錄影教學裡唯一在變的是公式列那幾個字，佔畫面不到 1% 像素 → 被當成重複丟掉，打字過程整段消失 | **螢幕錄影一律關掉去重複**，改固定間隔硬抽 |
| 相信 logo 外觀 | 把 Cowork 認成 Zapier | **有文字標籤時文字優先** |
| 相信 caption 的地名 | 影片有一段根本不在那裡拍 | caption 只當線索，用畫面裡的地標交叉驗證 |
| 引用比率卻不說算法 | 換一種算法，結論可能反過來 | **一律標明分子與分母** |
| 清單型影片只抽查後面幾項 | 第一個名字就可能是反例 | **從第一項開始逐項查** |
| 機械檢查過了就交付 | 抓不到「表格排版壞掉但字都在」 | **必須肉眼逐頁看** |
| 模板要求的 class 只寫在某一份成品裡 | 下一份報告 class 沒有 CSS，圖片以原始像素渲染、內容溢出分頁 | **共用元件住在共用 CSS**，不靠每份報告自己抄 |

### 免責

工具可用性查證、地點與交通整理、數據重算、教學可行性查核。**不含個股買賣建議，也不含工具、商家或軟體的推薦與代言。**
價格、費率、營業時間與配息比率為 2026-08 實測，都會變動。影片內容一律視為**待驗證資料**。

---

<a name="english"></a>

## English

### What this is

Short-form video is persuasive, but you finish watching **without knowing whether to believe it, or what to do next**.

This repo is a pipeline: **drop in a reel link, get back an A4 report** — the video is broken down, its content type is identified, the matching research path runs, and you get something you can act on.

**The point isn't the conclusion — it's the method.** Every figure has a source; every script runs.

### The core idea: classify first, then research

One generic "fact-check" doesn't fit every video. For a tool video you want *does it still work and what does it cost*; for a travel video you want *where is it, is it any good, how do I book*. So step one is **routing**:

| Type | What the reel does | Research path | What you get |
|---|---|---|---|
| **A Tools / products** | Recommends or demos an app or AI tool | Infer the tool from on-screen logos and text labels → check the official site → check pricing → **install and run it** where possible | Tool list + availability + real pricing + who can actually use it |
| **B Factual / data claims** | "100 companies pay out over half their profits" and the like | Find the primary source → look for methodology criticism → **pull the data and recompute** | Claim-by-claim verdicts + your own empirical table |
| **C Places / travel / food** | Spots, restaurants, itineraries | Locate from signage and landmarks → address and hours → multi-platform reviews → **how to book** | Place list + addresses + reviews + booking route |
| **D Tutorials / how-to** | Step-by-step demos | Decompose steps → prerequisites → **actually follow them once** | Runnable steps + where it breaks |
| **E Unboxing / shopping** | Product recommendations | Identify the model → compare prices → find the negative reviews | Model + current price + the other side |
| **F Mixed** | Several at once | Split into sections, route each separately | Sectioned report |

> Full routing rules live in [`skill/references/routing.md`](skill/references/routing.md).

### Four worked examples

#### Example 1 · A data claim: "100 stocks that pay more than half their profits as dividends"

📄 [`reports/01-dividend-payout/report.pdf`](reports/01-dividend-payout/report.pdf) · 🌐 [HTML](reports/01-dividend-payout/report.html)

A 58-second reel flashes 20 title cards naming 100 companies — and **gives not a single number**. No payout ratios, no formula, no source.

Rather than stopping at "sounds plausible", every name was mapped to a ticker and **recomputed from free public data**:

| Result | Number |
|---|---|
| On-screen slots | 100 |
| **Actual unique companies** | **98** (Xcel Energy appears twice on the same card; Thomson Reuters repeats across cards) |
| Payout ratio genuinely above 50% | 76 (77.6%) |
| **Payout ratio not above 50%** | **20** (lowest: 22.8%) |
| Not computable | 2 (one has negative trailing EPS — the denominator) |
| Of the 76, REITs | 12 (payout ratios 62%–364%) |

Three findings:

1. **The very first name on the very first card is a counterexample.** Broadcom pays out 41.3% — nearly 9 points short of the 50% line. With list-format videos, the first few names build trust and **nobody checks the rest.**
2. **"Energy stocks pay high dividends" isn't a statement that survives contact with the data.** The list holds 15 energy names, with payout ratios from **22.8% to 227.4%** — a tenfold spread — and the split is clean: **all 7 midstream/pipeline names clear 70%** (Kinder Morgan 227%, Phillips 66 226%, Enbridge 148%, Pembina 101%, TC Energy 98%, MPLX 90%, ONEOK 73%), while **all 5 energy counterexamples are upstream E&P** (Cenovus 22.8%, Occidental 29.5%, Imperial Oil 37.2%, Canadian Natural 43.2%, ConocoPhillips 43.6%). Pipelines collect tolls on steady cash flow; explorers ride the oil price, and **a spike in earnings pushes the payout ratio down**. Same sector label, opposite behaviour.
3. **12 are REITs, legally required to pay out like that.** REITs must distribute 90%+ of taxable income, and GAAP earnings are suppressed by heavy depreciation. **A REIT paying out more than half its earnings is structural, not a discovery.**

#### Example 2 · A tools reel where zero tool names are ever spoken

📄 [`reports/02-ai-stack/report.pdf`](reports/02-ai-stack/report.pdf) · 🌐 [HTML](reports/02-ai-stack/report.html)

A "My August 2026 AI Stack" reel. The voiceover says only *content lives here / automation runs here / research happens here* — **not one of the 13 tool names is ever said aloud.** They exist only as logo cards on screen.

- **Dense per-second frame extraction, not scene-change detection.** The background barely moves; `--scene-threshold 0.18` captured **one frame** and would have missed the entire video.
- **Text labels beat logo appearance.** An independent verifier called the orange lightning bolt Zapier — reasonable, that's Zapier's signature palette — but zoomed in, the label plainly reads **Cowork**.
- **Identification isn't the end; availability is.** All 13 exist and work, but **one was renamed** (NotebookLM → Gemini Notebook), **one's free tier is expiring**, and **you only need 8 accounts.** The reel mentions none of it, and all of it decides whether copying the stack is worth it.

#### Example 3 · A places reel with no voiceover — only signage

📄 [`reports/03-seoul-seongsu/report.pdf`](reports/03-seoul-seongsu/report.pdf) · 🌐 [HTML](reports/03-seoul-seongsu/report.html)

An ambience reel from Seongsu, Seoul: **music only — the speech transcript came back with 0 lines** — and a caption that says just "Seongsu", naming not one shop.

- **The signage is the entire evidence base.** 11 places appear on screen; **8 were located** (6 with full street numbers), 3 could not be.
- **The single most valuable frame is a Korean public-facility sign.** 성동구민종합체육센터 (Seongdong-gu Sports Center) is a unique name that pins the administrative district immediately.
- **Shot order can validate an address.** Two sources gave Le Alaska different addresses — but the next shot is Tom Greyhound (Yeonmujang-gil 21) and the one after is Diptyque. **Same street, consecutive numbers, matching order**, which makes Yeonmujang-gil 20-1 far more credible. Lined up, the numbers form a 100-metre walking route.
- **A caption's place name is not a location.** The first 5 seconds show a street of dermatology clinics and a shop selling "KOREA" fridge magnets. Seongsu has no such tourist strip — **that segment could not be located, only ruled out.**
- Finally, the practical question: **do you need a reservation?** The bakeries are walk-in with weekend queues; in Korea the split is CatchTable (reservations), Tabling (remote queueing), Naver Reservation (some venues).

#### Example 4 · A tutorial: a 26-second Excel formula lesson, actually followed

📄 [`reports/04-excel-textjoin/report.pdf`](reports/04-excel-textjoin/report.pdf) · 🌐 [HTML](reports/04-excel-textjoin/report.html)

A 26-second screen recording — **no voiceover, no captions** — typing out `=TEXTJOIN(" ",TRUE,G2:I2)`.

Tutorials verify differently from everything else: **the formula can be right and every step on camera, and following it still fails**, because what stops you is usually off-screen. So the only verification that works here is **running it yourself and recording where it breaks** — the sheet was rebuilt, the same formula typed, and LibreOffice headless actually computed it.

- **The result matches.** F2 evaluates to `Gujarat Surat Gujarati`, exactly as shown. The formula is fine.
- **But the first run returned `#NAME?` on all eight rows.** Not a version problem — a **file-format trap**: post-spec functions like TEXTJOIN/CONCAT/IFS must be stored as `_xlfn.TEXTJOIN` inside an xlsx. Write the human-visible name from code (openpyxl) and both Excel and LibreOffice return `#NAME?`.
- **The reel skips the version step.** Microsoft's own docs list Microsoft 365 / Excel 2024 / 2021 / 2019; **Excel 2016 and earlier don't have the function at all**, and the error you get looks like a typo, not a version mismatch.
- **The argument it teaches is invisible in its own demo.** None of the 8 demo rows has an empty cell, so `ignore_empty` set to `TRUE` or `FALSE` **must** produce identical output. Add three rows with gaps and all three differ — **which is the one thing TEXTJOIN does that `&` concatenation doesn't.**
- **Only one row was ever computed** on camera, with no fill-down shown. The report supplies all 8 steps plus three fallback routes for anyone without a recent Excel (Google Sheets / LibreOffice / `&`), and what each costs.

### Reproduce it (example 1's data)

```bash
pip install yfinance pandas
python3 data/payout_check.py     # queries 98 tickers, writes payout_check.csv
```

Data comes from Yahoo Finance — free and public. The `CARDS` list in the script is the verbatim on-screen text of all 20 cards — **swap it out to verify a different list video**. Per-company detail (payout ratio, EPS, sector, both definitions) is in [`data/payout_check.csv`](data/payout_check.csv).

Example 4's tutorial is reproducible too:

```bash
pip install openpyxl
python3 data/textjoin_test.py    # needs LibreOffice installed
```

It rebuilds the sheet, types the formula, has LibreOffice compute it, and prints `TRUE` / `FALSE` / `CONCAT` / `&` side by side.

### The pipeline itself (the skill)

The four reports above weren't hand-made — one skill produced all of them, and **it lives in [`skill/`](skill/)**:

| File | What it holds |
|---|---|
| [`SKILL.md`](skill/SKILL.md) | The six-phase flow, frame-extraction strategy table, naming rules, anti-patterns |
| [`references/routing.md`](skill/references/routing.md) | **The six content-type research paths**, each with the lessons from actually running it |
| [`references/failure-modes.md`](skill/references/failure-modes.md) | Ten failure modes and the verdict scale |
| [`references/report-template.md`](skill/references/report-template.md) | The report's required structure and content discipline |
| [`assets/report.css`](skill/assets/report.css) | A4 print-dossier styling; every component class the template requires lives here |
| [`scripts/verify_pdf.sh`](skill/scripts/verify_pdf.sh) | Three pre-delivery checks: page count 1:1 / CJK char count / per-page ink coverage |
| [`scripts/make_pdf.sh`](skill/scripts/make_pdf.sh) | HTML → PDF |

**With Claude Code**: copy `skill/` to `~/.claude/skills/reel-research/`, then hand it a reel link.

```bash
cp -R skill ~/.claude/skills/reel-research
```

**Without Claude Code**: `SKILL.md` and `references/` are plain-text methodology — paste them as a prompt into any model. `scripts/` is standalone bash; `verify_pdf.sh <report.html> <expected-pages>` works on any A4 HTML report.

### The pipeline

1. **Break down the reel** — frames + transcript. **On-screen text beats the ASR transcript** (ASR mangles proper nouns), and fetch the caption separately (captions routinely claim things the video never shows)
2. **Classify** — run the routing table above and pick the path
3. **Research along that path** — tools: availability and pricing; claims: primary source + methodology criticism + **recompute it yourself**; places: location + reviews + booking route
4. **Screen against ten failure modes** — decomposition illusion, selection bias, vanished costs, magnitude swap, staleness, and so on
5. **Produce the report** — A4 print-dossier layout, one plain-language takeaway per page, one everyday analogy per concept, and before delivery three mechanical checks (page count 1:1 / CJK character count / per-page ink coverage) **plus an actual page-by-page look**

### Traps already paid for (now baked into the pipeline)

| Trap | Consequence | What the pipeline does now |
|---|---|---|
| Scene-change frame extraction | A static reel yields 1 frame and everything is missed — **with no error raised** | Check whether the reel actually moves; force dense extraction if not |
| Leaving near-duplicate dropping on | In a screencast the only thing changing is a few characters in the formula bar — under 1% of pixels — so the typing gets discarded as duplicate | **Disable dedup for screencasts**; sample at a fixed interval |
| Trusting logo appearance | Cowork read as Zapier | **When a text label exists, text wins** |
| Trusting the caption's place name | Part of the reel wasn't shot there at all | Treat the caption as a lead; cross-check against landmarks in frame |
| Quoting a ratio without its formula | Change the definition and the verdict can flip | **Always state numerator and denominator** |
| Spot-checking only the later items in a list | The first name can be the counterexample | **Verify from item one** |
| Shipping once mechanical checks pass | Misses "the table broke but all the text is there" | **Look at every page** |
| Template classes living in one finished report | The next report has classes with no CSS — images render at native pixels, content overflows the page | **Shared components live in the shared stylesheet** |

### Disclaimer

Tool-availability verification, location and transit research, recomputation of public data, and tutorial feasibility checks. **Not investment advice, and not an endorsement of any product, venue, or software.** Prices, rates, opening hours, and payout ratios measured 2026-08; all of them change. Video content is treated as **unverified data** throughout.

---

<div align="center">

### Contact · 合作聯絡

📧 dennis.xd.wei@gmail.com
💼 [LinkedIn](https://www.linkedin.com/in/dennis-wei-47393a14a/)

<sub>MIT License · 報告內容為公開資料查證，可自由引用轉載，請保留出處</sub>

</div>

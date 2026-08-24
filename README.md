<div align="center">

# reel-fact-check · Claude 選股工具與隔夜策略查證

### 兩支財經短影音，逐條查證 · Fact-checking two finance reels, claim by claim

**不是「聽起來合理」，是實際安裝、實際跑數據、實際打開原始碼。**
**Not "sounds plausible" — actually installed it, actually ran the numbers, actually read the source.**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Report](https://img.shields.io/badge/report-A4%20%C3%978%20pages-B23A2E.svg)
![Data](https://img.shields.io/badge/data-yfinance%20%C2%B7%20free-blue.svg)
![Reproducible](https://img.shields.io/badge/scripts-reproducible-3C6B4F.svg)
![Language](https://img.shields.io/badge/lang-繁體中文%20%C2%B7%20EN-lightgrey.svg)

**[繁體中文](#繁體中文)** · **[English](#english)**

<img src="docs/preview-p1.png" width="88%" alt="report cover — 一頁總表" />

<sub><b>一頁總表：不想細讀的人只看這頁就夠。</b><br/>One-page summary — if you read nothing else, read this.</sub>

<br/><br/>

<p align="center">
  <img src="docs/preview-p6.png" width="45%" alt="empirical test" />
  <img src="docs/preview-p7.png" width="45%" alt="cost comparison" />
</p>

<sub>左：5 支股票 66 天實測 · 右：每月成本對照<br/>Left: 5 tickers × 66 trading days · Right: monthly cost comparison</sub>

</div>

---

<a name="繁體中文"></a>

## 繁體中文

### 這是什麼

兩支在 IG 上流傳的財經短影音，一支推薦 AI 選股工具、一支秀出一張「隔夜買進賺 1.38 億%」的圖表。
這個 repo 是把兩支**逐條查證後的完整報告**，加上**可以自己重跑的驗證腳本**。

**重點不是結論，是方法**——每個數字都附來源，每個腳本都能自己跑一遍。

### 兩支影片、兩種查證方式

| | 影片 A | 影片 B |
|---|---|---|
| 主張 | Claude 推出 10 個股票分析工具，推薦 3 個 | 每天收盤買、隔天開盤賣，30 年賺 1.38 億% |
| 性質 | 工具推薦 | 數據主張 |
| 查證方式 | **實際安裝、實際跑、讀原始碼** | **實際抓股價、自己算一遍** |
| 結論 | 大致正確，但漏講一個工具要機構級付費資料 | 數字沒造假，**但照做會虧** |

### 影片 B：我們實測了

常見的疑問是「那測近 2–3 個月看看？挑一支股票試試」。我們測了 **5 支、66 個交易日**：

| 股票 | 隔夜（不算手續費） | 扣 30bps 手續費 | 什麼都不做 | 誰贏 |
|---|---|---|---|---|
| MU | +63.55% | +34.30% | **+41.85%** | 抱著贏 |
| NVDA | +10.79% | −9.11% | **−3.42%** | 抱著贏 |
| AAPL | **−7.71%** ← 相反 | −24.33% | **+3.86%** | 抱著贏 |
| TSLA | **−13.62%** ← 相反 | −29.19% | **−11.50%** | 抱著贏 |
| SPY | +6.79% | −12.40% | **+3.66%** | 抱著贏 |

兩個發現：

1. **挑哪一支決定你的結論。** 挑 MU 會覺得「這招超有效」，挑 AAPL 會覺得「根本沒用」——
   同一個方法換一支股票就得到相反答案，**這代表測到的不是規律，是那支股票這三個月剛好的走勢**。
2. **扣掉手續費後，五支全部輸給「什麼都不做」**，連最漂亮的 MU 也輸。
   因為這招每天要進出一次，66 天就是 66 趟來回。

### 手續費怎麼吃掉報酬（可自己改參數）

`data/隔夜策略手續費試算.xlsx` 是一份**活公式** Excel，四個分頁：

| 分頁 | 內容 |
|---|---|
| ① 參數設定 | 改黃色格子的 bps，其他分頁自動重算 |
| ② 逐日明細 | 66 天每一天的隔夜報酬、扣完成本剩多少、累積曲線——**每格都是公式，點進去看得到怎麼算的** |
| ③ 五支彙總 | 0／10／30／50 bps 四種成本下的結果，對照「什麼都不做」 |
| ④ 成本敏感度 | 手續費多高才由賺轉賠，綠轉紅一目了然 |

### 自己重跑

```bash
pip install yfinance pandas numpy openpyxl
python3 data/overnight_test.py          # 隔夜 vs 日內，含「兩半乘回去=總報酬」驗算
python3 data/overnight_with_costs.py    # 加上 10/30bps 成本
python3 data/build_xlsx.py              # 重新產出 Excel
```

資料來源是 Yahoo Finance，免費公開。**改一下 `TICKERS` 就能測你自己的股票。**

### 這份報告怎麼做的

1. **拆影片**——抽關鍵影格＋逐字稿，caption 另外抓（caption 常宣稱畫面沒演的東西）
2. **四線查證**——存在性／數字出處／方法論批評／對照面。**後兩條最容易漏，也最有價值**
3. **自己跑數據**——只要主張是「某方法有效」，就自己算，不要只講道理
4. **十大失效模式過篩**——拆分幻覺、選樣偏誤、成本消失、量級偷換……
5. **產報告**——A4 印刷稿版型，每頁一句白話總結，每個概念配生活比喻

### 報告本身

- 📄 [`report/report.pdf`](report/report.pdf) — 8 頁 A4
- 🌐 [`report/report.html`](report/report.html) — 單檔可攜（圖片已內嵌）

### 免責

工具能力查證與成本試算，**不含個股買賣建議**。價格與 API 費率為 2026-08 實測，兩者都會變動。

---

<a name="english"></a>

## English

### What this is

Two finance reels went around on Instagram: one recommending AI stock-analysis tools, one showing a chart
claiming "buy at close, sell at open → +138,330,342% since 1990."

This repo is the **full fact-check report** on both, plus **the scripts to reproduce every number yourself**.

**The point isn't the conclusion — it's the method.** Every figure has a source; every script runs.

### Two reels, two verification paths

| | Reel A | Reel B |
|---|---|---|
| Claim | Claude shipped 10 stock-analysis agents; here are 3 | Buy at close, sell at open → +138M% over 30 years |
| Type | Tool recommendation | Data claim |
| How we checked | **Installed it, ran it, read the source** | **Pulled the prices, ran the math ourselves** |
| Verdict | Broadly accurate — but omits that one tool needs institutional paid data | Numbers aren't faked, **but following it loses money** |

### Reel B: we actually tested it

The obvious question is "why not just test the last 2–3 months on one stock?" We tested **5 tickers, 66 trading days**:

| Ticker | Overnight (no fees) | After 30bps fees | Buy & hold | Winner |
|---|---|---|---|---|
| MU | +63.55% | +34.30% | **+41.85%** | Buy & hold |
| NVDA | +10.79% | −9.11% | **−3.42%** | Buy & hold |
| AAPL | **−7.71%** ← inverted | −24.33% | **+3.86%** | Buy & hold |
| TSLA | **−13.62%** ← inverted | −29.19% | **−11.50%** | Buy & hold |
| SPY | +6.79% | −12.40% | **+3.66%** | Buy & hold |

Two findings:

1. **Which ticker you pick determines your conclusion.** Pick MU and the strategy looks brilliant;
   pick AAPL and it looks useless. Same method, opposite answers — **that means you measured
   this quarter's price path, not a regularity.**
2. **After realistic fees, all five lose to doing nothing** — even MU, the best-looking one.
   The strategy needs a round trip every single day: 66 days = 66 round trips.

### How fees eat the return (tweak it yourself)

`data/隔夜策略手續費試算.xlsx` is a **live-formula** workbook, four sheets:

| Sheet | Contents |
|---|---|
| ① Parameters | Change the bps in the yellow cell; everything else recalculates |
| ② Daily detail | Every one of the 66 days — overnight return, return after fees, running curve. **Every cell is a formula you can inspect** |
| ③ Summary | Results at 0 / 10 / 30 / 50 bps, against buy & hold |
| ④ Sensitivity | At what fee level does it flip from profit to loss — green turns red |

### Reproduce it

```bash
pip install yfinance pandas numpy openpyxl
python3 data/overnight_test.py          # overnight vs intraday, incl. the (1+A)(1+B)-1 = total check
python3 data/overnight_with_costs.py    # with 10/30bps costs applied
python3 data/build_xlsx.py              # regenerate the workbook
```

Data comes from Yahoo Finance — free and public. **Change `TICKERS` to test your own.**

### How the report was made

1. **Break down the reel** — key frames + transcript; fetch the caption separately
   (captions routinely claim things the video never shows)
2. **Four verification lines** — existence / source of the numbers / methodology criticism / the other side.
   **The last two are the easiest to skip and the most valuable**
3. **Run the numbers yourself** — if the claim is "this method works," compute it; don't just argue
4. **Screen against ten failure modes** — decomposition illusion, selection bias, vanished costs,
   magnitude swap, and so on
5. **Produce the report** — A4 print-dossier layout, one plain-language takeaway per page,
   one everyday analogy per concept

### The report

- 📄 [`report/report.pdf`](report/report.pdf) — 8 pages, A4
- 🌐 [`report/report.html`](report/report.html) — single self-contained file (images embedded)

### Disclaimer

Tool-capability verification and cost estimation. **Not investment advice.**
Prices and API rates measured 2026-08; both change.

---

<div align="center">

### Contact · 合作聯絡

📧 dennis.xd.wei@gmail.com
💼 [LinkedIn](https://www.linkedin.com/in/dennis-wei-47393a14a/)

<sub>MIT License · 報告內容為公開資料查證，可自由引用轉載，請保留出處</sub>

</div>

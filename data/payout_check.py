#!/usr/bin/env python3
"""
驗證一支 IG reel 的主張：「100 stocks that pay more than half their profits as dividends」
（@jonerlichman，2026-08 抓取）

做法：影片只在畫面上列公司名，沒有給任何數字，也沒有說 payout ratio 怎麼算。
     所以這支腳本做三件事：
       1. 把畫面 20 張字卡、100 個名字逐一對成股票代號 —— 順便抓出重複
       2. 用 Yahoo Finance 的免費資料，逐檔取 payout ratio（配息 / 每股盈餘）
       3. 自己再算一次（近 12 個月實際配息 / trailing EPS）當交叉驗證
     並標記 REIT —— REIT 依法必須把 90% 以上的應稅所得配出去，
     「配息超過一半盈餘」對 REIT 是結構性必然，不是發現。

資料來源：Yahoo Finance（免費、公開）。執行：python3 payout_check.py
"""
import sys, time, warnings, csv
warnings.filterwarnings('ignore')

try:
    import yfinance as yf
except ImportError:
    sys.exit('請先安裝：pip install yfinance pandas')

# 影片 20 張字卡的原文（依出現順序），name -> ticker
CARDS = [
    [('Broadcom','AVGO'),('Exxon Mobil','XOM'),('J&J','JNJ'),('Abbvie','ABBV'),('Home Depot','HD')],
    [('Coca-Cola','KO'),('UnitedHealth','UNH'),('IBM','IBM'),('Cisco','CSCO'),('Philip Morris','PM')],
    [('TD Bank','TD'),('Intuit','INTU'),('Verizon','VZ'),('Blackstone','BX'),('BlackRock','BLK')],
    [('Texas Instruments','TXN'),('Enbridge','ENB'),('Pfizer','PFE'),('Welltower','WELL'),('Bank of Montreal','BMO')],
    [('Analog Devices','ADI'),('Southern Copper','SCCO'),('ConocoPhillips','COP'),('ADP','ADP'),('CME Group','CME')],
    [('Duke Energy','DUK'),('Bristol-Myers Squibb','BMY'),('Can Nat Resources','CNQ'),('UPS','UPS'),('Marsh & McLennan','MMC')],
    [('Waste Management','WM'),('Equinix','EQIX'),('TC Energy','TRP'),('Johnson Controls','JCI'),('Mondelez','MDLZ')],
    [('Illinois Tool Works','ITW'),('Imperial Oil','IMO'),('Amer Electric Power','AEP'),('Arthur J Gallagher','AJG'),('Simon Property','SPG')],
    [('Digital Realty Trust','DLR'),('Thomson Reuters','TRI'),('Kinder Morgan','KMI'),('Air Products & Chemicals','APD'),('Dominion Energy','D')],
    [('Public Storage','PSA'),('Xcel Energy','XEL'),('Fastenal','FAST'),('Xcel Energy','XEL'),('Restaurant Brands','QSR')],
    [('Target','TGT'),('YUM! Brands','YUM'),('Paychex','PAYX'),('Occidental Petroleum','OXY'),('Crown Castle','CCI')],
    [('Sysco','SYY'),('Ventas','VTR'),('Consolidated Edison','ED'),('Cognizant Tech','CTSH'),('Hershey','HSY')],
    [('Brookfield Infrastructure','BIP'),('Iron Mountain','IRM'),('Pembina Pipeline','PBA'),('Humana','HUM'),('Extra Space Storage','EXR')],
    [('P&G','PG'),('Chevron','CVX'),('RB Global','RBA'),('Ester Lauder','EL'),('VICI Properties','VICI')],
    [('Kimberly-Clark','KMB'),('NRG Energy','NRG'),('Nutrien','NTR'),('Fortis','FTS'),('Sempra','SRE')],
    [('Starbucks','SBUX'),('Altria','MO'),('PepsiCo','PEP'),("McDonald's",'MCD'),('Williams Cos','WMB')],
    [('Colgate-Palmolive','CL'),('FedEx','FDX'),('Abbott Labs','ABT'),('Becton Dickinson','BDX'),('Scotiabank','BNS')],
    [('Medtronic','MDT'),('Brookfield','BN'),('Accenture','ACN'),('ONEOK','OKE'),('Rockwell Automation','ROK')],
    [('Cenovus Energy','CVE'),('Prologis','PLD'),('American Tower','AMT'),('Thomson Reuters','TRI'),('Philips 66','PSX')],
    [('Nike','NKE'),('Corning','GLW'),('Archer Daniels Midland','ADM'),('MPLX','MPLX'),('Ares Management','ARES')],
]

THRESHOLD = 0.50   # 影片主張：配息 > 一半的盈餘

def main():
    slots = [(c+1, n, t) for c, card in enumerate(CARDS) for n, t in card]
    print(f'畫面字卡：{len(CARDS)} 張 × 5 個名字 = {len(slots)} 個位置')

    seen, dupes = {}, []
    for card, name, tk in slots:
        key = tk
        if key in seen:
            dupes.append((name, tk, seen[key], card))
        else:
            seen[key] = card
    print(f'唯一公司：{len(seen)} 家')
    for name, tk, first, again in dupes:
        print(f'  ⚠ 重複：{name} ({tk}) 出現在第 {first} 張與第 {again} 張字卡')
    print()

    rows = []
    for i, (tk, card) in enumerate(sorted(seen.items(), key=lambda kv: kv[1]), 1):
        name = next(n for c, n, t in slots if t == tk)
        try:
            info = yf.Ticker(tk).info
        except Exception as e:
            rows.append(dict(ticker=tk, name=name, err=str(e)[:40])); continue

        pr   = info.get('payoutRatio')
        eps  = info.get('trailingEps')
        rate = info.get('dividendRate')
        sec  = info.get('sector') or ''
        ind  = info.get('industry') or ''
        is_reit = sec == 'Real Estate' or 'REIT' in ind.upper()

        # 自己再算一次：宣告年配息 / trailing EPS
        own = (rate / eps) if (rate and eps and eps > 0) else None

        if pr is None or eps is None or eps <= 0:
            verdict = 'N/A'          # 盈餘為負或缺資料 → 比率沒有意義
        elif pr > THRESHOLD:
            verdict = 'PASS'
        else:
            verdict = 'FAIL'

        rows.append(dict(card=card, ticker=tk, name=name, sector=sec, industry=ind,
                         reit=is_reit, payout_yf=pr, eps=eps, div_rate=rate,
                         payout_own=own, verdict=verdict))
        if i % 10 == 0:
            print(f'  … 已查 {i}/{len(seen)}', flush=True)
        time.sleep(0.15)

    ok   = [r for r in rows if r.get('verdict') == 'PASS']
    bad  = [r for r in rows if r.get('verdict') == 'FAIL']
    na   = [r for r in rows if r.get('verdict') == 'N/A']
    reit = [r for r in rows if r.get('reit')]

    print('\n' + '=' * 72)
    print(f'查得資料 {len(rows)} 家')
    print(f'  配息 > 50% 盈餘（主張成立）：{len(ok)}')
    print(f'  配息 ≤ 50% 盈餘（主張不成立）：{len(bad)}')
    print(f'  無法計算（盈餘為負或缺資料）：{len(na)}')
    print(f'  其中屬 REIT／房地產（配息 >50% 為法規結構性必然）：{len(reit)}')

    if bad:
        print('\n── 反例：畫面點名了，但配息並沒有超過一半盈餘 ──')
        print(f'{"代號":<7}{"公司":<26}{"payout":>9}   產業')
        for r in sorted(bad, key=lambda r: r['payout_yf']):
            print(f'{r["ticker"]:<7}{r["name"][:25]:<26}{r["payout_yf"]*100:>8.1f}%   {r["industry"][:28]}')

    if na:
        print('\n── 無法判定 ──')
        for r in na:
            print(f'{r["ticker"]:<7}{r["name"][:25]:<26}eps={r["eps"]}')

    with open('payout_check.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    print('\n→ 明細已寫入 payout_check.csv')

if __name__ == '__main__':
    main()

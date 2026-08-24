import yfinance as yf, pandas as pd, numpy as np
pd.set_option('display.width',200)

TICK = ["MU","NVDA","AAPL","TSLA","SPY"]
END = pd.Timestamp.today().normalize()
START = END - pd.Timedelta(days=100)   # 近約 3 個月

rows=[]
for t in TICK:
    df = yf.download(t, start=START, end=END, interval="1d",
                     auto_adjust=False, progress=False, threads=False)
    if df.empty: print(t,"no data"); continue
    if isinstance(df.columns, pd.MultiIndex): df.columns = df.columns.get_level_values(0)
    df = df.dropna(subset=["Open","Close"])
    o, c = df["Open"].values, df["Close"].values
    # 隔夜 = 前一日收盤 -> 今日開盤 ; 日內 = 今日開盤 -> 今日收盤
    overnight = o[1:]/c[:-1] - 1
    intraday  = c[1:]/o[1:]  - 1
    total     = c[1:]/c[:-1] - 1
    n=len(overnight)
    cum = lambda r: np.prod(1+r)-1
    rows.append(dict(ticker=t, n_days=n,
        隔夜累積=cum(overnight), 日內累積=cum(intraday), 實際總報酬=cum(total),
        隔夜勝率=(overnight>0).mean(), 日內勝率=(intraday>0).mean(),
        隔夜日均=overnight.mean(), 日內日均=intraday.mean()))
r = pd.DataFrame(rows)
print(f"\n=== 期間 {START.date()} ~ {END.date()}（約 3 個月）===")
for _,x in r.iterrows():
    print(f"\n{x.ticker}  ({int(x.n_days)} 個交易日)")
    print(f"  只做隔夜（收盤買、開盤賣）: {x.隔夜累積*100:+7.2f}%   勝率 {x.隔夜勝率*100:.1f}%")
    print(f"  只做日內（開盤買、收盤賣）: {x.日內累積*100:+7.2f}%   勝率 {x.日內勝率*100:.1f}%")
    print(f"  實際總報酬（買著不動）    : {x.實際總報酬*100:+7.2f}%")
    print(f"  驗算 (1+隔夜)*(1+日內)-1  : {((1+x.隔夜累積)*(1+x.日內累積)-1)*100:+7.2f}%  ← 應等於總報酬")
r.to_csv('/tmp/ovtest.csv',index=False)

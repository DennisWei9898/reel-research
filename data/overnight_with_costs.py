import yfinance as yf, pandas as pd, numpy as np
TICK=["MU","NVDA","AAPL","TSLA","SPY"]
END=pd.Timestamp.today().normalize(); START=END-pd.Timedelta(days=100)
print(f"{'股票':<6}{'隔夜(無成本)':>14}{'扣10bps':>11}{'扣30bps':>11}{'買著不動':>11}")
print("-"*56)
for t in TICK:
    df=yf.download(t,start=START,end=END,interval="1d",auto_adjust=False,progress=False,threads=False)
    if isinstance(df.columns,pd.MultiIndex): df.columns=df.columns.get_level_values(0)
    df=df.dropna(subset=["Open","Close"]); o,c=df["Open"].values,df["Close"].values
    ov=o[1:]/c[:-1]-1; tot=c[1:]/c[:-1]-1; n=len(ov)
    cum=lambda r: (np.prod(1+r)-1)*100
    print(f"{t:<6}{cum(ov):>13.2f}%{cum(ov-0.0010):>10.2f}%{cum(ov-0.0030):>10.2f}%{cum(tot):>10.2f}%")
print("-"*56)
print(f"（每天進出一次 = {n} 趟來回。10bps=萬分之10、30bps=萬分之30，是散戶合理的來回成本區間）")

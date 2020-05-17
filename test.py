from binance.client import Client
from indicators import *
import pandas as pd
import mplfinance as mpf

btc_usdt = import_data('BTCUSDT', 'd', '2020-01-01', '2020-04-17')

x = 0

if x:
       adp = [mpf.make_addplot(ema(btc_usdt['Close'], 7)),
       mpf.make_addplot(ema(btc_usdt['Close'], 30))]
else:
       adp = mpf.make_addplot(macd(btc_usdt['Close']))


mpf.plot(btc_usdt, type='candle', addplot=adp)
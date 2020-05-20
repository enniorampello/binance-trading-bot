from binance.client import Client
from indicators import *
import mplfinance as mpf

btc_usdt = import_data('BTCUSDT', '1h', '2020-04-10', '2020-04-17')

x = 0

if x:
       adp = [mpf.make_addplot(ema(btc_usdt['Close'], 7)),
       mpf.make_addplot(ema(btc_usdt['Close'], 30))]
else:
       adp = mpf.make_addplot(macd(btc_usdt['Close']),panel='lower')


mpf.plot(btc_usdt, type='candle', addplot=adp)
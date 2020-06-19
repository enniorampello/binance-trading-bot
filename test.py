from binance.client import Client
from indicators import *
import import_data
from datetime import datetime
import backtrader as bt
import time
import os

epoch = 1591056001000 / 1000
print(time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(epoch)))
date = datetime.fromtimestamp(epoch)
print(date)

os.mkdir('./ETHBTC')
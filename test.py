from binance.client import Client
from indicators import *
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'./BTCUSDT/training-data-1d.csv')

print(data['Close'].iloc[-1])
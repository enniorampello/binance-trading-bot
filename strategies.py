import  backtrader as bt
from backtrader.indicators import ExponentialMovingAverage

class GoldenCross(bt.Strategy):
    params = (
        ('ema1', 7),
        ('ema2', 30),
    )
    def __init__(self):
        self.ema1 = ExponentialMovingAverage(data=self.data, period=self.p.ema1)
        self.ema2 = ExponentialMovingAverage(data=self.data, period=self.p.ema2)
        self.long = False

    def next(self):
        if self.env.cash <= 0:
            print('baaaaaaankruptttttt')
        position_size = (self.env.cash * 0.5)/self.data.close
        if not self.long and self.ema1 > self.ema2:
            self.buy(size=position_size)
            self.long = True
        elif self.long and self.ema1 < self.ema2:
            self.sell(size=position_size)
            self.long = False
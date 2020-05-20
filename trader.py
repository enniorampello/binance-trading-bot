from indicators import *


class position:
    LONG = True
    SHORT = False

class Trade:

    # in the argument pos, pass position.LONG or position.SHORT
    # TODO understand if it is better to pass directly the quantity or pass the amount and then convert it into a quantity in the __init__
    def __init__(self, symbol: str, pos: bool, quantity: float):
        self.symbol = symbol
        self.pos = pos
        self.quantity = quantity


class Trader:

    def __init__(self, initial_capital: int, symbol='BTCUSDT', time_window=100, start_date='2019-01-01', end_date='2020-04-15', timestamp='1h'):
        self.df = import_data(symbol, timestamp, from_date=start_date, to_date=end_date)
        self.df_window = self.df.tail(time_window) # TODO the idea is to start from the bottom of the df and have an iterator that brings the window towards the top, doing the trades meanwhile
        self.capital = initial_capital
        self.trades = []


    def long(self, symbol, amount):
        self.trades.append(Trade(symbol, position.LONG, ))

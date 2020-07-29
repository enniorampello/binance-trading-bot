import pandas as pd
import datetime
from pathlib import Path
from datetime import timedelta
from import_data import symbols_and_start_dates
from strategy import Strategy

timestamps = ['5min', '15min', '30min', '1h', '2h', '4h', '6h', '12h', '1d']

class Mode:
    TEST = 0
    VALIDATION = 1

class Backtester:

    def __init__(self):
        self.data = None
        self.strategy = None
        
        self.mode = Mode.TEST
        self.initial_capital = 10000
        
        
        # STATISTICS: indicators of the performance of the strategy
        self.max_drawdown = 0
        self.profit_trades = 0
        self.loss_trades = 0
        self.percent_win = 0
        self.avg_drawdown = 0
        self.sharpe_ratio = 0
        self.risk_to_reward = 0

        # STATE VARIABLES
        self.trades = []
        self.current_capital = 10000
        self.current_date = None
        self.current_coins = 0

    def add_data(self, symbol='BTCUSDT', timestamp='2h', mode=0):
        if timestamp not in timestamps:
            print('Timestamp error: wrong format.')
            return
        
        data_path = Path.cwd() / f'data/{symbol}/training-data-{timestamp}.csv'
        from_date = datetime.datetime.strptime(symbols_and_start_dates.get(symbol), '%Y-%m-%d')
        if mode == Mode.VALIDATION:
            from_date = from_date + timedelta(days=521)
        to_date = from_date + timedelta(days=520)
        
        self.current_date = from_date

        df = pd.read_csv(data_path)
        df['OpenTime'] = pd.to_datetime(df['Open time'])
        df = df.drop(['Open time'], axis=1)
        df = df[(df.OpenTime >= from_date) & (df.OpenTime <= to_date)]
        df = df.set_index('OpenTime')

        self.data = df
        
    def add_strategy(self, strategy):
        self.strategy = strategy
        self.strategy.backtester = self

    def run(self):
        


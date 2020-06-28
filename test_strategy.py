import backtrader as bt
from backtrader import observers as obs
import datetime
from datetime import timedelta
from import_data import symbols_and_start_dates
from strategies import GoldenCross, TrailCross

class BackTester:

    def __init__(self, strategy: bt.Strategy):
        self.strategy = strategy
        self.cerebro = bt.Cerebro()
        self.cerebro.broker.setcommission(commission=0.001)
        self.symbol = 'BTCUSDT'
        self.timestamp = '30min'
        self.opt = False
        self.data_path = None
        self.from_date = None
        self.to_date = None
        self.data = None

    def set_data(self, days_after_start_date, tot_days_window):
        self.data_path = f'./data/{self.symbol}/training-data-{self.timestamp}.csv'
        
        self.from_date = datetime.datetime.strptime(symbols_and_start_dates.get(self.symbol), '%Y-%m-%d')
        self.from_date = self.from_date + timedelta(days=days_after_start_date)
        self.to_date = self.from_date + timedelta(days=tot_days_window)

        self.data = bt.feeds.GenericCSVData(dataname=self.data_path,
                                    fromdate=self.from_date,
                                    todate=self.to_date,
                                    dtformat= '%Y-%m-%d %H:%M:%S',
                                    timeframe= bt.TimeFrame.Ticks,
                                    datetime=0,
                                    high=1,
                                    low=2,
                                    open=3,
                                    close=4,
                                    volume=5,
                                    openinterest=-1
                                    )
        self.cerebro.adddata(self.data)

    def run_strategy(self):
        if self.opt:
            self.run_opt()
        else:
            self.cerebro.addstrategy(self.strategy)
            print(f'Starting Portfolio Value: {self.cerebro.broker.getvalue()}')
            self.cerebro.run()
            print(f'Final Portfolio Value: {self.cerebro.broker.getvalue()}')
            self.cerebro.plot()

    def run_opt(self):
        if self.strategy is GoldenCross:

            '''
            period1_1 = int(input('Set lower bound for the short EMA: '))
            period1_2 = int(input('Set upper bound for the short EMA: '))
            period2_1 = int(input('Set lower bound for the long EMA: '))
            period2_2 = int(input('Set upper bound for the long EMA: '))
            
            self.cerebro.optstrategy(
                GoldenCross,
                period1=range(period1_1,period1_2),
                period2=range(period2_1, period2_2)
            )
            '''
            self.cerebro.optstrategy(
                GoldenCross,
                period1=range(17, 21),
                period2=range(39, 43)
            )

            self.cerebro.run()
        elif self.strategy is TrailCross:
            # TODO complete the TrailCross strategy
            period1_1, period1_2 = input('Set the range for the short EMA: ').split()
            period2_1, period2_2 = input('Set the range for the long EMA: ').split()
            is_percent = input('Type 1 to set percent or type 0 to set amount: ')

            if is_percent == 1:
                #TODO implement input management with percentage mode
                pass
            else:
                tp_amount1, tp_amount2 = input('Set the range for take-profit amount (default 4.0): ').split()
                sl_amount1, sl_amount2 = input('Set the range for stop-loss amount (default 1.5): ').split()
                self.cerebro.optstrategy(
                    self.strategy,
                    period1=range(int(period1_1),int(period1_2)),
                    period2=range(int(period2_1),int(period2_2)),
                    tp_amount=range(int(tp_amount1),int(tp_amount2)),
                    sl_amount=range(int(sl_amount1),int(sl_amount2))
                )

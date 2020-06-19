import backtrader as bt
import datetime
from datetime import timedelta
from import_data import symbols_and_start_dates
from strategies import *

def run_strategy(strategy: bt.Strategy, symbol='BTCUSDT', timestamp='30min'):
    #initial_capital = input('Insert initial capital: ')
    data_path = f'./data/{symbol}/training-data-{timestamp}.csv'

    cerebro = bt.Cerebro()
    #cerebro.broker.set_cash(initial_capital)
    cerebro.broker.setcommission(commission=0.001)
    cerebro.optstrategy(strategy, period1=range(5, 20), period2=range(25, 50))
    #cerebro.addstrategy(strategy)

    from_date = datetime.datetime.strptime(symbols_and_start_dates.get(symbol), '%Y-%m-%d') + timedelta(days=365)
    to_date = from_date + timedelta(days=180)
    data = bt.feeds.GenericCSVData(dataname=data_path,
                                   fromdate=from_date,
                                   todate=to_date,
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
    cerebro.adddata(data)
    print(f'Starting Portfolio Value: {cerebro.broker.getvalue()}')
    cerebro.run()
    print(f'Final Portfolio Value: {cerebro.broker.getvalue()}')
    #cerebro.plot()

if __name__ == '__main__':
    run_strategy(GoldenCross, symbol='BTCUSDT', timestamp='5min')
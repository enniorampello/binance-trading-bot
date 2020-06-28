from binance.client import Client
import import_data
from import_data import symbols_and_start_dates
import datetime
import backtrader as bt
from datetime import timedelta
from strategies import TrailCross, GoldenCross

def test_strategy(strategy: bt.Strategy, symbol='BTCUSDT', timestamp='30min', days_after_start_date=365, tot_days_window=180, opt=False):
    cerebro = bt.Cerebro()
    cerebro.broker.setcommission(commission=0.001)

    data_path = f'./data/{symbol}/training-data-{timestamp}.csv'

    from_date = datetime.datetime.strptime(symbols_and_start_dates.get(symbol), '%Y-%m-%d')
    from_date = from_date + timedelta(days=days_after_start_date)
    to_date = from_date + timedelta(days=tot_days_window)

    data = bt.feeds.GenericCSVData(dataname=data_path,
                                        fromdate=from_date,
                                        todate=to_date,
                                        dtformat='%Y-%m-%d %H:%M:%S',
                                        timeframe=bt.TimeFrame.Ticks,
                                        datetime=0,
                                        high=1,
                                        low=2,
                                        open=3,
                                        close=4,
                                        volume=5,
                                        openinterest=-1
                                        )
    cerebro.adddata(data)

    if strategy is GoldenCross:
        period1_1 = int(input('Set lower bound for the short EMA: '))
        period1_2 = int(input('Set upper bound for the short EMA: '))
        period2_1 = int(input('Set lower bound for the long EMA: '))
        period2_2 = int(input('Set upper bound for the long EMA: '))

        self.cerebro.optstrategy(
            GoldenCross,
            period1=range(period1_1,period1_2),
            period2=range(period2_1, period2_2)
        )
    elif strategy is TrailCross:
        # TODO complete the TrailCross strategy
        period1_1, period1_2 = input('Set the range for the short EMA: ').split()
        period2_1, period2_2 = input('Set the range for the long EMA: ').split()
        is_percent = input('Type 1 to set percent or type 0 to set amount: ')

        if is_percent == 1:
            # TODO implement input management with percentage mode
            pass
        else:
            tp_amount1, tp_amount2 = input('Set the range for take-profit amount (default 4.0): ').split()
            sl_amount1, sl_amount2 = input('Set the range for stop-loss amount (default 1.5): ').split()
            cerebro.optstrategy(
                strategy,
                period1=range(int(period1_1), int(period1_2)),
                period2=range(int(period2_1), int(period2_2)),
                tp_amount=range(int(tp_amount1), int(tp_amount2)),
                sl_amount=range(int(sl_amount1), int(sl_amount2))
            )
    cerebro.run()


if __name__ == '__main__':
    test_strategy(TrailCross, opt=True)
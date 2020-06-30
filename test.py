from binance.client import Client
import import_data
from import_data import symbols_and_start_dates
import datetime
from pathlib import Path
import backtrader as bt
from datetime import timedelta
from strategies import TrailCross, GoldenCross, BollingerBandsStrategy

timestamps = ['5min', '15min', '30min', '1h', '2h', '4h', '6h', '12h', '1d']

def get_timeframe(timestamp: str):
    result = []

    if timestamp.find('min') != -1:
        result.append(bt.TimeFrame.Minutes)
        if timestamp.find('15') != -1:
            result.append(15)
        elif timestamp.find('30') != -1:
            result.append(30)
        elif timestamp.find('5') != -1:
            result.append(5)
    elif timestamp.find('h') != -1:
        result.append(bt.TimeFrame.Minutes)
        if timestamp.find('12') != -1:
            result.append(720)
        elif timestamp.find('6') != -1:
            result.append(360)
        elif timestamp.find('4') != -1:
            result.append(240)
        elif timestamp.find('2') != -1:
            result.append(120)
        elif timestamp.find('1') != -1:
            result.append(60)
    elif timestamp.find('d') != -1:
        result.append([bt.TimeFrame.Days, 1])

    return result

def test_strategy(strategy: bt.Strategy, symbol='BTCUSDT', timestamp='30min', days_after_start_date=365, tot_days_window=180, opt=False, multi_timestamp=False):
    current_path = Path.cwd()

    if timestamp not in timestamps:
        print('Timestamp error: wrong format.')
        return
    
    if not multi_timestamp:
        cerebro = bt.Cerebro()
        cerebro.broker.setcommission(commission=0.001)

        data_path = current_path / f'data/{symbol}/training-data-{timestamp}.csv'

        from_date = datetime.datetime.strptime(symbols_and_start_dates.get(symbol), '%Y-%m-%d')
        from_date = from_date + timedelta(days=days_after_start_date)
        to_date = from_date + timedelta(days=tot_days_window)

        data = bt.feeds.GenericCSVData(
            dataname=data_path,
            fromdate=from_date,
            todate=to_date,
            dtformat='%Y-%m-%d %H:%M:%S',
            timeframe=get_timeframe(timestamp)[0],
            compression=get_timeframe(timestamp)[1],
            datetime=0,
            high=1,
            low=2,
            open=3,
            close=4,
            volume=5,
            openinterest=-1
            )
        cerebro.adddata(data)

        if opt:
            if strategy is GoldenCross:
                period1_1 = int(input('Set lower bound for the short EMA: '))
                period1_2 = int(input('Set upper bound for the short EMA: '))
                period2_1 = int(input('Set lower bound for the long EMA: '))
                period2_2 = int(input('Set upper bound for the long EMA: '))

                cerebro.optstrategy(
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
            elif strategy is BollingerBandsStrategy:
                period = input("Insert the period range for the Bollinger Bands: ").split()
                distance = input('Insert the range for the minimum distam=nce from the bands: ').split()
                stop_loss = input('Insert the range for the stop loss percentage: ').split()
                cerebro.optstrategy(
                    strategy,
                    period=range(int(period[0]),int(period[1])),
                    distance=range(int(distance[0]),int(distance[1])),
                    stoploss=range(int(stop_loss[0]),int(stop_loss[1]))
                )
        else:
            cerebro.addstrategy(strategy)
        cerebro.run()
        if not opt:
            cerebro.plot()
    
    elif multi_timestamp:
        for tmstmp in timestamps:
            cerebro = bt.Cerebro()
            cerebro.broker.setcommission(commission=0.001)

            data_path = current_path / f'data/{symbol}/training-data-{tmstmp}.csv'

            from_date = datetime.datetime.strptime(symbols_and_start_dates.get(symbol), '%Y-%m-%d')
            from_date = from_date + timedelta(days=days_after_start_date)
            to_date = from_date + timedelta(days=tot_days_window)

            data = bt.feeds.GenericCSVData(
                dataname=data_path,
                fromdate=from_date,
                todate=to_date,
                dtformat='%Y-%m-%d %H:%M:%S',
                timeframe=get_timeframe(tmstmp)[0],
                compression=get_timeframe(tmstmp)[1],
                datetime=0,
                high=1,
                low=2,
                open=3,
                close=4,
                volume=5,
                openinterest=-1,
                )
            cerebro.adddata(data)
            cerebro.addstrategy(strategy)
            cerebro.run()
            cerebro.plot()




if __name__ == '__main__':

    test_strategy(BollingerBandsStrategy, multi_timestamp=False, timestamp='4h')
from binance.client import Client
from datetime import datetime
import pandas as pd
import os

symbols_and_start_dates = {'BTCUSDT': '2018-01-01',
                               'ETHUSDT': '2018-01-01',
                               'BNBUSDT': '2018-01-01',
                               'ETHBTC':  '2018-01-01',
                               'BNBBTC':  '2018-01-01',
                               'BNBETH':  '2018-01-01',
                               'TRXETH':  '2018-01-01',
                               'EOSETH':  '2018-01-01',
                               'XRPBTC':  '2018-01-01',
                               'EOSBTC':  '2018-01-01',
                               'TRXBTC':  '2018-01-01',
                               'LTCBTC':  '2018-01-01',
                               'EOSUSDT': '2018-07-02',
                               'XRPUSDT': '2018-07-02',
                               'TRXUSDT': '2018-07-02',
                               'LTCUSDT': '2018-01-01'
                               }

def kline_to_csv(kline, symbol, file_name):
    """
    function to generate a dataframe from the kline and creates a .csv
    :return: pd.DataFrame containing ohlcv historical data
    """
    print(f'\tcreating file "{file_name}" in folder "{symbol}"')
    df = pd.DataFrame(kline)
    df.columns = ['Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time', 'Quote asset volume',
                  'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'Can be ignored']
    df = df[['Open time', 'Open', 'High', 'Low', 'Close', 'Volume']].astype(float).round(2)
    df['Open time'] = df['Open time'].apply(lambda x: datetime.fromtimestamp(x/1000))
    open(f'./{symbol}/{file_name}.csv', 'w')
    df.to_csv(f'./{symbol}/{file_name}.csv', index=False,
              columns=['Open time', 'Open', 'High', 'Low', 'Close', 'Volume'])
    print('import complete.')
    return df

"""
keys.txt is a text file containing api keys for security purposes. It is formatted as follows:
public_binance_api_key
secret_binance_api_key
"""

with open('./<path-to-keys-file>' ,'r') as keys:
    lines = keys.readlines()
    PUBLIC_KEY = lines[0].replace('\n' ,'')
    PRIVATE_KEY = lines[1]

client = Client(PUBLIC_KEY ,PRIVATE_KEY)

def import_data_1m(symbol='BTCUSDT', start_date='1 month ago', end_date=None):
    """
    this function retrieves data for the last month with a 1-min timestamp
    it generates a .csv file with approximately 43081 tuples
    :return: pd.Dataframe containing ohlcv historical data
    """
    print(f'fetching {symbol} data...')
    kline = client.get_historical_klines(symbol=symbol,
                                         interval=Client.KLINE_INTERVAL_1MINUTE,
                                         start_str=start_date,
                                         end_str=end_date)
    print('\tgenerating .csv file...')
    return kline_to_csv(kline, symbol, 'training-data-1min')

def import_data_5m(symbol='BTCUSDT', start_date='2 month ago', end_date=None):
    """
    this function retrieves data from the last 2 months with a 5-min timestamp
    it generates a .csv file with approximately 17514 tuples
    :return: pd.Dataframe containing ohlcv historical data
    """
    print(f'fetching {symbol} data...')
    kline = client.get_historical_klines(symbol=symbol,
                                         interval=Client.KLINE_INTERVAL_5MINUTE,
                                         start_str=start_date,
                                         end_str=end_date)
    print('\tgenerating .csv file...')
    return kline_to_csv(kline, symbol, 'training-data-5min')

def import_data_15m(symbol='BTCUSDT', start_date='1 year ago', end_date=None):
    """
    this function retrieves data from the last year with a 15-min timestamp
    it generates a .csv file with approximately 35030 tuples
    :return: pd.Dataframe containing ohlcv historical data
    """
    print(f'fetching {symbol} data...')
    kline = client.get_historical_klines(symbol=symbol,
                                         interval=Client.KLINE_INTERVAL_15MINUTE,
                                         start_str=start_date,
                                         end_str=end_date)
    print('\tgenerating .csv file...')
    return kline_to_csv(kline, symbol, 'training-data-15min')

def import_data_30m(symbol='BTCUSDT', start_date='1 year ago', end_date=None):
    """
    this function retrieves data from the last year with a 30-min timestamp
    it generates a .csv file with approximately 17517 tuples
    :return: pd.Dataframe containing ohlcv historical data
    """
    print(f'fetching {symbol} data...')
    kline = client.get_historical_klines(symbol=symbol,
                                         interval=Client.KLINE_INTERVAL_30MINUTE,
                                         start_str=start_date,
                                         end_str=end_date)
    print('\tgenerating .csv file...')
    return kline_to_csv(kline, symbol, 'training-data-30min')

def import_data_1h(symbol='BTCUSDT', start_date='1 year ago', end_date=None):
    """
    this function retrieves data from the last year with a 1-hour timestamp
    it generates a .csv file with approximately 8761 tuples
    :return: pd.Dataframe containing ohlcv historical data
    """
    print(f'fetching {symbol} data...')
    kline = client.get_historical_klines(symbol=symbol,
                                         interval=Client.KLINE_INTERVAL_1HOUR,
                                         start_str=start_date,
                                         end_str=end_date)
    print('\tgenerating .csv file...')
    return kline_to_csv(kline, symbol, 'training-data-1h')

def import_data_2h(symbol='BTCUSDT', start_date='1 year ago', end_date=None):
    """
    this function retrieves data from the last year with a 2-hour timestamp
    it generates a .csv file with approximately 4382 tuples
    :return: pd.Dataframe containing ohlcv historical data
    """
    print(f'fetching {symbol} data...')
    kline = client.get_historical_klines(symbol=symbol,
                                         interval=Client.KLINE_INTERVAL_2HOUR,
                                         start_str=start_date,
                                         end_str=end_date)
    print('\tgenerating .csv file...')
    return kline_to_csv(kline, symbol, 'training-data-2h')

def import_data_4h(symbol='BTCUSDT', start_date='1 year ago', end_date=None):
    """
    this function retrieves data from the last year with a 4-hour timestamp
    it generates a .csv file with approximately 2194 tuples
    :return: pd.Dataframe containing ohlcv historical data
    """
    print(f'fetching {symbol} data...')
    kline = client.get_historical_klines(symbol=symbol,
                                         interval=Client.KLINE_INTERVAL_4HOUR,
                                         start_str=start_date,
                                         end_str=end_date)
    print('\tgenerating .csv file...')
    return kline_to_csv(kline, symbol, 'training-data-4h')

def import_data_6h(symbol='BTCUSDT', start_date='1 year ago', end_date=None):
    """
    this function retrieves data from the last year with a 6-hour timestamp
    it generates a .csv file with approximately 1464 tuples
    :return: pd.Dataframe containing ohlcv historical data
    """
    print(f'fetching {symbol} data...')
    kline = client.get_historical_klines(symbol=symbol,
                                         interval=Client.KLINE_INTERVAL_6HOUR,
                                         start_str=start_date,
                                         end_str=end_date)
    print('\tgenerating .csv file...')
    return kline_to_csv(kline, symbol, 'training-data-6h')

def import_data_12h(symbol='BTCUSDT', start_date='1 year ago', end_date=None):
    """
    this function retrieves data from the last year with a 12-hour timestamp
    it generates a .csv file with approximately 732 tuples
    :return: pd.Dataframe containing ohlcv historical data
    """
    print(f'fetching {symbol} data...')
    kline = client.get_historical_klines(symbol=symbol,
                                         interval=Client.KLINE_INTERVAL_12HOUR,
                                         start_str=start_date,
                                         end_str=end_date)
    print('\tgenerating .csv file...')
    return kline_to_csv(kline, symbol, 'training-data-12h')

def import_data_1d(symbol='BTCUSDT', start_date='1 year ago', end_date=None):
    """
    this function retrieves data from the last year with a 1-day timestamp
    it generates a .csv file with approximately 366 tuples
    :return: pd.Dataframe containing ohlcv historical data
    """
    print(f'fetching {symbol} data...')
    kline = client.get_historical_klines(symbol=symbol,
                                         interval=Client.KLINE_INTERVAL_1DAY,
                                         start_str=start_date,
                                         end_str=end_date)
    print('\tgenerating .csv file...')
    return kline_to_csv(kline, symbol, 'training-data-1d')


if __name__ == '__main__':
    for key in symbols_and_start_dates.keys():
        os.mkdir(f'./{key}')
        import_data_5m(symbol=key, start_date=symbols_and_start_dates.get(key))
        import_data_15m(symbol=key, start_date=symbols_and_start_dates.get(key))
        import_data_30m(symbol=key, start_date=symbols_and_start_dates.get(key))
        import_data_1h(symbol=key, start_date=symbols_and_start_dates.get(key))
        import_data_2h(symbol=key, start_date=symbols_and_start_dates.get(key))
        import_data_4h(symbol=key, start_date=symbols_and_start_dates.get(key))
        import_data_6h(symbol=key, start_date=symbols_and_start_dates.get(key))
        import_data_12h(symbol=key, start_date=symbols_and_start_dates.get(key))
        import_data_1d(symbol=key, start_date=symbols_and_start_dates.get(key))

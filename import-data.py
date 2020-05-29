import pandas as pd
from binance.client import Client


def kline_to_csv(kline, file_name):
    df = pd.DataFrame(kline)
    df.columns = ['Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time', 'Quote asset volume',
                  'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'Can be ignored']
    df = df[['Open', 'High', 'Low', 'Close', 'Volume']]

    open(f'./{file_name}.csv', 'w')
    df.to_csv(f'./{file_name}.csv', index=False,
              columns=['Open', 'High', 'Low', 'Close', 'Volume'])

"""
keys.txt is a text file containing api keys for security purposes. It is formatted as follows:

public_binance_api_key
secret_binance_api_key
"""

with open('./keys.txt' ,'r') as keys:
    lines = keys.readlines()
    PUBLIC_KEY = lines[0].replace('\n' ,'')
    PRIVATE_KEY = lines[1]

client = Client(PUBLIC_KEY ,PRIVATE_KEY)


def import_data_1m():
    """
    this function retrieves data for the last month with a 1-min timestamp

    it generates a .csv file with approximately 43081 tuples
    """
    kline = client.get_historical_klines(symbol='BTCUSDT' ,
                                         interval=Client.KLINE_INTERVAL_1MINUTE,
                                         start_str=f'1 month ago')
    kline_to_csv(kline,'training-data-1min')


def import_data_5m():
    """
    this function retrieves data from the last 2 months with a 5-min timestamp

    it generates a .csv file with approximately 17514 tuples
    """
    print('fetching data...')

    kline = client.get_historical_klines(symbol='BTCUSDT' ,
                                         interval=Client.KLINE_INTERVAL_5MINUTE,
                                         start_str='2 month ago')
    kline_to_csv(kline,'training-data-5min')


def import_data_15m():
    """
    this function retrieves data from the last year with a 15-min timestamp

    it generates a .csv file with approximately 35030 tuples
    """
    print('fetching data...')

    kline = client.get_historical_klines(symbol='BTCUSDT' ,
                                         interval=Client.KLINE_INTERVAL_15MINUTE,
                                         start_str='1 year ago')
    kline_to_csv(kline,'training-data-15min')


def import_data_30m():
    """
    this function retrieves data from the last year with a 30-min timestamp

    it generates a .csv file with approximately 17517 tuples
    """
    print('fetching data...')

    kline = client.get_historical_klines(symbol='BTCUSDT',
                                         interval=Client.KLINE_INTERVAL_30MINUTE,
                                         start_str='1 year ago')
    kline_to_csv(kline,'training-data-30min')


def import_data_1h():
    """
    this function retrieves data from the last year with a 1-hour timestamp

    it generates a .csv file with approximately 8761 tuples
    """
    print('fetching data...')

    kline = client.get_historical_klines(symbol='BTCUSDT',
                                         interval=Client.KLINE_INTERVAL_1HOUR,
                                         start_str='1 year ago')
    kline_to_csv(kline, 'training-data-1h')


def import_data_2h():
    """
    this function retrieves data from the last year with a 2-hour timestamp

    it generates a .csv file with approximately 4382 tuples
    """
    print('fetching data...')

    kline = client.get_historical_klines(symbol='BTCUSDT',
                                         interval=Client.KLINE_INTERVAL_2HOUR,
                                         start_str='1 year ago')
    kline_to_csv(kline, 'training-data-2h')


def import_data_4h():
    """
    this function retrieves data from the last year with a 4-hour timestamp

    it generates a .csv file with approximately 2194 tuples
    """
    print('fetching data...')

    kline = client.get_historical_klines(symbol='BTCUSDT',
                                         interval=Client.KLINE_INTERVAL_4HOUR,
                                         start_str='1 year ago')
    kline_to_csv(kline, 'training-data-4h')


def import_data_6h():
    """
    this function retrieves data from the last year with a 6-hour timestamp

    it generates a .csv file with approximately 1464 tuples
    """
    print('fetching data...')

    kline = client.get_historical_klines(symbol='BTCUSDT',
                                         interval=Client.KLINE_INTERVAL_6HOUR,
                                         start_str='1 year ago')
    kline_to_csv(kline, 'training-data-6h')


def import_data_12h():
    """
    this function retrieves data from the last year with a 12-hour timestamp

    it generates a .csv file with approximately 732 tuples
    """
    print('fetching data...')

    kline = client.get_historical_klines(symbol='BTCUSDT',
                                         interval=Client.KLINE_INTERVAL_12HOUR,
                                         start_str='1 year ago')
    kline_to_csv(kline, 'training-data-12h')


def import_data_1d():
    """
    this function retrieves data from the last year with a 1-day timestamp

    it generates a .csv file with approximately 366 tuples
    """
    print('fetching data...')

    kline = client.get_historical_klines(symbol='BTCUSDT',
                                         interval=Client.KLINE_INTERVAL_1DAY,
                                         start_str='1 year ago')
    kline_to_csv(kline, 'training-data-1d')

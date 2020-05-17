from datetime import datetime
import pandas as pd

def import_data(ticker: str, timestamp: str, from_date: str, to_date: str):
    from_date = datetime.strptime(from_date, '%Y-%m-%d')
    to_date = datetime.strptime(to_date, '%Y-%m-%d')

    if timestamp == '1h':
        parse = lambda x: datetime.strptime(x, '%Y-%m-%d %H-%p')
    else:
        parse = lambda x: datetime.strptime(x, '%Y-%m-%d')

    df = pd.read_csv(f'Crypto Historical Data/Binance_{ticker}_{timestamp}.csv', skiprows=1, parse_dates=['Date'],
                     date_parser=parse)
    df = df.drop('Symbol', axis=1)
    df = df.dropna()

    mask = (df['Date'] > from_date) & (df['Date'] <= to_date)
    df = df.loc[mask]

    df = df.set_index('Date')

    df = df.iloc[::-1]  # reverse the dataframe to print it correctly
    return df

def ema(series: pd.Series, n: int):
    return series.ewm(span=n, min_periods=0, adjust=False, ignore_na=False).mean()

def sma(series: pd.Series, n: int):
    return series.rolling(window=n).mean()

def macd(series, e1=12, e2=26, e3=9):
    ema1 = ema(series, e1)
    ema2 = ema(series, e2)

    macd = ema1 - ema2
    ema3 = ema(macd, e3)

    d = {'macd': macd, 'signal': ema3}

    result = pd.DataFrame(d)
    result = result.set_index(macd.index.values)

    return result

import pandas as pd


def ema(series: pd.Series, n: int):
    return series.ewm(span=n, min_periods=0, adjust=False, ignore_na=False).mean()

def sma(series: pd.Series, n: int):
    return series.rolling(window=n).mean()


# remember to plot the macd using panel='lower' in mpf.make_addplot()
def macd(series: pd.Series, e1=12, e2=26, e3=9):
    ema1 = ema(series, e1)
    ema2 = ema(series, e2)

    macd = ema1 - ema2
    signal = ema(macd, e3)

    d = {'macd': macd, 'signal': signal}

    result = pd.DataFrame(d)
    result = result.set_index(macd.index.values)

    return result

# this function returns the current close price of the given symbol
def close(symbol: pd.DataFrame):
    return symbol['Close'].iloc[-1]

def high(symbol: pd.DataFrame):
    return symbol['High'].iloc[-1]

def low(symbol: pd.DataFrame):
    return symbol['Low'].iloc[-1]

def open_price(symbol: pd.DataFrame):
    return symbol['Open'].iloc[-1]

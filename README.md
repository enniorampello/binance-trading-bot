# BinanceTradingBot

### Introduction
This is a cryptocurrency trading bot built to work on binance exchange.
The main goal of this bot is to **trade automatically on Binance**, and, for doing so, it is necessary to have a [Binance account](https://accounts.binance.com/en/register) and to configure **Binance API keys**.

### Libraries
This bot is developed in Python 3.8 and it's currently based on **these libraries**:
- [`pandas`](https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/)
- [`python-binance`](https://python-binance.readthedocs.io/en/latest/overview.html)
- [`matplotlib`](https://matplotlib.org/tutorials/introductory/pyplot.html)

`python-binance` is currently **fundamental** for the development of the algorithm, since it is used as a **wrapper for the Binance API**.
It is possible, in future, to consider using directly the Binance API through requests made using the [`requests`](https://requests.readthedocs.io/projects/it/it/latest/) library.
For all the information about function calls, parameters and constants, check the documentation [here](https://python-binance.readthedocs.io/en/latest/overview.html).

### Loading data
The file `import-data.py` contains some **functions to request the historical data** (OHLCV: Open, High, Low, Close, Volume) to the *Binance API*. Every function is set to retrieve data of a different format (1min, 5min, 1hour, 1day, etc...). Currently all the functions are set to **retrieve data about BTC/USDT** but they should be set to receive as parameter the symbol and the time window of the data.<br/>
After all the price data is imported from the exchange (through the function `get_historical_klines()` of the `python-binance` wrapper) it is converted into a `pd.DataFrame` (that is returned from the function) and it is also saved into a *.csv* file, in the directory of the project (in order to be used in future without reimporting it).

### Indicators
In the file `indicators.py` there are all the **functions needed to implement a strategy**. To understand what they do, just Google their name and there are a lot of informations around.

### Trader and Trade
These are two classes that should be used for the execution of the algorithm.
The class `Trader` is used to store the following informations:
- **starting capital**: it gives information about all the starting quantities of cryptocurrencies.
- **current capital**: the current state of the capital.
- **% of starting capital available**: it is a measure of how well the algorithm is performing. If it's above 100 we have a positive return, otherwise we are having a loss.
- **% of capital per trade**: it is a value that tells how much of the available capital should be involved in each trade.
- **open trades***: it stores all the informations about the current open trades.
- **trades history****: a set of all the past trades and the related informations.

### TODO
- Modify the functions of `import-data.py` to set the index of the DataFrame and the *.csv* file to be the correct datetime of the tuple (Google *epoch*).
- Modify the functions of `import-data.py` to receive as parameters the *symbol*, the *start_date* and the (optional) *end_date*. If the *end_date* is not given, the default should be the current date.
- Implement all the missing attributes and methods of the classes `Trade` and `Trader`.
- Develop an initial strategy to test the execution of the algorithm on historical data.

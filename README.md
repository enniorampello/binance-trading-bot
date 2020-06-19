# BinanceTradingBot

### Introduction
This is a cryptocurrency trading bot built to work on binance exchange.
The main goal of this bot is to **trade automatically on Binance**, and, for doing so, it is necessary to have a [Binance account](https://accounts.binance.com/en/register) and to configure **Binance API keys**.

### Libraries
This bot is developed in Python 3.8 and it's currently based on **these libraries**:
- [`pandas`](https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/)
- [`python-binance`](https://python-binance.readthedocs.io/en/latest/overview.html)
- [`matplotlib`](https://matplotlib.org/tutorials/introductory/pyplot.html)
- [`backtrader`](https://www.backtrader.com/docu/)

`python-binance` is currently **fundamental** for the development of the algorithm, since it is used as a **wrapper for the Binance API**.
It is possible, in future, to consider using directly the Binance API through requests made using the [`requests`](https://requests.readthedocs.io/projects/it/it/latest/) library.
For all the information about function calls, parameters and constants, check the documentation [here](https://python-binance.readthedocs.io/en/latest/overview.html).

### Loading data
The file `import-data.py` contains some **functions to request the historical data** (OHLCV: Open, High, Low, Close, Volume) to the *Binance API*. Every function is set to retrieve data of a different format (1min, 5min, 1hour, 1day, etc...). Currently all the functions are set to **retrieve data about BTC/USDT** but they should be set to receive as parameter the symbol and the time window of the data.<br/>
After all the price data is imported from the exchange (through the function `get_historical_klines()` of the `python-binance` wrapper) it is converted into a `pd.DataFrame` (that is returned from the function) and it is also saved into a *.csv* file, in the directory of the project (in order to be used in future without reimporting it).

### Indicators
In the file `indicators.py` there are all the **functions needed to implement a strategy**. To understand what they do, just Google their name and there are a lot of informations around.

### Backtesting
Until there are no problems, all the backtesting is going to be done through the framework `backtrader`. This is a famous framework with **multiple features** that help to get the most information about the execution of the strategy on a dataset. It allows to work with generic *.csv* files, specifying the formatting ([here](https://www.backtrader.com/docu/datafeed/) more info).<br/>
*Backtrader* allows also to **optimize the parameters of the strategy**; this should be a powerful tool that would allow us to **save a lot of time**. Of course the optimization must be done in the training set. 

### Strategies
Here there is a list of all the strategies to implement:
- EMA crossover (optimizing parameters);
- MACD stratgy;
- EMA crossover w/ stop-loss and take-profit;
- EMA crossover w/ low timestamp and daily parameter optimization; (**Hot topic**)
- Bollinger Bands strategy;
- Stochastic Oscillator strategy;
- RSI strategy;
- Combinations of multiple strategies; (**Hot topic**)

### TODO
[x] Implement the EMA Crossover strategy (class `GoldenCross`);
[x] Implement the EMA Crossover with *take-profit* and *stop-loss* (class `TrailCross`);
[] Fix bugs in class `TrailCross`;

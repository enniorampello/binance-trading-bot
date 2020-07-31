from trade import Trade, Type

class Strategy:

    def __init__(self):
        self.backtester = None
        self.len = 0
    def next(self):
        pass
    def stop(self):
        pass

    def buy(self, amount, tradeid=0):
        idx = self.len
        if amount <= self.backtester.current_capital:
            quantity = amount / self.backtester.data_window.iloc[idx].Close
            self.backtester.current_capital -= amount
        elif self.backtester.current_capital > 0:
            quantity = self.backtester.current_capital / self.backtester.data_window.iloc[idx].Close
            self.backtester.current_capital = 0
        else:
            print('Error: couldn\'t execute BUY order')
            return
        
        trade = Trade(
                tradeid=tradeid,
                trade_number=self.backtester.num_trades,
                direction=Type.LONG, 
                entry_price=self.backtester.data_window.iloc[idx].Close, 
                quantity=quantity, 
                date=self.backtester.current_date
                )
        self.backtester.open_trades.insert(0,trade)
        self.backtester.current_coins += quantity
        self.backtester.num_trades += 1

    def sell(self, amount, tradeid=0):
        idx = self.len
        quantity = amount / self.backtester.data_window.iloc[idx].Close
        if quantity <= self.backtester.current_coins:
            self.backtester.current_coins -= quantity
        elif self.backtester.current_coins > 0:
            quantity = self.backtester.current_coins
            self.backtester.current_coins = 0
        else:
            print('Error: couldn\'t execute SELL order.')
            return

        trade = Trade(
                tradeid=tradeid,
                trade_number=self.backtester.num_trades,
                direction=Type.SHORT, 
                entry_price=self.backtester.data_window.iloc[idx].Close, 
                quantity=quantity, 
                date=self.backtester.current_date
                )
        self.backtester.open_trades.insert(0,trade)
        self.backtester.current_capital += (quantity * self.backtester.data_window.iloc[idx].Close)
        self.backtester.num_trades += 1

    def close(self, tradeid):
        idx = self.len
        for t in self.backtester.open_trades:
            if t.id == tradeid:
                t.close(
                    exit_price=self.backtester.data_window.iloc[idx].Close, 
                    date=self.backtester.current_date
                    )
                self.backtester.trades.append([t.open_date, t.id, t.trade_number, t.type, t.quantity, t.entry_price, t.exit_price, t.close_date, t.pnl])
                self.backtester.open_trades.remove(t)
                return

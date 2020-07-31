from trade import Trade, Type

class Strategy:

    def __init__(self):
        self.backtester = None
        self.len = 0
        self.close = None
    def next(self):
        pass
    def stop(self):
        pass

    def buy(self, amount, tradeid=0):
        last = self.len
        if amount <= self.backtester.current_capital:
            quantity = amount / self.close.iloc[last]
            self.backtester.current_capital -= amount
        elif self.backtester.current_capital > 0:
            quantity = self.backtester.current_capital / self.close.iloc[last]
            self.backtester.current_capital = 0
        else:
            print('Error: couldn\'t execute BUY order')
            return
        
        trade = Trade(
                tradeid=tradeid,
                trade_number=self.backtester.num_trades,
                direction=Type.LONG, 
                entry_price=self.close.iloc[last], 
                quantity=quantity, 
                date=self.backtester.current_date
                )
        self.backtester.open_trades.insert(0,trade)
        self.backtester.current_coins += quantity
        self.backtester.num_trades += 1

    def sell(self, amount, tradeid=0):
        last = self.len
        quantity = amount / self.close.iloc[last]
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
                entry_price=self.close.iloc[last],
                quantity=quantity, 
                date=self.backtester.current_date
                )
        self.backtester.open_trades.insert(0,trade)
        self.backtester.current_capital += (quantity * self.close.iloc[last])
        self.backtester.num_trades += 1

    def close(self, tradeid):
        last = self.len
        for t in self.backtester.open_trades:
            if t.id == tradeid:
                t.close(
                    exit_price=self.close.iloc[last], 
                    date=self.backtester.current_date
                    )
                self.backtester.trades.append([t.open_date, t.id, t.trade_number, t.type, t.quantity, t.entry_price, t.exit_price, t.close_date, t.pnl])
                self.backtester.open_trades.remove(t)
                return

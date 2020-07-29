from trade import Trade, Type

class Strategy:

    def __init__(self):
        self.backtester = None
    def next(self):
        pass
    def stop(self):
        pass

    def buy(self, quantity, tradeid=0):
        self.backtester.trades.append(
            Trade(
                tradeid=tradeid,
                direction=Type.LONG, 
                entry_price=self.backtester.data_window.iloc[0].Close, 
                quantity=quantity, 
                date=self.backtester.current_date
                ))

    def sell(self, quantity, tradeid=0):
        if quantity > self.backtester.current_coins & self.backtester.current_coins > 0:
                self.backtester.trades.append(
                    Trade(
                        tradeid=tradeid,
                        direction=Type.SHORT, 
                        entry_price=self.backtester.data_window.iloc[0].Close, 
                        quantity=quantity, 
                        date=self.backtester.current_date
                        ))
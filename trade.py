
class Type:
    LONG = 0
    SHORT = 1

class Trade:
    
    def __init__(self, tradeid, trade_number, direction, entry_price, quantity, date):
        self.id = tradeid
        self.trade_number = trade_number
        self.type = direction
        self.entry_price = entry_price
        self.exit_price = None
        self.quantity = quantity
        self.open_date = date
        self.close_date = None
        self.pnl = 0
        self.closed = False
    
    def close(self, exit_price, date):
        self.exit_price = exit_price
        self.close_date = date
        self.pnl = self.quantity * (self.exit_price - self.entry_price)
        if self.type == Type.SHORT:
            self.pnl = -self.pnl
        self.closed = True


# Simple Stock Market Application - Loose Interface Design

# Requirements:
# - Should be able to buy a stock at price 5
# - Should be able to sell a stock at price 10
# - See history of the stock price
# - See total balance and money earned (5)
# - See a list of owned stocks (one owned of EN, TO owned of 2)


class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.portfolio = {}
        self.transaction_history = []

    def view_portfolio(self):
        print(f"Portfolio for {self.name}:")
        for symbol, qty in self.portfolio.items():
            print(f"  {symbol}: {qty} shares")


class StockSystem:
    def __init__(self):
        self.prices = {"EN": 5, "TO": 10, "AB": 7}
        self.price_history = {
            "EN": [3, 4, 5],
            "TO": [8, 9, 10],
            "AB": [5, 6, 7],
        }

    def buy_stock(self, user, symbol, amount):
        price = self.prices.get(symbol, 0)
        total_cost = price * amount
        if user.balance >= total_cost:
            user.balance -= total_cost
            user.portfolio[symbol] = user.portfolio.get(symbol, 0) + amount
            user.transaction_history.append(f"Bought {amount} of {symbol} at {price}")
            print(f"Bought {amount} shares of {symbol} for {total_cost}")
        else:
            print("Insufficient balance.")

    def sell_stock(self, user, symbol, amount):
        owned = user.portfolio.get(symbol, 0)
        if owned >= amount:
            price = self.prices.get(symbol, 0)
            total_earned = price * amount
            user.balance += total_earned
            user.portfolio[symbol] = owned - amount
            user.transaction_history.append(f"Sold {amount} of {symbol} at {price}")
            print(f"Sold {amount} shares of {symbol} for {total_earned}")
        else:
            print("Not enough shares to sell.")

    def show_price_history(self, symbol):
        history = self.price_history.get(symbol, [])
        print(f"Price history for {symbol}: {history}")

    def show_balance(self, user):
        print(f"Balance for {user.name}: {user.balance}")

    def show_owned_stocks(self, user):
        print(f"Owned stocks for {user.name}:")
        for symbol, qty in user.portfolio.items():
            print(f"  {symbol}: {qty} shares")

    def update_prices(self, symbols, increments):
        for symbol, inc in zip(symbols, increments):
            price = self.prices[symbol]
            self.price_history[symbol].append(price + inc)
            self.prices[symbol] = price + inc

    def print_net_changes(self, labels, balance_after_buy, balance_after_sell, initial_balance):
        for i, label in enumerate(labels):
            print(f"Net change from {label}: {balance_after_sell[i] - balance_after_buy[i]}")
        print(f"Total net change this session: {balance_after_sell[-1] - initial_balance}")


def simulate_trading_session(user, stock_system):
    symbols = ["EN", "TO", "AB"]
    net_labels = ["EN trades", "TO trade", "AB trades"]

    stock_system.update_prices(symbols, [1, 2, 1])
    user.balance += 50
    initial_balance = user.balance

    balance_after_buy = []
    for symbol, amount in zip(symbols, [1, 2, 1]):
        stock_system.buy_stock(user, symbol, amount)
        balance_after_buy.append(user.balance)

    owned = [user.portfolio.get(s, 0) for s in symbols]
    balance_after_sell = []
    for symbol, amount in zip(symbols, [owned[0], owned[1] - 1, owned[2]]):
        stock_system.sell_stock(user, symbol, amount)
        balance_after_sell.append(user.balance)

    stock_system.print_net_changes(net_labels, balance_after_buy, balance_after_sell, initial_balance)
    for symbol in symbols:
        stock_system.show_price_history(symbol)
    stock_system.show_balance(user)
    stock_system.show_owned_stocks(user)
    user.view_portfolio()
    print(f"Remaining TO shares: {user.portfolio.get('TO', 0)}")
    print(f"Final balance: {user.balance}")


if __name__ == "__main__":
    user = User("Alice", 100)
    system = StockSystem()

    system.buy_stock(user, "EN", 1)
    system.buy_stock(user, "TO", 2)
    system.sell_stock(user, "EN", 1)
    system.show_price_history("EN")
    system.show_price_history("TO")
    system.show_balance(user)
    system.show_owned_stocks(user)
    user.view_portfolio()

    simulate_trading_session(user, system)

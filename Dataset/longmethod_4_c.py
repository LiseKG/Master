
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


def simulate_trading_session(user, stock_system):
    symbol_0 = "EN"
    symbol_1 = "TO"
    symbol_2 = "AB"
    price_0 = stock_system.prices[symbol_0]
    price_1 = stock_system.prices[symbol_1]
    price_2 = stock_system.prices[symbol_2]
    stock_system.price_history[symbol_0].append(price_0 + 1)
    stock_system.prices[symbol_0] = price_0 + 1
    stock_system.price_history[symbol_1].append(price_1 + 2)
    stock_system.prices[symbol_1] = price_1 + 2
    stock_system.price_history[symbol_2].append(price_2 + 1)
    stock_system.prices[symbol_2] = price_2 + 1
    user.balance += 50
    initial_balance = user.balance
    stock_system.buy_stock(user, symbol_0, 1)
    balance_after_buy_0 = user.balance
    stock_system.buy_stock(user, symbol_1, 2)
    balance_after_buy_1 = user.balance
    stock_system.buy_stock(user, symbol_2, 1)
    balance_after_buy_2 = user.balance
    owned_en = user.portfolio.get(symbol_0, 0)
    owned_to = user.portfolio.get(symbol_1, 0)
    owned_ab = user.portfolio.get(symbol_2, 0)
    stock_system.sell_stock(user, symbol_0, owned_en)
    balance_after_sell_0 = user.balance
    stock_system.sell_stock(user, symbol_1, owned_to - 1)
    balance_after_sell_1 = user.balance
    stock_system.sell_stock(user, symbol_2, owned_ab)
    balance_after_sell_2 = user.balance
    net_change_0 = balance_after_sell_0 - balance_after_buy_0
    net_change_1 = balance_after_sell_1 - balance_after_buy_1
    net_change_2 = balance_after_sell_2 - balance_after_buy_2
    total_net = balance_after_sell_2 - initial_balance
    print(f"Net change from EN trades: {net_change_0}")
    print(f"Net change from TO trade: {net_change_1}")
    print(f"Net change from AB trades: {net_change_2}")
    print(f"Total net change this session: {total_net}")
    stock_system.show_price_history(symbol_0)
    stock_system.show_price_history(symbol_1)
    stock_system.show_price_history(symbol_2)
    stock_system.show_balance(user)
    stock_system.show_owned_stocks(user)
    user.view_portfolio()
    remaining_to = user.portfolio.get(symbol_1, 0)
    print(f"Remaining TO shares: {remaining_to}")
    final_balance = user.balance
    print(f"Final balance: {final_balance}")


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

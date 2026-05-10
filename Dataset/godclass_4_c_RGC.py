
# Simple Stock Market Application - Loose Interface Design

# Requirements:
# - Should be able to buy a stock at price 5
# - Should be able to sell a stock at price 10
# - See history of the stock price
# - See total balance and money earned (5)
# - See a list of owned stocks (one owned of EN, TO owned of 2)


class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price
        self.price_history = [price]


class Transaction:
    def __init__(self, transaction_type, symbol, amount, price):
        self.transaction_type = transaction_type
        self.symbol = symbol
        self.amount = amount
        self.price = price


class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.portfolio = {}
        self.transactions = []

    def view_portfolio(self):
        print(f"Portfolio for {self.name}:")
        for symbol, amount in self.portfolio.items():
            print(f"  {symbol}: {amount} shares")


class MarketRegistry:
    def __init__(self):
        self.stocks = {}
        self.market_open = True

    def add_stock(self, symbol, price):
        stock = Stock(symbol, price)
        self.stocks[symbol] = stock
        print(f"Stock '{symbol}' added at price {price}.")

    def update_stock_price(self, symbol, new_price):
        stock = self.get_stock(symbol)
        if stock is not None:
            stock.price = new_price
            stock.price_history.append(new_price)
            print(f"Stock '{symbol}' updated to price {new_price}.")

    def get_stock(self, symbol):
        if symbol in self.stocks:
            return self.stocks[symbol]
        print(f"Stock '{symbol}' not found.")
        return None

    def get_stock_price(self, symbol):
        stock = self.get_stock(symbol)
        if stock is not None:
            return stock.price
        return 0

    def open_market(self):
        self.market_open = True
        print("Market has been opened.")

    def close_market(self):
        self.market_open = False
        print("Market has been closed.")

    def check_market_open(self):
        if self.market_open:
            print("Market is open.")
        else:
            print("Market is closed.")
        return self.market_open

    def show_all_stocks(self):
        print("All available stocks:")
        for symbol, stock in self.stocks.items():
            print(f"  {symbol}: current price {stock.price}")

    def show_price_history(self, symbol):
        stock = self.get_stock(symbol)
        if stock is not None:
            print(f"Price history for {symbol}: {stock.price_history}")


class TradeExecutor:
    def __init__(self, market):
        self.market = market

    def validate_buy(self, user, symbol, amount):
        stock = self.market.get_stock(symbol)
        if stock is None:
            return False
        total_cost = stock.price * amount
        if user.balance < total_cost:
            print(f"Insufficient balance. Need {total_cost}, have {user.balance}.")
            return False
        return True

    def validate_sell(self, user, symbol, amount):
        owned = user.portfolio.get(symbol, 0)
        if owned < amount:
            print(f"Not enough shares of '{symbol}'. Owned: {owned}, requested: {amount}.")
            return False
        return True

    def record_transaction(self, user, transaction_type, symbol, amount, price):
        transaction = Transaction(transaction_type, symbol, amount, price)
        user.transactions.append(transaction)
        print(f"Transaction recorded: {transaction_type} {amount} of {symbol} at {price}.")

    def buy_stock(self, user, symbol, amount):
        if not self.market.check_market_open():
            return
        if not self.validate_buy(user, symbol, amount):
            return
        price = self.market.get_stock_price(symbol)
        total_cost = price * amount
        user.balance -= total_cost
        user.portfolio[symbol] = user.portfolio.get(symbol, 0) + amount
        self.record_transaction(user, "BUY", symbol, amount, price)
        print(f"{user.name} bought {amount} share(s) of {symbol} at {price} each. Total cost: {total_cost}.")

    def sell_stock(self, user, symbol, amount):
        if not self.market.check_market_open():
            return
        if not self.validate_sell(user, symbol, amount):
            return
        price = self.market.get_stock_price(symbol)
        total_revenue = price * amount
        user.balance += total_revenue
        user.portfolio[symbol] -= amount
        if user.portfolio[symbol] == 0:
            del user.portfolio[symbol]
        self.record_transaction(user, "SELL", symbol, amount, price)
        print(f"{user.name} sold {amount} share(s) of {symbol} at {price} each. Total revenue: {total_revenue}.")


class PortfolioReporter:
    def __init__(self, market):
        self.market = market

    def show_balance(self, user):
        print(f"{user.name}'s balance: {user.balance}")

    def show_owned_stocks(self, user):
        if not user.portfolio:
            print(f"{user.name} owns no stocks.")
        else:
            print(f"{user.name}'s owned stocks:")
            for symbol, amount in user.portfolio.items():
                print(f"  {symbol}: {amount} share(s)")

    def calculate_portfolio_value(self, user):
        total = 0
        for symbol, amount in user.portfolio.items():
            price = self.market.get_stock_price(symbol)
            total += price * amount
        print(f"{user.name}'s portfolio market value: {total}")
        return total

    def calculate_earnings(self, user, initial_balance):
        earnings = user.balance - initial_balance + self.calculate_portfolio_value(user)
        print(f"{user.name}'s total earnings compared to initial balance {initial_balance}: {earnings}")
        return earnings

    def show_transaction_history(self, user):
        print(f"Transaction history for {user.name}:")
        if not user.transactions:
            print("  No transactions yet.")
        for t in user.transactions:
            print(f"  {t.transaction_type} {t.amount} of {t.symbol} at {t.price}")


class StockSystem:
    def __init__(self):
        self.users = []
        self.market = MarketRegistry()
        self.trader = TradeExecutor(self.market)
        self.reporter = PortfolioReporter(self.market)

    def register_user(self, user):
        self.users.append(user)
        print(f"User '{user.name}' registered with balance {user.balance}.")

    def list_users(self):
        print("Registered users:")
        for user in self.users:
            print(f"  {user.name} (balance: {user.balance})")

    def reset_user_portfolio(self, user):
        user.portfolio = {}
        user.transactions = []
        print(f"{user.name}'s portfolio and transaction history have been reset.")



if __name__ == "__main__":
    system = StockSystem()

    alice = User("Alice", 1000)
    bob = User("Bob", 500)

    system.register_user(alice)
    system.register_user(bob)

    system.market.add_stock("EN", 5)
    system.market.add_stock("TO", 10)

    system.list_users()
    system.market.show_all_stocks()

    system.market.open_market()
    system.market.check_market_open()

    system.trader.buy_stock(alice, "EN", 1)
    system.trader.buy_stock(alice, "TO", 2)
    system.trader.buy_stock(bob, "EN", 3)

    alice.view_portfolio()
    bob.view_portfolio()

    system.reporter.show_owned_stocks(alice)
    system.reporter.show_owned_stocks(bob)

    system.reporter.show_balance(alice)
    system.reporter.show_balance(bob)

    system.market.update_stock_price("EN", 8)
    system.market.update_stock_price("TO", 15)

    system.market.show_price_history("EN")
    system.market.show_price_history("TO")

    system.trader.sell_stock(alice, "EN", 1)
    system.trader.sell_stock(alice, "TO", 1)

    system.reporter.show_balance(alice)
    system.reporter.show_owned_stocks(alice)

    initial_alice = 1000
    system.reporter.calculate_portfolio_value(alice)
    system.reporter.calculate_earnings(alice, initial_alice)

    system.reporter.show_transaction_history(alice)
    system.reporter.show_transaction_history(bob)

    system.market.close_market()
    system.market.check_market_open()

    system.trader.buy_stock(bob, "TO", 1)

    system.reset_user_portfolio(bob)
    system.reporter.show_owned_stocks(bob)
    system.reporter.show_transaction_history(bob)



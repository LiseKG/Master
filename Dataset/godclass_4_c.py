
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


class StockSystem:
    def __init__(self):
        self.stocks = {}
        self.users = []
        self.market_open = True

    # Method 1
    def register_user(self, user):
        self.users.append(user)
        print(f"User '{user.name}' registered with balance {user.balance}.")

    # Method 2
    def add_stock(self, symbol, price):
        stock = Stock(symbol, price)
        self.stocks[symbol] = stock
        print(f"Stock '{symbol}' added at price {price}.")

    # Method 3
    def update_stock_price(self, symbol, new_price):
        stock = self.get_stock(symbol)
        if stock is not None:
            stock.price = new_price
            stock.price_history.append(new_price)
            print(f"Stock '{symbol}' updated to price {new_price}.")

    # Method 4
    def get_stock(self, symbol):
        if symbol in self.stocks:
            return self.stocks[symbol]
        print(f"Stock '{symbol}' not found.")
        return None

    # Method 5
    def get_stock_price(self, symbol):
        stock = self.get_stock(symbol)
        if stock is not None:
            return stock.price
        return 0

    # Method 6
    def check_market_open(self):
        if self.market_open:
            print("Market is open.")
        else:
            print("Market is closed.")
        return self.market_open

    # Method 7
    def open_market(self):
        self.market_open = True
        print("Market has been opened.")

    # Method 8
    def close_market(self):
        self.market_open = False
        print("Market has been closed.")

    # Method 9
    def validate_buy(self, user, symbol, amount):
        stock = self.get_stock(symbol)
        if stock is None:
            return False
        total_cost = stock.price * amount
        if user.balance < total_cost:
            print(f"Insufficient balance. Need {total_cost}, have {user.balance}.")
            return False
        return True

    # Method 10
    def validate_sell(self, user, symbol, amount):
        owned = user.portfolio.get(symbol, 0)
        if owned < amount:
            print(f"Not enough shares of '{symbol}'. Owned: {owned}, requested: {amount}.")
            return False
        return True

    # Method 11
    def record_transaction(self, user, transaction_type, symbol, amount, price):
        transaction = Transaction(transaction_type, symbol, amount, price)
        user.transactions.append(transaction)
        print(f"Transaction recorded: {transaction_type} {amount} of {symbol} at {price}.")

    # Method 12
    def buy_stock(self, user, symbol, amount):
        if not self.check_market_open():
            return
        if not self.validate_buy(user, symbol, amount):
            return
        price = self.get_stock_price(symbol)
        total_cost = price * amount
        user.balance -= total_cost
        user.portfolio[symbol] = user.portfolio.get(symbol, 0) + amount
        self.record_transaction(user, "BUY", symbol, amount, price)
        print(f"{user.name} bought {amount} share(s) of {symbol} at {price} each. Total cost: {total_cost}.")

    # Method 13
    def sell_stock(self, user, symbol, amount):
        if not self.check_market_open():
            return
        if not self.validate_sell(user, symbol, amount):
            return
        price = self.get_stock_price(symbol)
        total_revenue = price * amount
        user.balance += total_revenue
        user.portfolio[symbol] -= amount
        if user.portfolio[symbol] == 0:
            del user.portfolio[symbol]
        self.record_transaction(user, "SELL", symbol, amount, price)
        print(f"{user.name} sold {amount} share(s) of {symbol} at {price} each. Total revenue: {total_revenue}.")

    # Method 14
    def show_price_history(self, symbol):
        stock = self.get_stock(symbol)
        if stock is not None:
            print(f"Price history for {symbol}: {stock.price_history}")

    # Method 15
    def show_balance(self, user):
        print(f"{user.name}'s balance: {user.balance}")

    # Method 16
    def show_owned_stocks(self, user):
        if not user.portfolio:
            print(f"{user.name} owns no stocks.")
        else:
            print(f"{user.name}'s owned stocks:")
            for symbol, amount in user.portfolio.items():
                print(f"  {symbol}: {amount} share(s)")

    # Method 17
    def calculate_portfolio_value(self, user):
        total = 0
        for symbol, amount in user.portfolio.items():
            price = self.get_stock_price(symbol)
            total += price * amount
        print(f"{user.name}'s portfolio market value: {total}")
        return total

    # Method 18
    def calculate_earnings(self, user, initial_balance):
        earnings = user.balance - initial_balance + self.calculate_portfolio_value(user)
        print(f"{user.name}'s total earnings compared to initial balance {initial_balance}: {earnings}")
        return earnings

    # Method 19
    def show_transaction_history(self, user):
        print(f"Transaction history for {user.name}:")
        if not user.transactions:
            print("  No transactions yet.")
        for t in user.transactions:
            print(f"  {t.transaction_type} {t.amount} of {t.symbol} at {t.price}")

    # Method 20
    def show_all_stocks(self):
        print("All available stocks:")
        for symbol, stock in self.stocks.items():
            print(f"  {symbol}: current price {stock.price}")

    # Method 21
    def list_users(self):
        print("Registered users:")
        for user in self.users:
            print(f"  {user.name} (balance: {user.balance})")

    # Method 22
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

    system.add_stock("EN", 5)
    system.add_stock("TO", 10)

    system.list_users()
    system.show_all_stocks()

    system.open_market()
    system.check_market_open()

    system.buy_stock(alice, "EN", 1)
    system.buy_stock(alice, "TO", 2)
    system.buy_stock(bob, "EN", 3)

    alice.view_portfolio()
    bob.view_portfolio()

    system.show_owned_stocks(alice)
    system.show_owned_stocks(bob)

    system.show_balance(alice)
    system.show_balance(bob)

    system.update_stock_price("EN", 8)
    system.update_stock_price("TO", 15)

    system.show_price_history("EN")
    system.show_price_history("TO")

    system.sell_stock(alice, "EN", 1)
    system.sell_stock(alice, "TO", 1)

    system.show_balance(alice)
    system.show_owned_stocks(alice)

    initial_alice = 1000
    system.calculate_portfolio_value(alice)
    system.calculate_earnings(alice, initial_alice)

    system.show_transaction_history(alice)
    system.show_transaction_history(bob)

    system.close_market()
    system.check_market_open()

    system.buy_stock(bob, "TO", 1)

    system.reset_user_portfolio(bob)
    system.show_owned_stocks(bob)
    system.show_transaction_history(bob)



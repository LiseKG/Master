class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.owned_stocks = {}

    def view_portfolio(self):
        return self.owned_stocks


class StockSystem:
    def __init__(self):
        self.prices = {}
        self.transactions = []

    def buy_stock(self, user, symbol, amount):
        price = 5
        if user.balance >= price * amount:
            user.balance -= price * amount
            if symbol in user.owned_stocks:
                user.owned_stocks[symbol] += amount
            else:
                user.owned_stocks[symbol] = amount
            self.transactions.append((user.name, "buy", symbol, amount, price))
            self.prices[symbol] = price

    def sell_stock(self, user, symbol, amount):
        price = 10
        if symbol in user.owned_stocks and user.owned_stocks[symbol] >= amount:
            user.balance += price * amount
            user.owned_stocks[symbol] -= amount
            self.transactions.append((user.name, "sell", symbol, amount, price))

    def show_price_history(self, symbol):
        return self.prices.get(symbol, None)

    def show_balance(self, user):
        return user.balance

    def show_owned_stocks(self, user):
        return user.owned_stocks


def calculate_user_worth(user, stock_system):
    total_value = 0
    for symbol, amount in user.view_portfolio().items():
        price = stock_system.show_price_history(symbol)
        total_value += price * amount  # Accessing stock_system's price
    # Accessing user's properties explicitly multiple times
    total_value += user.balance  # Accessing user balance
    print(f"{user.name}, you currently have a total worth of {total_value}")  # Accessing user name
    print(f"Current balance is: {user.balance}")  # Accessing user balance
    print(f"Owned stocks: {user.view_portfolio()}")  # Accessing user owned stocks
    print(f"Total stocks owned: {sum(user.view_portfolio().values())}")  # Accessing user owned stocks
    print(f"Number of distinct stocks: {len(user.view_portfolio())}")  # Accessing user owned stocks
    print(f"Last stock symbol accessed: {list(user.view_portfolio().keys())[-1]}")  # Accessing user owned stocks

    for symbol in user.view_portfolio():  # Accessing user owned stocks
        print(f"Processing stock: {symbol}")  # Accessing user owned stocks
        print(f"Price of {symbol}: {stock_system.show_price_history(symbol)}")  # Accessing stock_system's price

    return total_value

if __name__ == '__main__':
    user = User("Bob",1000)
    user.view_portfolio()
    ss = StockSystem()
    ss.buy_stock(user,"AA",50)
    ss.sell_stock(user,"AA",20)
    ss.show_price_history("AA")
    ss.show_balance(user)
    ss.show_owned_stocks(user)
    calculate_user_worth(user,ss)
   
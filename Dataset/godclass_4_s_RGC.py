class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.owned_stocks = {}

    def view_portfolio(self):
        return self.owned_stocks

    def update_balance(self, amount):
        self.balance += amount


class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.current_price = price
        self.price_history = [price]

    def update_price(self, price):
        self.current_price = price
        self.price_history.append(price)

    def show_price_history(self):
        print(self.price_history)
        return self.price_history

    def get_highest_price(self):
        return max(self.price_history)

    def get_lowest_price(self):
        return min(self.price_history)


class StockSystem:
    def __init__(self):
        self.users = []
        self.stocks = {}  # symbol -> Stock

    def add_user(self, name, balance):
        user = User(name, balance)
        self.users.append(user)

    def add_stock(self, symbol, price):
        self.stocks[symbol] = Stock(symbol, price)

    def buy_stock(self, user, symbol, amount):
        stock = self.stocks.get(symbol)
        if stock is None:
            self.add_stock(symbol,5)
            stock =  self.stocks.get(symbol)
        if amount * stock.current_price <= user.balance:
            user.update_balance(-amount * stock.current_price)
            self.update_owned_stocks(user, symbol, amount)
            stock.show_price_history().append(stock.current_price)
            print(f"{amount} of {symbol} bought for {user.name}.")
        else:
            print("Insufficient balance or stock does not exist.")

    def sell_stock(self, user, symbol, amount):
        stock = self.stocks.get(symbol)
        if stock is None:
            self.add_stock(symbol,5)
            stock = self.stocks.get(symbol)
        if user.owned_stocks.get(symbol, 0) >= amount:
            user.update_balance(amount * 10)  # Selling price
            user.owned_stocks[symbol] -= amount
            stock.show_price_history().append(10)
            print(f"{amount} of {symbol} sold for {user.name}.")
        else:
            print("Insufficient stocks or stock does not exist.")

    def update_owned_stocks(self, user, symbol, amount):
        if symbol in user.owned_stocks:
            user.owned_stocks[symbol] += amount
        else:
            user.owned_stocks[symbol] = amount

    def show_balance(self, user):
        return user.balance

    def show_owned_stocks(self, user):
        return user.view_portfolio()

    def list_all_users(self):
        return self.users

    def total_users(self):
        return len(self.users)

    def print_summary(self):
        for user in self.users:
            print(f"User: {user.name}, Balance: {user.balance}, Owned Stocks: {user.view_portfolio()}")

    def simulate_market_fluctuation(self):
        for stock in self.stocks.values():
            new_price = stock.current_price + (1 if stock.current_price < 10 else -1)
            stock.update_price(new_price)
    
    def show_price_history(self,stock):
        if stock in self.stocks:
            return self.stocks[stock].show_price_history()

def main():
    stock_system = StockSystem()

    # Add users and stocks
    stock_system.add_user("Alice", 50)
    stock_system.add_user("Bob", 30)

    # Simulate buying stocks
    user1 = stock_system.users[0]
    user2 = stock_system.users[1]

    stock_system.add_stock("EN", 5)
    stock_system.add_stock("TO", 5)

    
    stock_system.buy_stock(user1, "EN", 1)
    stock_system.buy_stock(user1, "TO", 2)
    stock_system.buy_stock(user2, "EN", 2)

    # Simulate selling stock
    stock_system.sell_stock(user1, "EN", 1)

    # Show balances and owned stocks
    print(stock_system.show_balance(user1))
    print(stock_system.show_owned_stocks(user1))
    for stock in stock_system.stocks:
        stock_system.stocks[stock].show_price_history()
    

    # Print user summary
    stock_system.print_summary()
    chosenStock = "EN"
    print(stock_system.stocks[chosenStock].current_price)
    stock_system.stocks[chosenStock].current_price += 3
    stock_system.stocks[chosenStock].current_price -= 2
    
    stock_system.stocks[chosenStock].get_highest_price()
    stock_system.stocks[chosenStock].get_lowest_price()
    # Simulate market changes
    stock_system.simulate_market_fluctuation()
    stock_system.print_summary()
    

if __name__ == "__main__":
    main()

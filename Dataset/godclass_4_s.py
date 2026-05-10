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
        self.owned_stocks = {}
        self.price_history = {}

    def view_portfolio(self):
        return self.owned_stocks


class StockSystem:
    def __init__(self):
        self.current_price = 5
        self.users = []
        self.price_history = {}
        
    def buy_stock(self, user, symbol, amount):
        if amount * self.current_price <= user.balance:
            user.balance -= amount * self.current_price
            self.update_owned_stocks(user, symbol, amount)
            self.record_price_history(symbol, self.current_price)
            print(f"{amount} of {symbol} bought for {user.name}.")
        else:
            print("Insufficient balance.")

    def sell_stock(self, user, symbol, amount):
        if symbol in user.owned_stocks and user.owned_stocks[symbol] >= amount:
            user.balance += amount * 10  # Selling price
            user.owned_stocks[symbol] -= amount
            self.record_price_history(symbol, 10)
            print(f"{amount} of {symbol} sold for {user.name}.")
        else:
            print("Insufficient stocks.")

    def show_price_history(self, symbol):
        return self.price_history.get(symbol, [])

    def show_balance(self, user):
        return user.balance

    def show_owned_stocks(self, user):
        return user.view_portfolio()

    def update_owned_stocks(self, user, symbol, amount):
        if symbol in user.owned_stocks:
            user.owned_stocks[symbol] += amount
        else:
            user.owned_stocks[symbol] = amount

    def record_price_history(self, symbol, price):
        if symbol not in self.price_history:
            self.price_history[symbol] = []
        self.price_history[symbol].append(price)

    def list_all_users(self):
        return self.users

    def add_user(self, name, balance):
        user = User(name, balance)
        self.users.append(user)

    def total_users(self):
        return len(self.users)

    def user_details(self, user):
        return {'name': user.name, 'balance': user.balance, 'owned_stocks': user.view_portfolio()}

    def get_user_portfolio(self, user):
        return user.view_portfolio()

    def get_current_stock_price(self):
        return self.current_price

    def increase_stock_price(self, increment):
        self.current_price += increment

    def decrease_stock_price(self, decrement):
        self.current_price -= decrement


    def get_highest_price(self, symbol):
        if symbol in self.price_history:
            return max(self.price_history[symbol])
        return None

    def get_lowest_price(self, symbol):
        if symbol in self.price_history:
            return min(self.price_history[symbol])
        return None

    def print_summary(self):
        print(f"Current price: {self.current_price}")
        for user in self.users:
            print(self.user_details(user))

    def simulate_market_fluctuation(self):
        import random
        self.increase_stock_price(random.randint(1, 5))
        self.decrease_stock_price(random.randint(1, 5))

def main():
    stock_system = StockSystem()

    # Add users
    stock_system.add_user("Alice", 50)
    stock_system.add_user("Bob", 30)

    # Access users once
    user1 = stock_system.users[0]
    user2 = stock_system.users[1]

    # Buy stocks (tests buy_stock, update_owned_stocks, record_price_history)
    stock_system.buy_stock(user1, "EN", 1)
    stock_system.buy_stock(user1, "TO", 2)
    stock_system.buy_stock(user2, "EN", 2)

    # Sell stock (tests sell_stock)
    stock_system.sell_stock(user1, "EN", 1)

    # Basic info methods
    stock_system.show_balance(user1)
    stock_system.show_owned_stocks(user1)
    stock_system.show_price_history("EN")

    # User and system info
    stock_system.list_all_users()
    stock_system.total_users()
    stock_system.user_details(user1)
    stock_system.get_user_portfolio(user1)

    # Price controls
    stock_system.get_current_stock_price()
    stock_system.increase_stock_price(3)
    stock_system.decrease_stock_price(2)

    # Price statistics
    stock_system.get_highest_price("EN")
    stock_system.get_lowest_price("EN")

    # Market simulation (tests internal price changes)
    stock_system.simulate_market_fluctuation()

    # Print summary (tests print_summary)
    stock_system.print_summary()

    

if __name__ == "__main__":
    main()

class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.portfolio = {}

    def view_portfolio(self):
        return self.portfolio


class StockSystem:
    def __init__(self):
        self.stock_prices = {'EN': 5, 'TO': 10}
        self.price_history = {'EN': [], 'TO': []}
    
    def buy_stock(self, user, symbol, amount):
        if symbol in self.stock_prices and user.balance >= self.stock_prices[symbol] * amount:
            total_cost = self.stock_prices[symbol] * amount
            user.balance -= total_cost
            user.portfolio[symbol] = user.portfolio.get(symbol, 0) + amount
            self.price_history[symbol].append(self.stock_prices[symbol])
            self.execute_long_method(user)
        else:
            print(f"Transaction failed for {user.name}")

    def sell_stock(self, user, symbol, amount):
        if symbol in user.portfolio and user.portfolio[symbol] >= amount:
            user.balance += self.stock_prices[symbol] * amount
            user.portfolio[symbol] -= amount
            self.price_history[symbol].append(self.stock_prices[symbol])
        else:
            print(f"Transaction failed for {user.name}")

    def show_price_history(self, symbol):
        return self.price_history.get(symbol, [])

    def show_balance(self, user):
        return user.balance

    def show_owned_stocks(self, user):
        return user.portfolio
    
    def execute_long_method(self, user):
        totals = sum(user.portfolio.values())
        print(f"Total stocks owned by {user.name}: {totals}")
        print("User has stocks." if totals > 0 else "User has no stocks.")
        
        for stock, amount in user.portfolio.items():
            print(f"Owned: {amount} of {stock}")
        
        earnings = sum(user.portfolio[stock] * 5 for stock in user.portfolio)  # Assume purchase price of 5
        print(f"Earnings potential: {earnings}")
        print("User is in debt!" if user.balance < 0 else "User is financially stable.")
        print("User has substantial earnings." if earnings > 100 else "User's earnings are below expectations.")
        
        for stock in user.portfolio:
            print(f"Checking stock {stock}")
            if stock == "EN":
                print("This is En stock.")
        
        print("Verifying stock ownership..." * 3)
        print("Completed verification.")
        
        price_recorded = [user.portfolio[stock] * 5 for stock in user.portfolio]
        average_price = sum(price_recorded) / len(price_recorded) if price_recorded else 0
        print(f"Average stock price for owned stocks: {average_price}")
        print("User's stocks are above average price." if average_price > 7 else "User's stocks are below average price.")
        
        print("Calculating long-term projections...")
        for i in range(1, 6):
            print(f"Projection year {i}...")
        print("Projections completed.")
        
        for stock in user.portfolio:
            print(f"Final check on {stock}.")
        
        print("All checks complete.")
        print(f"User {user.name}'s review finished.")
        print("Final balance check." if totals > 0 else "No stocks to check.")
        print("Summary of stocks completed.")
        print("Final earnings projection passed.")
        print("Business analysis for stocks concluded.")
        print("All system checks completed.")
        print("End of method execution.")

if __name__ == '__main__':
    user = User("Bob",1000)
    user.view_portfolio()
    ss = StockSystem()
    ss.buy_stock(user,"AA",50)
    ss.sell_stock(user,"AA",20)
    ss.show_price_history("AA")
    ss.show_balance(user)
    ss.show_owned_stocks(user)
    ss.execute_long_method(user)

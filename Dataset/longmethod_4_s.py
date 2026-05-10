class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.portfolio = {}
        self.price_history = {}

    def view_portfolio(self):
        return self.portfolio


class StockSystem:
    def __init__(self):
        self.stock_prices = {'EN': 5, 'TO': 10}
        self.price_history = {'EN': [], 'TO': []}
    
    def buy_stock(self, user, symbol, amount):
        if symbol in self.stock_prices and user.balance >= self.stock_prices[symbol] * amount:
            user.balance -= self.stock_prices[symbol] * amount
            if symbol in user.portfolio:
                user.portfolio[symbol] += amount
            else:
                user.portfolio[symbol] = amount
            self.price_history[symbol].append(self.stock_prices[symbol])
            
            execute_long_method(user)
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


def execute_long_method(user):
    #1
    totals = sum(user.portfolio.values())  
    #2
    print(f"Total stocks owned by {user.name}: {totals}")
    #3
    if totals > 0:
        print("User has stocks.")
    #4
    else:
        print("User has no stocks.")
    #5
    for stock, amount in user.portfolio.items():
        print(f"Owned: {amount} of {stock}")
    #6
    earnings = 0
    #7
    for stock in user.portfolio:
        earnings += user.portfolio[stock] * 5  # Assume constant purchase price
    #8
    print(f"Earnings potential: {earnings}")
    #9
    if user.balance < 0:
        print("User is in debt!")
    #10
    else:
        print("User is financially stable.")
    #11
    if earnings > 100:
        print("User has substantial earnings.")
    #12
    else:
        print("User's earnings are below expectations.")
    #13
    for stock in user.portfolio:
        print(f"Checking stock {stock}")
    #14
    stock = "EN"
    if stock == "EN":
        print("This is En stock.")
    #15
    for _ in range(3):
        print("Verifying stock ownership...")
    #16
    print("Completed verification.")
    #17
    price_recorded = []
    #18
    for stock in user.portfolio:
        price_recorded.append(user.portfolio[stock] * 5)
    #19
    average_price = sum(price_recorded) / len(price_recorded) if price_recorded else 0
    #20
    print(f"Average stock price for owned stocks: {average_price}")
    #21
    if average_price > 7:
        print("User's stocks are above average price.")
    #22
    else:
        print("User's stocks are below average price.")
    #23
    print("Calculating long-term projections...")
    #24
    for i in range(5):
        print(f"Projection year {i + 1}...")
    #25
    print("Projections completed.")
    #26
    for stock in user.portfolio:
        print(f"Final check on {stock}.")
    #27
    print("All checks complete.")
    #28
    print(f"User {user.name}'s review finished.")
    #29
    if totals > 0:
        print("Final balance check.")
    #30
    else:
        print("No stocks to check.")
    #31
    print("Summary of stocks completed.")
    #32
    print("Final earnings projection passed.")
    #33
    print("Business analysis for stocks concluded.")
    #34
    print("All system checks completed.")
    #35
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
    execute_long_method(user)

   
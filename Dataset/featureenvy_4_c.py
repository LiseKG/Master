
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
        self.total_earned = 0

    def view_portfolio(self):
        print(f"{self.name}'s portfolio: {self.portfolio}")


class StockSystem:
    def __init__(self):
        self.prices = {"EN": 5, "TO": 5}
        self.price_history = {"EN": [5], "TO": [5]}

    def buy_stock(self, user, symbol, amount):
        cost = self.prices[symbol] * amount
        if user.balance >= cost:
            user.balance -= cost
            user.portfolio[symbol] = user.portfolio.get(symbol, 0) + amount
            print(f"{user.name} bought {amount} of {symbol}")
        else:
            print("Insufficient balance")

    def sell_stock(self, user, symbol, amount):
        if user.portfolio.get(symbol, 0) >= amount:
            revenue = self.prices[symbol] * amount
            user.balance += revenue
            user.total_earned += revenue
            user.portfolio[symbol] -= amount
            print(f"{user.name} sold {amount} of {symbol}")
        else:
            print("Not enough stocks to sell")

    def show_price_history(self, symbol):
        print(f"Price history for {symbol}: {self.price_history[symbol]}")

    def show_balance(self, user):
        print(f"{user.name}'s balance: {user.balance}, total earned: {user.total_earned}")

    def show_owned_stocks(self, user):
        print(f"{user.name} owns: {user.portfolio}")


def generate_user_report(user):
    report = ""
    report += "Name: " + user.name + "\n"
    report += "Balance: " + str(user.balance) + "\n"
    report += "Total Earned: " + str(user.total_earned) + "\n"
    report += "Portfolio: " + str(user.portfolio) + "\n"

    if user.balance > 50:
        report += user.name + " has a healthy balance.\n"
    else:
        report += user.name + " has a low balance.\n"

    if user.total_earned > 0:
        report += user.name + " has earned money.\n"
    else:
        report += user.name + " has not earned anything yet.\n"

    stock_count = sum(user.portfolio.values()) if user.portfolio else 0
    report += user.name + " owns " + str(stock_count) + " stocks in total.\n"

    if user.portfolio:
        report += user.name + "'s holdings: " + str(user.portfolio) + "\n"

    report += "Final balance for " + user.name + ": " + str(user.balance) + "\n"

    return report


if __name__ == "__main__":
    user = User("Alice", 100)
    system = StockSystem()

    system.buy_stock(user, "EN", 1)
    system.buy_stock(user, "TO", 2)
    system.sell_stock(user, "EN", 1)
    system.show_price_history("EN")
    system.show_balance(user)
    system.show_owned_stocks(user)
    user.view_portfolio()

    report = generate_user_report(user)
    print(report)



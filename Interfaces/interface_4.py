
# Simple Stock Market Application - Loose Interface Design

# Requirements:
# - Should be able to buy a stock at price 5
# - Should be able to sell a stock at price 10
# - See history of the stock price
# - See total balance and money earned (5)
# - See a list of owned stocks (one owned of EN, TO owned of 2)


class User:
    def __init__(self, name, balance):
        pass

    def view_portfolio(self):
        pass


class StockSystem:
    def __init__(self):
        pass

    def buy_stock(self, user, symbol, amount):
        pass

    def sell_stock(self, user, symbol, amount):
        pass

    def show_price_history(self, symbol):
        pass

    def show_balance(self, user):
        pass

    def show_owned_stocks(self, user):
        pass



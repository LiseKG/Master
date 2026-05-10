import godclass_4_c as Reviewer1
import godclass_4_c_RGC as Reviewer2
#import godclass_4_c_RGC_E as Reviewer3
import longmethod_4_c as Reviewer4
import longmethod_4_c_RLM as Reviewer5
#import longmethod_4_c_RLM_E as Reviewer6
import featureenvy_4_c as Reviewer7
import featureenvy_4_c_RFE as Reviewer8
#import featureenvy_4_c_RFE_E as Reviewer9


# Define test cases
test_cases = [
    # {
    #     "class": Reviewer1.StockSystem,
    #     "user": Reviewer1.User("Alice", 100),
    #     "stock": "EN",
    #     "amount": 1
    # },
    #  {
    #      "class": Reviewer2.StockSystem,
    #      "user": Reviewer2.User("Bob", 100),
    #       "stock": "EN",
    #      "amount": 1
    #  },
  
    # {
    #     "class": Reviewer4.StockSystem,
    #     "user": Reviewer4.User("David", 100),
    #      "stock": "EN",
    #     "amount": 1
    # },
    # {
    #     "class": Reviewer5.StockSystem,
    #     "user": Reviewer5.User("Eva", 100),
    #     "stock": "EN",
    #     "amount": 1
    # },
  
    # {
    #     "class": Reviewer7.StockSystem,
    #     "user": Reviewer7.User("Grace", 100),
    #     "stock": "EN",
    #     "amount": 1
    # },
    # {
    #     "class": Reviewer8.StockSystem,
    #     "user": Reviewer8.User("Hannah", 100),
    #      "stock": "EN",
    #     "amount": 1
    # },
 
]

# Running the tests
for test_case in test_cases:
    print(test_case)
    stock_system = test_case["class"]()
    user = test_case["user"]
    stock = test_case["stock"]
    amount = test_case["amount"]
    
    print(f"Testing {test_case['class'].__name__} with user {user.name}")

    # Buy stock
    stock_system.buy_stock(user, stock, amount)
    # Assert to check if the owned stocks are updated
    owned_stocks = stock_system.show_owned_stocks(user)
    # if isinstance(owned_stocks, dict):
    #     assert stock in owned_stocks.keys(), f"Failed to find {stock} in owned stocks."
    # else:
    #     assert stock in owned_stocks, f"Failed to find {stock} in owned stocks."

    # Sell stock
    stock_system.sell_stock(user, stock, amount)
    # Assert to check if the owned stocks are updated
    owned_stocks = stock_system.show_owned_stocks(user)
   
    if(len(owned_stocks) == 0):
        pass
    else:
        assert 0 == owned_stocks[stock], f"Failed to find {stock} in owned stocks after selling."

    # Show price history
    price_history = stock_system.show_price_history(stock)
    print(price_history,"priceh")
    if isinstance(price_history,int):
        assert price_history > 0, "Price history should not be empty."
    else:
        assert len(price_history) > 0, "Price history should not be empty."

    # Show balance
    balance = stock_system.show_balance(user)
    assert balance >= 0, "Balance should be non-negative."

    print("Success!\n")

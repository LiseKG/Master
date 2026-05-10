
# Simple Shopping System
"""
Rules for application:
Be able to have a list of products
Be able to add a banana to a shopping cart
Create an User
Able to buy a chosen banana and receieve a receipt
"""
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        return "Product: " + str(self.name) + ", Price: " + str(self.price)
    #returns product info


class User:
    def __init__(self, username, income):
        self.username = username
        self.income = income

    def buy(self, product):
        self.income = self.income - product.price
        return "You bought " + str(product.name) + " for " + str(product.price)
    #return a string saying you bought and price. Should subtract price from income


class Cart:
    def __init__(self):
        self.items = []

    def add(self, product):
        self.items.append(product)
        return "Added " + str(product.name) + " to cart"
    #add a new product, return confirmation string


class Shop:
    def __init__(self):
        self.products = []

    def process(self, user, product):
        confirmation = user.buy(product)
        return confirmation
    #buy product, return confirmation


class Receipt:
    def __init__(self, user, product):
        self.user = user
        self.product = product

    def show(self):
        return "Receipt - User: " + str(self.user.username) + ", Item: " + str(self.product.name) + ", Price: " + str(self.product.price) + ", Remaining balance: " + str(self.user.income)
    #shows reciept information


def create_banana():
    banana_name = "Banana"
    print("purchase_banana: banana name set to: " + banana_name)
    banana_price = 1
    print("purchase_banana: banana price set to: " + str(banana_price))
    banana = Product(banana_name, banana_price)
    print("purchase_banana: created Product instance for banana")
    banana_info = banana.get_info()
    print("purchase_banana: banana info: " + banana_info)
    return banana


def inspect_user(user: User, banana_price: int):
    user_name = user.username
    print("purchase_banana: extracted username: " + str(user_name))
    user_income = user.income
    print("purchase_banana: extracted user income: " + str(user_income))
    can_afford = user_income >= banana_price
    print("purchase_banana: user can afford banana: " + str(can_afford))
    income_after = user_income - banana_price
    print("purchase_banana: projected income after purchase: " + str(income_after))
    return user_name, user_income


def add_to_cart_and_shop(cart: Cart, shop: Shop, banana: Product):
    cart_confirmation = cart.add(banana)
    print("purchase_banana: cart.add() returned: " + str(cart_confirmation))
    cart_size = len(cart.items)
    print("purchase_banana: cart now contains items: " + str(cart_size))
    shop.products.append(banana)
    print("purchase_banana: banana added to shop product list")
    shop_stock = len(shop.products)
    print("purchase_banana: shop product count: " + str(shop_stock))


def process_and_receipt(shop: Shop, user: User, banana: Product, user_income: int):
    process_confirmation = shop.process(user, banana)
    print("purchase_banana: shop.process() returned: " + str(process_confirmation))
    updated_income = user.income
    print("purchase_banana: user income after purchase: " + str(updated_income))
    receipt = Receipt(user, banana)
    print("purchase_banana: created Receipt instance")
    receipt_output = receipt.show()
    print("purchase_banana: receipt.show() returned: " + str(receipt_output))
    purchase_logged = True
    print("purchase_banana: purchase_logged flag set: " + str(purchase_logged))
    result = process_confirmation
    print("purchase_banana: result assigned: " + str(result))
    income_diff = user_income - updated_income
    print("purchase_banana: income deducted: " + str(income_diff))
    balance_positive = updated_income > 0
    print("purchase_banana: user balance still positive: " + str(balance_positive))
    return result


def purchase_banana(user: User, shop: Shop, cart: Cart) -> str:
    print("purchase_banana: starting execution")
    print("purchase_banana: received user parameter")
    print("purchase_banana: received shop parameter")
    print("purchase_banana: received cart parameter")
    banana = create_banana()
    user_name, user_income = inspect_user(user, banana.price)
    add_to_cart_and_shop(cart, shop, banana)
    result = process_and_receipt(shop, user, banana, user_income)
    print("purchase_banana: final result for " + str(user_name) + ": " + str(result))
    print("purchase_banana: execution complete, returning result")
    return result


if __name__ == "__main__":
    user = User("Bob", 50)
    shop = Shop()
    cart = Cart()
    product = Product("Banana", 1)
    product.get_info()
    cart.add(product)
    shop.process(user, product)
    receipt = Receipt(user, product)
    receipt.show()
    user.buy(product)
    result = purchase_banana(user, shop, cart)
    print("main: result = " + result)




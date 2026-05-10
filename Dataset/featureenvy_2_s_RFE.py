"""
Rules for application:
Be able to have a list of products
Be able to add a banana to a shopping cart
Create an User
Able to buy a chosen banana and receipt a recite.
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_info(self):
        return f"{self.name}: ${self.price}"


class User:
    def __init__(self, username):
        self.username = username
        self.cart = Cart()
    
    def buy(self, product):
        receipt = Receipt(self, product)
        return receipt


class Cart:
    def __init__(self):
        self.products = []
    
    def add(self, product):
        self.products.append(product)
    
    def total_price(self):
        return sum(product.price for product in self.products)


class Shop:
    def __init__(self):
        self.products = []

    def process(self, user, product):
        user.cart.add(product)
        return user.buy(product)


class Receipt:
    def __init__(self, user, product):
        self.user = user
        self.product = product
    
    def show(self):
        return f"Receipt: {self.user.username} bought {self.product.get_info()}"


def show_cart_summary(user):
    print(f"Cart summary for {user.username}:")
    cart_total = user.cart.total_price()
    print(f"Total items in cart: {len(user.cart.products)}")
    for product in user.cart.products:
        print(product.get_info())
    print(f"Total price: ${cart_total}")
    print(f"User: {user.username}")
    print_cart_contents(user.cart)
    print_banana_status(user.cart)
    print_first_product_info(user.cart)
    print_user_cart_reference(user.cart)
    print_bought_product_info(user.cart)


def print_cart_contents(cart):
    print(f"Cart contents: {', '.join(product.get_info() for product in cart.products)}")


def print_banana_status(cart):
    has_banana = 'banana' in [product.name for product in cart.products]
    print(f"Has bananas: {has_banana}")


def print_first_product_info(cart):
    if cart.products:
        print(f"First product name: {cart.products[0].name}")
        print(f"First product price: {cart.products[0].price}")
    else:
        print("First product name: No products")
        print("First product price: No products")


def print_user_cart_reference(cart):
    print(f"User cart reference: {cart}")


def print_bought_product_info(cart):
    if cart.products:
        print(f"User bought product: {cart.products[0].get_info()}")
    else:
        print("User bought product: No products")



if __name__ == '__main__':
    product = Product("Apple",0.3)
    product.get_info()
    user = User("Bob")
    user.buy(product)
    cart = Cart()
    cart.add(product)
    show_cart_summary(user)
    shop = Shop()
    shop.process(user,product)
    receipt = Receipt(user,product)
    print(receipt.show())

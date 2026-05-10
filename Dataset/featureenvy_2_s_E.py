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
        return f"{self.name}: ${self.price:.2f}"

    
class User:
    def __init__(self, username):
        self.username = username
        self.cart = Cart()
    
    def buy(self, product):
        return Receipt(self, product)


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
    cart = user.cart
    products = cart.products
    total_items = len(products)
    total_price = cart.total_price()

    print(f"Cart summary for {user.username}:")
    print(f"Total items in cart: {total_items}")

    for product in products:
        print(product.get_info())

    print(f"Total price: ${total_price:.2f}")
    print(f"User: {user.username}")
    print(f"Cart contents: {', '.join(product.get_info() for product in products)}")
    has_banana = any(product.name.lower() == 'banana' for product in products
                     )
    print(f"Has bananas: {has_banana}")

    if products:
        first_product = products[0]
        print(f"First product name: {first_product.name}")
        print(f"First product price: ${first_product.price:.2f}")
        print(f"User cart reference: {cart}")
        print(f"User bought product: {first_product.get_info()}")
    else:
        print("First product name: No products")
        print("First product price: No products")




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

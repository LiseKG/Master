"""
Rules for application:
Be able to have a list of products
Be able to add a banana to a shopping cart
Create a User
Able to buy a chosen banana and receive a receipt.
"""


class Shop:
    def __init__(self):
        self.products = []
        self.cart = Cart()

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        return [product.get_info() for product in self.products]

    def process(self, user, product):
        self.add_product(product)
        self.cart.add(product)
        receipt = self.create_receipt(user, product)
        return receipt

    def create_receipt(self, user, product):
        return Receipt(user, product)

    def checkout(self, user):
        total = self.calculate_total()
        user_feedback = user.buy(self.cart.items[0]) if self.cart.items else 'Cart is empty.'
        return user_feedback, f'Total: {total}'

    def calculate_total(self):
        total = sum(product.price for product in self.cart.items)
        return total

    def empty_cart(self):
        self.cart.items = []

    def has_product(self, product_name):
        return any(product.name == product_name for product in self.products)

    def get_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product
        return None

    def clear_cart(self):
        self.empty_cart()

    def display_receipt(self, receipt):
        return receipt.show()

    def finalize_purchase(self, user):
        feedback, total = self.checkout(user)
        self.clear_cart()
        return feedback, total

    def buy_product(self, user, product_name):
        if self.has_product(product_name):
            product = self.get_product(product_name)
            self.process(user, product)
            return self.finalize_purchase(user)
        return 'Product not found.'

    def add_banana(self):
        banana = Product('Banana', 0.99)
        self.add_product(banana)

    def add_apple(self):
        apple = Product('Apple', 0.99)
        self.add_product(apple)

    def show_cart(self):
        return self.cart.list_items()

    def simulate_user_purchase(self, username, product_name):
        user = User(username)
        return self.buy_product(user, product_name)

    def list_all_products(self):
        return self.list_products()

    def check_cart_items(self):
        return self.show_cart()

    def view_total(self):
        return self.calculate_total()


class Receipt:
    def __init__(self, user, product):
        self.user = user
        self.product = product

    def show(self):
        return f'Receipt: {self.user.username} bought {self.product.get_info()}'

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        return f'Product: {self.name}, Price: {self.price}'


class User:
    def __init__(self, username):
        self.username = username

    def buy(self, product):
        return f'{self.username} bought {product.get_info()}'


class Cart:
    def __init__(self):
        self.items = []

    def add(self, product):
        self.items.append(product)

    def list_items(self):
        return [item.get_info() for item in self.items]


if __name__ == '__main__':
    print("---- SHOP INITIALIZATION ----")
    shop = Shop()

    print("\n---- ADDING PRODUCTS ----")
    shop.add_banana()
    shop.add_apple()

    print("\n---- LISTING PRODUCTS ----")
    print(shop.list_all_products())

    print("\n---- CHECK PRODUCT EXISTS ----")
    print("Has Banana?", shop.has_product("Banana"))
    print("Has Orange?", shop.has_product("Orange"))

    print("\n---- GET PRODUCT ----")
    banana = shop.get_product("Banana")
    print(banana.get_info() if banana else "Not Found")

    print("\n---- MANUAL CART TEST ----")
    shop.cart.add(banana)
    print("Cart Items:", shop.show_cart())
    print("Total:", shop.view_total())

    print("\n---- CHECKOUT TEST ----")
    user = User("Bob")
    feedback, total = shop.checkout(user)
    print(feedback)
    print(total)

    print("\n---- EMPTY CART TEST ----")
    shop.empty_cart()
    print("Cart after empty:", shop.check_cart_items())

    print("\n---- RECEIPT TEST ----")
    shop.cart.add(banana)
    receipt = shop.create_receipt(user, banana)
    print(shop.display_receipt(receipt))

    print("\n---- FINALIZE PURCHASE TEST ----")
    feedback, total = shop.finalize_purchase(user)
    print(feedback)
    print(total)

    print("\n---- BUY PRODUCT METHOD TEST ----")
    result = shop.buy_product(User("Alice"), "Banana")
    print(result)

    print("\n---- SIMULATED PURCHASE TEST ----")
    print(shop.simulate_user_purchase("Charlie", "Apple"))

    print("\n---- CLEAR CART TEST ----")
    shop.cart.add(banana)
    shop.clear_cart()
    print("Cart after clear:", shop.check_cart_items())

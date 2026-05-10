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

    def clear(self):
        self.items.clear()


class Shop:
    def __init__(self):
        self.products = []
        self.cart = Cart()

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        return [product.get_info() for product in self.products]

    def process(self, user, product):
        self.cart.add(product)
        return Receipt(user, product)

    def checkout(self, user):
        if not self.cart.items:
            return 'Cart is empty.',
        
        user_feedback = user.buy(self.cart.items[0])
        total = self.calculate_total()
        self.clear_cart()
        return user_feedback, f'Total: {total}'

    def calculate_total(self):
        return sum(product.price for product in self.cart.items)

    def clear_cart(self):
        self.cart.clear()

    def has_product(self, product_name):
        return any(product.name == product_name for product in self.products)

    def get_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product
        return None

    def buy_product(self, user, product_name):
        if self.has_product(product_name):
            product = self.get_product(product_name)
            receipt = self.process(user, product)
            return self.checkout(user), receipt
        return 'Product not found.', None

    def add_item(self, name, price):
        self.add_product(Product(name, price))

    def show_cart(self):
        return self.cart.list_items()

    def simulate_user_purchase(self, username, product_name):
        user = User(username)
        return self.buy_product(user, product_name)

    def list_all_products(self):
        return self.list_products()

    def view_total(self):
        return self.calculate_total()


class Receipt:
    def __init__(self, user, product):
        self.user = user
        self.product = product

    def show(self):
        return f'Receipt: {self.user.username} bought {self.product.get_info()}'


if __name__ == '__main__':
    print("---- SHOP INITIALIZATION ----")
    shop = Shop()

    print("\n---- ADDING PRODUCTS ----")
    shop.add_item("Banana", 0.99)
    shop.add_item("Apple", 0.99)

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
    shop.clear_cart()
    print("Cart after empty:", shop.show_cart())

    print("\n---- RECEIPT TEST ----")
    receipt = Receipt(user, banana)
    print(receipt.show())

    print("\n---- FINALIZE PURCHASE TEST ----")
    (feedback, total), receipt = shop.buy_product(user, "Banana")
    print(feedback)
    print(total)
    print(receipt.show())

    print("\n---- BUY PRODUCT METHOD TEST ----")
    result, receipt = shop.buy_product(User("Alice"), "Banana")
    print(result)

    print("\n---- SIMULATED PURCHASE TEST ----")
    text, receipt = shop.simulate_user_purchase("Charlie", "Apple")
    print(text)

    print("\n---- CLEAR CART TEST ----")
    shop.cart.add(banana)
    shop.cart.clear()
    print("Cart after clear:", shop.show_cart())

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
    print(f"Cart summary for {user.username}:")
    print(f"Total items in cart: {len(cart.products)}")
    print_cart_contents(cart)
    cart_total = cart.total_price()
    print(f"Total price: ${cart_total}")
    print(f"User: {user.username}")
    print_banana_status(cart)
    print_first_product_info(cart)
    print_user_cart_reference(cart)
    print_bought_product_info(cart)


def print_cart_contents(cart):
    if cart.products:
        print(f"Cart contents: {', '.join(product.get_info() for product in cart.products)}")
    else:
        print("Cart contents: No products")


def print_banana_status(cart):
    has_banana = any(product.name == 'banana' for product in cart.products)
    print(f"Has bananas: {has_banana}")


def print_first_product_info(cart):
    if cart.products:
        first_product = cart.products[0]
        print(f"First product name: {first_product.name}")
        print(f"First product price: {first_product.price}")
    else:
        print("First product name: No products")
        print("First product price: No products")


def print_user_cart_reference(cart):
    print(f"User cart reference: {id(cart)}")


def print_bought_product_info(cart):
    if cart.products:
        print(f"User bought product: {cart.products[-1].get_info()}")
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

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        return f"{self.name}: ${self.price:.1f}"


class User:
    def __init__(self, username):
        self.username = username

    def buy(self, product):
        return Receipt(self, product)


class Cart:
    def __init__(self):
        self.items = []

    def add(self, product):
        self.items.append(product)


class Shop:
    def __init__(self):
        self.products = []
        self.cart = Cart()

    def add_product(self, product):
        self.products.append(product)

    def process(self, user, product):
        self.cart.add(product)
        long_method(user, product)


class Receipt:
    def __init__(self, user, product):
        self.user = user
        self.product = product

    def show(self):
        return f"Receipt for {self.user.username}: {self.product.get_info()}"


def long_method(user, product):
    print(f"{user.username} is trying to buy {product.name}")

    total_cost = max(product.price - (5 if product.price > 50 else 0), 0)
    print(f"Total cost after discount: {total_cost}")

    if total_cost < 0:
        print("Cost cannot be negative")
        return

    print("Processing payment...")

    # Assuming payment is processed immediately for this example
    transaction_id = 1234
    print(f"Payment successful. Transaction ID: {transaction_id}")

    print(f"Thank you for your purchase, {user.username}!")
    print(f"Item 1: {product.get_info()}")
    
    print("Generating receipt...")
    receipt = Receipt(user, product)
    print(receipt.show())
    
    print("Thank you for shopping with us!")
    print("We hope to see you again soon!")
    
    if product.price > 50:
        print(f"Discount applied: $5")
        
    print("End of transaction.")

if __name__ == '__main__':
    product = Product("Apple",0.3)
    product.get_info()
    user = User("Bob")
    user.buy(product)
    cart = Cart()
    cart.add(product)
    shop = Shop()
    shop.process(user,product)
    receipt = Receipt(user,product)
    print(receipt.show())
    long_method(user,product)
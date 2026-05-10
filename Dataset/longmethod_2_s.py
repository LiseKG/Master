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
    # 1
    total_cost = product.price
    # 2
    payment_received = False
    # 3
    transaction_id = None
    # 4
    print(f"{user.username} is trying to buy {product.name}")
    # 5
    confirmation_number = 1234
    # 6
    item_count = 1
    # 7
    discount = 0
    # 8
    if total_cost > 50:
        # 9
        discount = 5
        # 10
    total_cost -= discount
    # 11
    print(f"Total cost after discount: {total_cost}")
    # 12
    if total_cost < 0:
        # 13
        print("Cost cannot be negative")
        # 14
        return
    # 15
    print("Processing payment...")
    # 16
    if payment_received:
        # 17
        print("Payment already received.")
        # 18
    else:
        # 19
        print("Payment being processed...")
        # 20
        payment_received = True
        # 21
        transaction_id = confirmation_number
        # 22
        print(f"Payment successful. Transaction ID: {transaction_id}")
    # 23
    print(f"Thank you for your purchase, {user.username}!")
    # 24
    for i in range(item_count):
        # 25
        print(f"Item {i + 1}: {product.get_info()}")
    # 26
    print("Generating receipt...")
    # 27
    receipt = Receipt(user, product)
    # 28
    print(receipt.show())
    # 29
    print("Thank you for shopping with us!")
    # 30
    print("We hope to see you again soon!")
    # 31
    if discount > 0:
        # 32
        print(f"Discount applied: ${discount}")
    # 33
    print("End of transaction.")
    # 34
    return
    # 35

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
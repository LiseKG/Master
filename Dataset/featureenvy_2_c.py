
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
        return f"{self.name}: ${self.price}"
        #returns product info


class User:
    def __init__(self, username, income):
        self.username = username
        self.income = income

    def buy(self, product):
        self.income -= product.price
        return f"You bought {product.name} for ${product.price}"
        #return a string saying you bought and price. Should subtract price from income


class Cart:
    def __init__(self):
        self.items = []

    def add(self, product):
        self.items.append(product)
        return f"Added {product.name} to cart"
        #add a new product, return confirmation string


class Shop:
    def __init__(self):
        self.products = []

    def process(self, user, product):
        return user.buy(product)
        #buy product, return confirmation


class Receipt:
    def __init__(self, user, product):
        self.user = user
        self.product = product

    def show(self):
        return f"Receipt - User: {self.user.username}, Item: {self.product.name}, Price: ${self.product.price}"
        #shows reciept information


def generate_product_report(product):
    report = ""
    report += "Product Report\n"
    report += "Name: " + product.name + "\n"
    report += "Price: $" + str(product.price) + "\n"
    report += "Info: " + product.get_info() + "\n"
    if product.price > 100:
        report += product.name + " is expensive\n"
    else:
        report += product.name + " is affordable\n"
    discounted = product.price * 0.9
    report += "Discounted price for " + product.name + ": $" + str(discounted) + "\n"
    tax = product.price * 0.2
    report += "Tax for " + product.name + ": $" + str(tax) + "\n"
    total = product.price + tax
    report += "Total with tax: $" + str(total) + "\n"
    report += "Summary: " + product.get_info() + " (tax included: $" + str(total) + ")\n"
    return report


if __name__ == '__main__':
    product = Product("Apple", 0.3)
    product.get_info()
    user = User("Bob", 100)
    user.buy(product)
    cart = Cart()
    cart.add(product)
    generate_product_report(product)
    shop = Shop()
    shop.process(user, product)
    receipt = Receipt(user, product)
    print(receipt.show())
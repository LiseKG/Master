
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
        return f"Product: {self.name}, Price: {self.price}"


class User:
    def __init__(self, username, income=100):
        self.username = username
        self.income = income

    def buy(self, product):
        self.income -= product.price
        return f"You bought {product.name} for {product.price}. Remaining income: {self.income}"


class Cart:
    def __init__(self):
        self.items = []

    def add(self, product):
        self.items.append(product)
        return f"Added {product.name} to cart."


class Receipt:
    def __init__(self, user, product):
        self.user = user
        self.product = product

    def show(self):
        return (f"--- Receipt ---\n"
                f"Customer: {self.user.username}\n"
                f"Item: {self.product.name}\n"
                f"Price: {self.product.price}\n"
                f"Remaining balance: {self.user.income}\n"
                f"---------------")


class Shop:
    def __init__(self):
        self.inventory = []
        self.carts = {}
        self.receipts = []
        self.discount_rate = 0.0
        self.sales_log = []
        self.registered_users = []
        self.setup_inventory()

    # 1
    def setup_inventory(self):
        banana = Product("Banana", 1.5)
        apple = Product("Apple", 2.0)
        mango = Product("Mango", 3.5)
        self.inventory.append(banana)
        self.inventory.append(apple)
        self.inventory.append(mango)

    # 2
    def process(self, user, product):
        if not self.check_stock(product):
            return f"{product.name} is out of stock."
        if not self.check_funds(user, product):
            return f"{user.username} has insufficient funds."
        discounted = self.apply_discount(product)
        confirmation = user.buy(discounted)
        self.generate_receipt(user, discounted)
        self.log_sale(user, discounted)
        self.remove_from_inventory(discounted)
        return confirmation

    # 3
    def check_stock(self, product):
        for item in self.inventory:
            if item.name == product.name:
                return True
        return False

    # 4
    def check_funds(self, user, product):
        return user.income >= product.price

    # 5
    def apply_discount(self, product):
        discounted_price = round(product.price * (1 - self.discount_rate), 2)
        return Product(product.name, discounted_price)

    # 6
    def generate_receipt(self, user, product):
        receipt = Receipt(user, product)
        self.receipts.append(receipt)
        return receipt

    # 7
    def log_sale(self, user, product):
        entry = f"{user.username} purchased {product.name} for {product.price}"
        self.sales_log.append(entry)

    # 8
    def remove_from_inventory(self, product):
        for i, item in enumerate(self.inventory):
            if item.name == product.name:
                self.inventory.pop(i)
                return f"{product.name} removed from inventory."
        return f"{product.name} not found in inventory."

    # 9
    def register_user(self, user):
        self.registered_users.append(user)
        return f"User {user.username} registered."

    # 10
    def create_cart(self, user):
        cart = Cart()
        self.carts[user.username] = cart
        return cart

    # 11
    def add_to_cart(self, user, product):
        if user.username not in self.carts:
            self.create_cart(user)
        if not self.check_stock(product):
            return f"{product.name} is not available."
        self.carts[user.username].add(product)
        return f"{product.name} added to {user.username}'s cart."

    # 12
    def checkout_cart(self, user):
        if user.username not in self.carts:
            return "No cart found for user."
        cart = self.carts[user.username]
        results = []
        for product in list(cart.items):
            result = self.process(user, product)
            results.append(result)
        del self.carts[user.username]
        return results

    # 13
    def set_discount(self, rate):
        self.discount_rate = rate
        return f"Discount set to {rate * 100}%."

    # 14
    def get_inventory_list(self):
        if not self.inventory:
            return "Inventory is empty."
        return [item.get_info() for item in self.inventory]

    # 15
    def restock(self, product):
        self.inventory.append(product)
        return f"{product.name} restocked at {product.price}."

    # 16
    def get_sales_report(self):
        if not self.sales_log:
            return "No sales recorded."
        report = "--- Sales Report ---\n"
        for entry in self.sales_log:
            report += entry + "\n"
        report += "--------------------"
        return report

    # 17
    def get_total_revenue(self):
        total = 0.0
        for entry in self.sales_log:
            parts = entry.split(" for ")
            if len(parts) == 2:
                total += float(parts[1])
        return round(total, 2)

    # 18
    def find_product(self, name):
        for item in self.inventory:
            if item.name == name:
                return item
        return None

    # 19
    def show_receipt(self, index):
        if index < 0 or index >= len(self.receipts):
            return "Receipt not found."
        return self.receipts[index].show()

    # 20
    def show_all_receipts(self):
        if not self.receipts:
            return "No receipts available."
        all_receipts = ""
        for receipt in self.receipts:
            all_receipts += receipt.show() + "\n"
        return all_receipts

    # 21
    def get_user_balance(self, user):
        return f"{user.username}'s balance: {user.income}"

    # 22
    def summarize_cart(self, user):
        if user.username not in self.carts:
            return f"No cart for {user.username}."
        cart = self.carts[user.username]
        if not cart.items:
            return f"{user.username}'s cart is empty."
        total = sum(item.price for item in cart.items)
        items = [item.name for item in cart.items]
        return f"{user.username}'s cart: {items}, Total: {total}"


# --- Run the application ---
if __name__ == "__main__":
    shop = Shop()
    user1 = User("Alice", 20.0)
    shop.register_user(user1)

    print("Inventory:")
    for info in shop.get_inventory_list():
        print(" ", info)

    banana = shop.find_product("Banana")
    shop.add_to_cart(user1, banana)
    print(shop.summarize_cart(user1))

    shop.set_discount(0.1)
    results = shop.checkout_cart(user1)
    for r in results:
        print(r)

    print(shop.get_sales_report())
    print(f"Total revenue: {shop.get_total_revenue()}")
    print(shop.show_receipt(0))
    print(shop.show_all_receipts())
    print(shop.get_user_balance(user1))

    apple = shop.find_product("Apple")
    shop.restock(Product("Banana", 1.5))
    print("\nInventory after restock:")
    for info in shop.get_inventory_list():
        print(" ", info)

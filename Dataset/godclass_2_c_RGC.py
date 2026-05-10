
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
    def __init__(self, username, income):
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


class Inventory:
    def __init__(self):
        self.stock = []
        self.setup()

    def setup(self):
        self.stock.append(Product("Banana", 1.5))
        self.stock.append(Product("Apple", 2.0))
        self.stock.append(Product("Mango", 3.5))

    def check_stock(self, product):
        for item in self.stock:
            if item.name == product.name:
                return True
        return False

    def remove(self, product):
        for i, item in enumerate(self.stock):
            if item.name == product.name:
                self.stock.pop(i)
                return f"{product.name} removed from inventory."
        return f"{product.name} not found in inventory."

    def restock(self, product):
        self.stock.append(product)
        return f"{product.name} restocked at {product.price}."

    def find_product(self, name):
        for item in self.stock:
            if item.name == name:
                return item
        return None

    def get_list(self):
        if not self.stock:
            return "Inventory is empty."
        return [item.get_info() for item in self.stock]


class DiscountService:
    def __init__(self):
        self.discount_rate = 0.0

    def set_discount(self, rate):
        self.discount_rate = rate
        return f"Discount set to {rate * 100}%."

    def apply_discount(self, product):
        discounted_price = round(product.price * (1 - self.discount_rate), 2)
        return Product(product.name, discounted_price)


class SalesLedger:
    def __init__(self):
        self.sales_log = []

    def log_sale(self, user, product):
        entry = f"{user.username} purchased {product.name} for {product.price}"
        self.sales_log.append(entry)

    def get_sales_report(self):
        if not self.sales_log:
            return "No sales recorded."
        report = "--- Sales Report ---\n"
        for entry in self.sales_log:
            report += entry + "\n"
        report += "--------------------"
        return report

    def get_total_revenue(self):
        total = 0.0
        for entry in self.sales_log:
            parts = entry.split(" for ")
            if len(parts) == 2:
                total += float(parts[1])
        return round(total, 2)


class ReceiptStore:
    def __init__(self):
        self.receipts = []

    def generate_receipt(self, user, product):
        receipt = Receipt(user, product)
        self.receipts.append(receipt)
        return receipt

    def show_receipt(self, index):
        if index < 0 or index >= len(self.receipts):
            return "Receipt not found."
        return self.receipts[index].show()

    def show_all_receipts(self):
        if not self.receipts:
            return "No receipts available."
        all_receipts = ""
        for receipt in self.receipts:
            all_receipts += receipt.show() + "\n"
        return all_receipts


class CartManager:
    def __init__(self, inventory):
        self.carts = {}
        self.inventory = inventory

    def create_cart(self, user):
        cart = Cart()
        self.carts[user.username] = cart
        return cart

    def add_to_cart(self, user, product):
        if user.username not in self.carts:
            self.create_cart(user)
        if not self.inventory.check_stock(product):
            return f"{product.name} is not available."
        self.carts[user.username].add(product)
        return f"{product.name} added to {user.username}'s cart."

    def checkout_cart(self, user, process_fn):
        if user.username not in self.carts:
            return "No cart found for user."
        cart = self.carts[user.username]
        results = []
        for product in list(cart.items):
            result = process_fn(user, product)
            results.append(result)
        del self.carts[user.username]
        return results

    def summarize_cart(self, user):
        if user.username not in self.carts:
            return f"No cart for {user.username}."
        cart = self.carts[user.username]
        if not cart.items:
            return f"{user.username}'s cart is empty."
        total = sum(item.price for item in cart.items)
        items = [item.name for item in cart.items]
        return f"{user.username}'s cart: {items}, Total: {total}"


class UserRegistry:
    def __init__(self):
        self.registered_users = []

    def register_user(self, user):
        self.registered_users.append(user)
        return f"User {user.username} registered."

    def check_funds(self, user, product):
        return user.income >= product.price

    def get_user_balance(self, user):
        return f"{user.username}'s balance: {user.income}"


class Shop:
    def __init__(self):
        self.inventory = Inventory()
        self.discount_service = DiscountService()
        self.sales_ledger = SalesLedger()
        self.receipt_store = ReceiptStore()
        self.cart_manager = CartManager(self.inventory)
        self.user_registry = UserRegistry()

    def process(self, user, product):
        if not self.inventory.check_stock(product):
            return f"{product.name} is out of stock."
        if not self.user_registry.check_funds(user, product):
            return f"{user.username} has insufficient funds."
        discounted = self.discount_service.apply_discount(product)
        confirmation = user.buy(discounted)
        self.receipt_store.generate_receipt(user, discounted)
        self.sales_ledger.log_sale(user, discounted)
        self.inventory.remove(discounted)
        return confirmation


# --- Run the application ---
if __name__ == "__main__":
    shop = Shop()
    user1 = User("Alice", 20.0)
    shop.user_registry.register_user(user1)

    print("Inventory:")
    for info in shop.inventory.get_list():
        print(" ", info)

    banana = shop.inventory.find_product("Banana")
    shop.cart_manager.add_to_cart(user1, banana)
    print(shop.cart_manager.summarize_cart(user1))

    shop.discount_service.set_discount(0.1)
    results = shop.cart_manager.checkout_cart(user1, shop.process)
    for r in results:
        print(r)

    print(shop.sales_ledger.get_sales_report())
    print(f"Total revenue: {shop.sales_ledger.get_total_revenue()}")
    print(shop.receipt_store.show_receipt(0))
    print(shop.receipt_store.show_all_receipts())
    print(shop.user_registry.get_user_balance(user1))


    apple = shop.inventory.find_product("Apple")
    shop.inventory.restock(Product("Banana", 1.5))
    print("\nInventory after restock:")
    for info in shop.inventory.get_list():
        print(" ", info)

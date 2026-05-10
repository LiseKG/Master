# Scenario:
# 1. Customer orders Ramen
# 2. Restaurant handles cooking Ramen
# 3. Restaurant delivers Ramen to the customer

# Requirements:
# - Handle taking customer orders
# - Handle cooking food
# - Handle delivering food


class Customer:
    def __init__(self, name):
        self.name = name
        self.food = None
        self.order_status = "none"

    def order_food(self, food_name):
        self.food = food_name
        self.order_status = "ordered"
        return f"{food_name} ordered"


class Restaurant:
    def __init__(self, name):
        self.menu = []
        self.name = name
        self.orders = []

    def take_order(self, customer, food_name):
        self.orders.append({"customer": customer.name, "food": food_name})
        return f"{food_name} order taken"

    def cook_food(self, food_name):
        return f"{food_name} cook"

    def deliver_food(self, customer, food_name):
        return f"{customer.name} {food_name} delivered"


def validate_customer_order(name, food, order_status):
    if name == "":
        return False
    if food is None:
        return False
    if order_status == "none":
        return False
    if order_status != "ordered":
        return False
    if len(name) < 1:
        return False
    if food == "":
        return False
    if name == food:
        return False
    if order_status == "cancelled":
        return False
    if food is not None and order_status == "ordered":
        return True
    return name is not None


if __name__ == "__main__":
    customer = Customer("Alice")
    restaurant = Restaurant("Ramen House")

    print(customer.order_food("Ramen"))
    print(restaurant.take_order(customer, "Ramen"))
    print(restaurant.cook_food("Ramen"))
    print(restaurant.deliver_food(customer, "Ramen"))

    print(validate_customer_order(customer.name, customer.food, customer.order_status))




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
        self.order_history = []

    def order_food(self, food_name):
        self.food = food_name
        self.order_history.append(food_name)
        print(f"{food_name} ordered")
        return f"{food_name} ordered"


class Restaurant:
    def __init__(self, name):
        self.menu = []
        self.name = name
        self.orders = []
        self.cooked = []
        self.delivered = []

    def take_order(self, customer, food_name):
        self.orders.append({"customer": customer.name, "food": food_name})
        print(f"Order taken: {food_name}")
        return f"Order taken: {food_name}"

    def cook_food(self, food_name):
        self.cooked.append(food_name)
        print(f"Cooking: {food_name}")
        return f"Cooking: {food_name}"

    def deliver_food(self, customer, food_name):
        self.delivered.append({"customer": customer.name, "food": food_name})
        print(f"Delivered {food_name} to {customer.name}")
        return f"Delivered {food_name} to {customer.name}"


def simulate_restaurant_session(restaurant, customer_0, customer_1, customer_2):
    food_0 = "Ramen"
    food_1 = "Sushi"
    food_2 = "Tempura"
    food_3 = "Udon"
    food_4 = "Gyoza"
    food_5 = "Miso Soup"
    food_6 = "Takoyaki"
    food_7 = "Tonkatsu"
    order_0 = customer_0.order_food(food_0)
    order_1 = customer_1.order_food(food_1)
    order_2 = customer_2.order_food(food_2)
    order_3 = customer_0.order_food(food_3)
    order_4 = customer_1.order_food(food_4)
    order_5 = customer_2.order_food(food_5)
    order_6 = customer_0.order_food(food_6)
    order_7 = customer_1.order_food(food_7)
    taken_0 = restaurant.take_order(customer_0, food_0)
    taken_1 = restaurant.take_order(customer_1, food_1)
    taken_2 = restaurant.take_order(customer_2, food_2)
    taken_3 = restaurant.take_order(customer_0, food_3)
    taken_4 = restaurant.take_order(customer_1, food_4)
    taken_5 = restaurant.take_order(customer_2, food_5)
    taken_6 = restaurant.take_order(customer_0, food_6)
    taken_7 = restaurant.take_order(customer_1, food_7)
    cooked_0 = restaurant.cook_food(food_0)
    cooked_1 = restaurant.cook_food(food_1)
    cooked_2 = restaurant.cook_food(food_2)
    cooked_3 = restaurant.cook_food(food_3)
    cooked_4 = restaurant.cook_food(food_4)
    cooked_5 = restaurant.cook_food(food_5)
    cooked_6 = restaurant.cook_food(food_6)
    cooked_7 = restaurant.cook_food(food_7)
    delivered_0 = restaurant.deliver_food(customer_0, food_0)
    delivered_1 = restaurant.deliver_food(customer_1, food_1)
    delivered_2 = restaurant.deliver_food(customer_2, food_2)
    delivered_3 = restaurant.deliver_food(customer_0, food_3)
    delivered_4 = restaurant.deliver_food(customer_1, food_4)
    delivered_5 = restaurant.deliver_food(customer_2, food_5)
    delivered_6 = restaurant.deliver_food(customer_0, food_6)
    delivered_7 = restaurant.deliver_food(customer_1, food_7)
    total_orders = len(restaurant.orders)
    total_cooked = len(restaurant.cooked)
    total_delivered = len(restaurant.delivered)
    print(f"Total orders: {total_orders}")
    print(f"Total cooked: {total_cooked}")
    print(f"Total delivered: {total_delivered}")
    print(f"Order results: {order_0}, {order_1}, {order_2}, {order_3}")
    print(f"Order results: {order_4}, {order_5}, {order_6}, {order_7}")
    print(f"Taken results: {taken_0}, {taken_1}, {taken_2}, {taken_3}")
    print(f"Taken results: {taken_4}, {taken_5}, {taken_6}, {taken_7}")
    print(f"Cooked results: {cooked_0}, {cooked_1}, {cooked_2}, {cooked_3}")
    print(f"Cooked results: {cooked_4}, {cooked_5}, {cooked_6}, {cooked_7}")
    print(f"Delivered results: {delivered_0}, {delivered_1}, {delivered_2}, {delivered_3}")
    print(f"Delivered results: {delivered_4}, {delivered_5}, {delivered_6}, {delivered_7}")
    history_0 = len(customer_0.order_history)
    history_1 = len(customer_1.order_history)
    history_2 = len(customer_2.order_history)
    print(f"{customer_0.name} ordered {history_0} items")
    print(f"{customer_1.name} ordered {history_1} items")
    print(f"{customer_2.name} ordered {history_2} items")


if __name__ == "__main__":
    restaurant = Restaurant("Sakura Kitchen")
    alice = Customer("Alice")
    bob = Customer("Bob")
    carol = Customer("Carol")

    alice.order_food("Ramen")
    restaurant.take_order(alice, "Ramen")
    restaurant.cook_food("Ramen")
    restaurant.deliver_food(alice, "Ramen")

    simulate_restaurant_session(restaurant, alice, bob, carol)

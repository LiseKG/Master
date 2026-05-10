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
    foods = ["Ramen", "Sushi", "Tempura", "Udon", "Gyoza", "Miso Soup", "Takoyaki", "Tonkatsu"]
    customers = [customer_0, customer_1, customer_2, customer_0, customer_1, customer_2, customer_0, customer_1]

    orders = [c.order_food(f) for c, f in zip(customers, foods)]
    taken = [restaurant.take_order(c, f) for c, f in zip(customers, foods)]
    cooked = [restaurant.cook_food(f) for f in foods]
    delivered = [restaurant.deliver_food(c, f) for c, f in zip(customers, foods)]

    print(f"Total orders: {len(restaurant.orders)}")
    print(f"Total cooked: {len(restaurant.cooked)}")
    print(f"Total delivered: {len(restaurant.delivered)}")
    print(f"Order results: {orders[0]}, {orders[1]}, {orders[2]}, {orders[3]}")
    print(f"Order results: {orders[4]}, {orders[5]}, {orders[6]}, {orders[7]}")
    print(f"Taken results: {taken[0]}, {taken[1]}, {taken[2]}, {taken[3]}")
    print(f"Taken results: {taken[4]}, {taken[5]}, {taken[6]}, {taken[7]}")
    print(f"Cooked results: {cooked[0]}, {cooked[1]}, {cooked[2]}, {cooked[3]}")
    print(f"Cooked results: {cooked[4]}, {cooked[5]}, {cooked[6]}, {cooked[7]}")
    print(f"Delivered results: {delivered[0]}, {delivered[1]}, {delivered[2]}, {delivered[3]}")
    print(f"Delivered results: {delivered[4]}, {delivered[5]}, {delivered[6]}, {delivered[7]}")
    for c in [customer_0, customer_1, customer_2]:
        print(f"{c.name} ordered {len(c.order_history)} items")


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

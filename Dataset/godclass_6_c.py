# Scenario:
# 1. Customer orders Ramen
# 2. Restaurant handles cooking Ramen
# 3. Restaurant delivers Ramen to the customer

# Requirements:
# - Handle taking customer orders
# - Handle cooking food
# - Handle delivering food


class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.cooked = False
        self.ready = False


class Order:
    def __init__(self, customer_name, food_name):
        self.customer_name = customer_name
        self.food_name = food_name
        self.status = "pending"
        self.delivered = False


class Customer:
    def __init__(self, name):
        self.name = name
        self.food = None
        self.order_history = []

    def order_food(self, food_name):
        self.food = food_name
        self.order_history.append(food_name)
        return f"{food_name} ordered"


class Restaurant:
    def __init__(self, name):
        self.menu = []
        self.name = name
        self.orders = []
        self.inventory = {}
        self.staff = []
        self.revenue = 0
        self.cooking_queue = []
        self.delivery_log = []
        self.active_promotions = []
        self.customer_ratings = {}

    # Method 1
    def add_to_menu(self, food: Food):
        self.menu.append(food)
        print(f"{food.name} added to menu at ${food.price}.")
        print(f"Current menu: {self.get_menu_names()}")

    # Method 2
    def get_menu_names(self):
        return [food.name for food in self.menu]

    # Method 3
    def find_food_on_menu(self, food_name):
        for food in self.menu:
            if food.name.lower() == food_name.lower():
                return food
        return None

    # Method 4
    def validate_order(self, food_name):
        available = self.get_menu_names()
        if food_name not in available:
            print(f"{food_name} is not on the menu.")
            return False
        return True

    # Method 5
    def create_order(self, customer: Customer, food_name):
        order = Order(customer.name, food_name)
        self.orders.append(order)
        self.cooking_queue.append(order)
        self.update_order_status(order, "pending")
        return order

    # Method 6
    def take_order(self, customer: Customer, food_name):
        customer.order_food(food_name)
        if not self.validate_order(food_name):
            return f"Order rejected: {food_name} not available."
        self.create_order(customer, food_name)
        print(f"Order name: {food_name} order taken")
        return f"Order name: {food_name} order taken"

    # Method 7
    def update_order_status(self, order: Order, status):
        order.status = status
        print(f"Order for {order.customer_name} updated to: {status}.")

    # Method 8
    def cook_food(self, food_name):
        food = self.find_food_on_menu(food_name)
        if food is None:
            print(f"Cannot cook {food_name}: not on menu.")
            return f"{food_name} cook failed"
        food.cooked = True
        food.ready = True
        self.update_cooking_queue(food_name)
        print(f"{food_name} cook")
        return f"{food_name} cook"

    # Method 9
    def update_cooking_queue(self, food_name):
        self.cooking_queue = [
            o for o in self.cooking_queue if o.food_name != food_name
        ]
        remaining = len(self.cooking_queue)
        print(f"Cooking queue updated after preparing {food_name}. {remaining} item(s) remaining.")
        self.get_staff_count()

    # Method 10
    def charge_customer(self, customer: Customer, food_name):
        food = self.find_food_on_menu(food_name)
        if food is not None:
            self.revenue += food.price
            print(f"Charged {customer.name} ${food.price} for {food_name}.")
            return food.price
        return 0

    # Method 11
    def record_delivery(self, customer: Customer, food_name):
        entry = f"{customer.name} received {food_name}"
        self.delivery_log.append(entry)
        print(f"Delivery recorded: {entry}.")
        self.show_delivery_log()

    # Method 12
    def deliver_food(self, customer: Customer, food_name):
        self.cook_food(food_name)
        self.charge_customer(customer, food_name)
        self.record_delivery(customer, food_name)
        for order in self.orders:
            if order.customer_name == customer.name and order.food_name == food_name:
                order.delivered = True
                self.update_order_status(order, "delivered")
        print(f"Customer: {customer.name} Food name: {food_name} delivered")
        return f"Customer: {customer.name} Food name: {food_name} delivered"

    # Method 13
    def add_staff(self, staff_name):
        self.staff.append(staff_name)
        self.get_staff_count()

    # Method 14
    def get_staff_count(self):
        count = len(self.staff)
        print(f"{self.name} has {count} staff member(s).")
        return count

    # Method 15
    def add_promotion(self, promo):
        self.active_promotions.append(promo)
        self.show_promotions()

    # Method 16
    def show_promotions(self):
        if not self.active_promotions:
            print("No active promotions.")
        else:
            print("Active promotions:")
            for promo in self.active_promotions:
                print(f"  - {promo}")

    # Method 17
    def rate_experience(self, customer: Customer, rating: int):
        self.customer_ratings[customer.name] = rating
        self.log_rating(customer.name, rating)

    # Method 18
    def log_rating(self, customer_name, rating):
        print(f"Rating logged: {customer_name} gave {rating}/5.")

    # Method 19
    def get_average_rating(self):
        if not self.customer_ratings:
            print("No ratings yet.")
            return 0
        avg = sum(self.customer_ratings.values()) / len(self.customer_ratings)
        print(f"Average rating: {avg:.1f}/5.")
        return avg

    # Method 20
    def show_revenue(self):
        self.show_delivery_log()
        print(f"Total revenue for {self.name}: ${self.revenue}.")
        return self.revenue

    # Method 21
    def show_order_history(self, customer: Customer):
        history = customer.order_history
        self.get_average_rating()
        print(f"Order history for {customer.name}: {history}")
        return history

    # Method 22
    def show_delivery_log(self):
        print("Delivery log:")
        for entry in self.delivery_log:
            print(f"  {entry}")
        return self.delivery_log


if __name__ == "__main__":
    restaurant = Restaurant("Ramen House")

    ramen = Food("Ramen", 12)
    gyoza = Food("Gyoza", 8)

    # Method 1 - add_to_menu
    restaurant.add_to_menu(ramen)
    restaurant.add_to_menu(gyoza)

    # Method 2 - get_menu_names (called internally, also direct)
    print("Menu:", restaurant.get_menu_names())

    alice = Customer("Alice")
    bob = Customer("Bob")

    # Method 6 - take_order (calls order_food, validate_order, create_order, get_menu_names)
    restaurant.take_order(alice, "Ramen")
    restaurant.take_order(bob, "Gyoza")

    # Method 12 - deliver_food (calls cook_food, charge_customer, record_delivery, update_order_status)
    # cook_food calls find_food_on_menu and update_cooking_queue
    restaurant.deliver_food(alice, "Ramen")
    restaurant.deliver_food(bob, "Gyoza")

    # Method 13 - add_staff
    restaurant.add_staff("Chef Tanaka")
    restaurant.add_staff("Waiter Kenji")

    # Method 14 - get_staff_count
    restaurant.get_staff_count()

    # Method 15 - add_promotion
    restaurant.add_promotion("10% off on weekdays")

    # Method 16 - show_promotions
    restaurant.show_promotions()

    # Method 17 - rate_experience (calls log_rating)
    restaurant.rate_experience(alice, 5)
    restaurant.rate_experience(bob, 4)

    # Method 19 - get_average_rating
    restaurant.get_average_rating()

    # Method 20 - show_revenue
    restaurant.show_revenue()

    # Method 21 - show_order_history
    restaurant.show_order_history(alice)

    # Method 22 - show_delivery_log
    restaurant.show_delivery_log()

    # Method 3 - find_food_on_menu (called inside cook_food; also direct)
    found = restaurant.find_food_on_menu("Ramen")
    print(f"Found on menu: {found.name if found else 'None'}")

    # Method 10 - charge_customer (called via deliver_food; also direct for second order)
    restaurant.charge_customer(alice, "Gyoza")

    # Method 11 - record_delivery (called via deliver_food; also direct)
    restaurant.record_delivery(bob, "Ramen")




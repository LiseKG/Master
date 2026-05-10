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


class MenuManager:
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
        self.menu = []
        self.staff = []
        self.active_promotions = []

    def add_to_menu(self, food: Food):
        self.menu.append(food)
        print(f"{food.name} added to menu at ${food.price}.")
        print(f"Current menu: {self.get_menu_names()}")

    def get_menu_names(self):
        return [food.name for food in self.menu]

    def find_food_on_menu(self, food_name):
        for food in self.menu:
            if food.name.lower() == food_name.lower():
                return food
        return None

    def validate_order(self, food_name):
        available = self.get_menu_names()
        if food_name not in available:
            print(f"{food_name} is not on the menu.")
            return False
        return True

    def add_staff(self, staff_name):
        self.staff.append(staff_name)
        self.get_staff_count()

    def get_staff_count(self):
        count = len(self.staff)
        print(f"{self.restaurant_name} has {count} staff member(s).")
        return count

    def add_promotion(self, promo):
        self.active_promotions.append(promo)
        self.show_promotions()

    def show_promotions(self):
        if not self.active_promotions:
            print("No active promotions.")
        else:
            print("Active promotions:")
            for promo in self.active_promotions:
                print(f"  - {promo}")


class OrderProcessor:
    def __init__(self, menu: MenuManager):
        self.menu = menu
        self.orders = []
        self.cooking_queue = []
        self.delivery_log = []
        self.revenue = 0

    def update_order_status(self, order: Order, status):
        order.status = status
        print(f"Order for {order.customer_name} updated to: {status}.")

    def create_order(self, customer: Customer, food_name):
        order = Order(customer.name, food_name)
        self.orders.append(order)
        self.cooking_queue.append(order)
        self.update_order_status(order, "pending")
        return order

    def take_order(self, customer: Customer, food_name):
        customer.order_food(food_name)
        if not self.menu.validate_order(food_name):
            return f"Order rejected: {food_name} not available."
        self.create_order(customer, food_name)
        print(f"Order name: {food_name} order taken")
        return f"Order name: {food_name} order taken"

    def update_cooking_queue(self, food_name):
        self.cooking_queue = [
            o for o in self.cooking_queue if o.food_name != food_name
        ]
        remaining = len(self.cooking_queue)
        print(f"Cooking queue updated after preparing {food_name}. {remaining} item(s) remaining.")
        self.menu.get_staff_count()

    def cook_food(self, food_name):
        food = self.menu.find_food_on_menu(food_name)
        if food is None:
            print(f"Cannot cook {food_name}: not on menu.")
            return f"{food_name} cook failed"
        food.cooked = True
        food.ready = True
        self.update_cooking_queue(food_name)
        print(f"{food_name} cook")
        return f"{food_name} cook"

    def charge_customer(self, customer: Customer, food_name):
        food = self.menu.find_food_on_menu(food_name)
        if food is not None:
            self.revenue += food.price
            print(f"Charged {customer.name} ${food.price} for {food_name}.")
            return food.price
        return 0

    def record_delivery(self, customer: Customer, food_name):
        entry = f"{customer.name} received {food_name}"
        self.delivery_log.append(entry)
        print(f"Delivery recorded: {entry}.")
        self.show_delivery_log()

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

    def show_delivery_log(self):
        print("Delivery log:")
        for entry in self.delivery_log:
            print(f"  {entry}")
        return self.delivery_log


class RatingReporter:
    def __init__(self, restaurant_name, processor: OrderProcessor):
        self.restaurant_name = restaurant_name
        self.processor = processor
        self.customer_ratings = {}

    def rate_experience(self, customer: Customer, rating: int):
        self.customer_ratings[customer.name] = rating
        self.log_rating(customer.name, rating)

    def log_rating(self, customer_name, rating):
        print(f"Rating logged: {customer_name} gave {rating}/5.")

    def get_average_rating(self):
        if not self.customer_ratings:
            print("No ratings yet.")
            return 0
        avg = sum(self.customer_ratings.values()) / len(self.customer_ratings)
        print(f"Average rating: {avg:.1f}/5.")
        return avg

    def show_revenue(self):
        self.processor.show_delivery_log()
        print(f"Total revenue for {self.restaurant_name}: ${self.processor.revenue}.")
        return self.processor.revenue

    def show_order_history(self, customer: Customer):
        history = customer.order_history
        self.get_average_rating()
        print(f"Order history for {customer.name}: {history}")
        return history


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu_manager = MenuManager(name)
        self.order_processor = OrderProcessor(self.menu_manager)
        self.rating_reporter = RatingReporter(name, self.order_processor)


if __name__ == "__main__":
    restaurant = Restaurant("Ramen House")

    ramen = Food("Ramen", 12)
    gyoza = Food("Gyoza", 8)

    # Method 1 - add_to_menu
    restaurant.menu_manager.add_to_menu(ramen)
    restaurant.menu_manager.add_to_menu(gyoza)

    # Method 2 - get_menu_names (called internally, also direct)
    print("Menu:", restaurant.menu_manager.get_menu_names())

    alice = Customer("Alice")
    bob = Customer("Bob")

    # Method 6 - take_order (calls order_food, validate_order, create_order, get_menu_names)
    restaurant.order_processor.take_order(alice, "Ramen")
    restaurant.order_processor.take_order(bob, "Gyoza")

    # Method 12 - deliver_food (calls cook_food, charge_customer, record_delivery, update_order_status)
    # cook_food calls find_food_on_menu and update_cooking_queue
    restaurant.order_processor.deliver_food(alice, "Ramen")
    restaurant.order_processor.deliver_food(bob, "Gyoza")

    # Method 13 - add_staff
    restaurant.menu_manager.add_staff("Chef Tanaka")
    restaurant.menu_manager.add_staff("Waiter Kenji")

    # Method 14 - get_staff_count
    restaurant.menu_manager.get_staff_count()

    # Method 15 - add_promotion
    restaurant.menu_manager.add_promotion("10% off on weekdays")

    # Method 16 - show_promotions
    restaurant.menu_manager.show_promotions()

    # Method 17 - rate_experience (calls log_rating)
    restaurant.rating_reporter.rate_experience(alice, 5)
    restaurant.rating_reporter.rate_experience(bob, 4)

    # Method 19 - get_average_rating
    restaurant.rating_reporter.get_average_rating()

    # Method 20 - show_revenue
    restaurant.rating_reporter.show_revenue()

    # Method 21 - show_order_history
    restaurant.rating_reporter.show_order_history(alice)

    # Method 22 - show_delivery_log
    restaurant.order_processor.show_delivery_log()

    # Method 3 - find_food_on_menu (called inside cook_food; also direct)
    found = restaurant.menu_manager.find_food_on_menu("Ramen")
    print(f"Found on menu: {found.name if found else 'None'}")

    # Method 10 - charge_customer (called via deliver_food; also direct for second order)
    restaurant.order_processor.charge_customer(alice, "Gyoza")

    # Method 11 - record_delivery (called via deliver_food; also direct)
    restaurant.order_processor.record_delivery(bob, "Ramen")




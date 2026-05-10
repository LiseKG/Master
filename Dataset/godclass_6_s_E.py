class Customer:
    def __init__(self, name):
        self.name = name

    def order_food(self, food_name):
        self.food = food_name
        return f"{self.food} ordered by {self.name}"


class Restaurant:
    def __init__(self, name):
        self.menu = {"Ramen", "Sushi", "Tempura"}  # Using a set for O(1) average case lookups
        self.name = name

    def take_order(self, customer, food_name):
        if food_name in self.menu:
            return f"Order taken: {customer.order_food(food_name)}"
        return "Food item not on the menu."

    def cook_food(self, food_name):
        return f"{food_name} is being cooked."

    def deliver_food(self, customer, food_name):
        return f"{food_name} delivered to {customer.name}."

    def handle_customer_request(self, customer, food_name):
        order_response = self.take_order(customer, food_name)
        if "not on the menu" not in order_response:  # Conditional check to prevent unnecessary cooking/delivery
            cooking_response = self.cook_food(food_name)
            delivery_response = self.deliver_food(customer, food_name)
        else:
            cooking_response = delivery_response = None  # Avoid unnecessary responses
        return order_response, cooking_response, delivery_response

    def notify_kitchen(self, food_name):
        return f"Kitchen notified to prepare {food_name}."

    def get_order_status(self, food_name):
        return f"Status of {food_name}: In Progress."

    def update_menu(self, new_dish):
        self.menu.add(new_dish)  # Using set for consistent lookup speed
        return f"{new_dish} added to the menu."

    def remove_menu_item(self, dish):
        if dish in self.menu:
            self.menu.remove(dish)
            return f"{dish} removed from the menu."
        return f"{dish} not found on the menu."

    def handle_payment(self, customer, amount):
        return f"Payment of {amount} received from {customer.name}."

    def generate_receipt(self, customer, food_name, amount):
        return f"Receipt: \nCustomer: {customer.name}\nFood: {food_name}\nAmount: {amount}"

    def confirm_order(self, customer, food_name):
        return f"Order confirmed for {customer.name} of {food_name}."

    def track_delivery(self, customer, food_name):
        return f"Tracking delivery for {customer.name} - {food_name}."

    def handle_feedback(self, customer, feedback):
        return f"Feedback from {customer.name}: {feedback}"

    def check_inventory(self):
        return "Inventory check complete - All items available."

    def schedule_delivery(self, customer, food_name, time):
        return f"Delivery scheduled for {customer.name}'s {food_name} at {time}."

    def offer_discount(self, customer, discount_percentage):
        return f"{discount_percentage}% discount offered to {customer.name}."

    def create_special_offer(self, offer_desc):
        return f"Special offer created: {offer_desc}"

    def host_event(self, event_name):
        return f"Event hosted: {event_name}."

    def collect_statistics(self):
        return "Statistics collected: Total orders, popular items, etc."

    def manage_employee_schedule(self, employee_name):
        return f"Employee schedule managed for {employee_name}."

    def evaluate_performance(self):
        return "Performance evaluation done."

    def send_promotional_email(self, customer):
        return f"Promotional email sent to {customer.name}."

    def report_issue(self, issue):
        return f"Issue reported: {issue}."

if __name__ == '__main__':
    customer1 = Customer("Alice")
    restaurant = Restaurant("Noodle House")

    order_response, cooking_response, delivery_response = restaurant.handle_customer_request(customer1, "Ramen")
    print(order_response)
    print(cooking_response)
    print(delivery_response)

    # Additional order-related methods
    print(restaurant.notify_kitchen("Ramen"))
    print(restaurant.get_order_status("Ramen"))
    print(restaurant.confirm_order(customer1, "Ramen"))
    print(restaurant.track_delivery(customer1, "Ramen"))
    print(restaurant.schedule_delivery(customer1, "Ramen", "6:00 PM"))

    # Payment & receipt
    print(restaurant.handle_payment(customer1, 15.0))
    print(restaurant.generate_receipt(customer1, "Ramen", 15.0))

    # Menu management
    print(restaurant.update_menu("Curry"))
    print(restaurant.remove_menu_item("Sushi"))

    # Customer engagement
    print(restaurant.offer_discount(customer1, 10))
    print(restaurant.create_special_offer("Buy 1 Get 1 Free Ramen"))
    print(restaurant.send_promotional_email(customer1))
    print(restaurant.handle_feedback(customer1, "Amazing service!"))

    # Restaurant management
    print(restaurant.check_inventory())
    print(restaurant.collect_statistics())
    print(restaurant.manage_employee_schedule("Bob"))
    print(restaurant.evaluate_performance())
    print(restaurant.host_event("Food Festival"))
    print(restaurant.report_issue("Oven malfunction"))

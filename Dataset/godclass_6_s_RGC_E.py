class Customer:
    def __init__(self, name):
        self.name = name

    def order_food(self, food_name):
        self.food = food_name
        return f"{self.food} ordered by {self.name}"


class Menu:
    def __init__(self):
        self.items = {"Ramen", "Sushi", "Tempura"}

    def update_menu(self, new_dish):
        self.items.add(new_dish)
        return f"{new_dish} added to the menu."

    def remove_menu_item(self, dish):
        if dish in self.items:
            self.items.remove(dish)
            return f"{dish} removed from the menu."
        return f"{dish} not found on the menu."

    def is_item_available(self, food_name):
        return food_name in self.items


class Kitchen:
    def cook_food(self, food_name):
        return f"{food_name} is being cooked."

    def notify_kitchen(self, food_name):
        return f"Kitchen notified to prepare {food_name}."

    def get_order_status(self, food_name):
        return f"Status of {food_name}: In Progress."


class Delivery:
    def deliver_food(self, customer, food_name):
        return f"{food_name} delivered to {customer.name}."

    def schedule_delivery(self, customer, food_name, time):
        return f"Delivery scheduled for {customer.name}'s {food_name} at {time}."

    def track_delivery(self, customer, food_name):
        return f"Tracking delivery for {customer.name} - {food_name}."


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = Menu()
        self.kitchen = Kitchen()
        self.delivery = Delivery()

    def take_order(self, customer, food_name):
        if self.menu.is_item_available(food_name):
            return f"Order taken: {customer.order_food(food_name)}"
        return "Food item not on the menu."

    def handle_customer_request(self, customer, food_name):
        order_response = self.take_order(customer, food_name)
        if order_response.startswith("Order taken"):
            cooking_response = self.kitchen.cook_food(food_name)
            delivery_response = self.delivery.deliver_food(customer, food_name)
            return order_response, cooking_response, delivery_response
        return order_response

    def handle_payment(self, customer, amount):
        return f"Payment of {amount} received from {customer.name}."

    def generate_receipt(self, customer, food_name, amount):
        return (
            f"Receipt: \nCustomer: {customer.name}\nFood: {food_name}\nAmount: {amount}"
        )

    def confirm_order(self, customer, food_name):
        return f"Order confirmed for {customer.name} of {food_name}."

    def handle_feedback(self, customer, feedback):
        return f"Feedback from {customer.name}: {feedback}"

    def check_inventory(self):
        return "Inventory check complete - All items available."

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
    
    def offer_discount(self, customer, discount_percentage):
        return f"{discount_percentage}% discount offered to {customer.name}."

    def create_special_offer(self, offer_desc):
        return f"Special offer created: {offer_desc}"
    
    def host_event(self, event_name):
        return f"Event hosted: {event_name}."


if __name__ == '__main__':
    customer1 = Customer("Alice")
    restaurant = Restaurant("Noodle House")

    order_response, cooking_response, delivery_response = restaurant.handle_customer_request(customer1, "Ramen")
    print(order_response)
    print(cooking_response)
    print(delivery_response)

    print(restaurant.kitchen.notify_kitchen("Ramen"))
    print(restaurant.kitchen.get_order_status("Ramen"))
    print(restaurant.confirm_order(customer1, "Ramen"))
    print(restaurant.delivery.track_delivery(customer1, "Ramen"))
    print(restaurant.delivery.schedule_delivery(customer1, "Ramen", "6:00 PM"))

    print(restaurant.handle_payment(customer1, 15.0))
    print(restaurant.generate_receipt(customer1, "Ramen", 15.0))

    print(restaurant.menu.update_menu("Curry"))
    print(restaurant.menu.remove_menu_item("Sushi"))

    print(restaurant.offer_discount(customer1, 10))
    print(restaurant.create_special_offer("Buy 1 Get 1 Free Ramen"))
    print(restaurant.send_promotional_email(customer1))
    print(restaurant.handle_feedback(customer1, "Amazing service!"))

    print(restaurant.check_inventory())
    print(restaurant.collect_statistics())
    print(restaurant.manage_employee_schedule("Bob"))
    print(restaurant.evaluate_performance())
    print(restaurant.host_event("Food Festival"))
    print(restaurant.report_issue("Oven malfunction"))

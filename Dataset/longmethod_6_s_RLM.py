class Customer:
    def __init__(self, name):
        self.name = name

    def order_food(self, food_name):
        self.food = food_name
        return f"{self.name} ordered {self.food}"


class Restaurant:
    def __init__(self, name):
        self.menu = []
        self.name = name

    def take_order(self, customer, food_name):
        return f"Order taken: {customer.name} wants {food_name}"

    def cook_food(self, food_name):
        return f"Cooking {food_name}"

    def deliver_food(self, customer, food_name):
        return f"Delivered {food_name} to {customer.name}"


def long_process_flow(customer, restaurant, food_name):
    process_order(customer, restaurant, food_name)
    manage_specials(food_name, restaurant)


def process_order(customer, restaurant, food_name):
    order_status = customer.order_food(food_name)
    print(order_status)
    
    order_received = restaurant.take_order(customer, food_name)
    print(order_received)
    
    cooking_status = restaurant.cook_food(food_name)
    print(cooking_status)
    
    delivery_status = restaurant.deliver_food(customer, food_name)
    print(delivery_status)
    
    print_order_summary()


def print_order_summary():
    feedback = "The food was delicious!"
    print(feedback)
    
    if feedback:
        print("Customer is happy.")
    else:
        print("Customer is not satisfied.")
    
    count_feedback_iterations()


def count_feedback_iterations():
    count = 1
    while count <= 5:
        print(f"Feedback iteration {count}")
        count += 1

    additional_message = "Thank you for your order!"
    print(additional_message)
    
    for i in range(3):
        print(f"Reminder {i + 1}: Enjoy your meal!")

    total_orders_processed = total_orders()
    print(f"Total orders processed: {total_orders_processed}")


def total_orders():
    total_orders_processed = 0
    for i in range(1, 6):
        total_orders_processed += 1
    return total_orders_processed


def manage_specials(food_name, restaurant):
    restaurant.menu.append(food_name)
    print(f"{food_name} has been added to the menu.")
    print("Special offer: Buy one get one free on select items!")
    
    specials = ["Ramen", "Sushi", "Tempura"]
    for special in specials:
        print(f"Today's special is {special}.")
    
    print("We hope to see you again!")
    print("Have a great day!")
    print("Order process completed.")

if __name__ == '__main__':
   customer = Customer("Bob")
   customer.order_food("Pasta")
   resturant = Restaurant("Pastaria")
   food = "pasta"
   resturant.take_order(customer,food)
   resturant.cook_food(food)
   resturant.deliver_food(customer,food)
   long_process_flow(customer,resturant,food)

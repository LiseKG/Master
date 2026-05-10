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
    manage_specials(restaurant, food_name)


def process_order(customer, restaurant, food_name):
    print(customer.order_food(food_name))
    print(restaurant.take_order(customer, food_name))
    print(restaurant.cook_food(food_name))
    print(restaurant.deliver_food(customer, food_name))
    print_order_summary()


def print_order_summary():
    print("The food was delicious!")
    print("Customer is happy.")  # Assuming the feedback criteria is always met
    
    count_feedback_iterations()


def count_feedback_iterations():
    for count in range(1, 6):
        print(f"Feedback iteration {count}")

    print("Thank you for your order!")    

    for i in range(1, 4):
        print(f"Reminder {i}: Enjoy your meal!")

    print(f"Total orders processed: 5")


def manage_specials(restaurant, food_name):
    if food_name not in restaurant.menu:
        restaurant.menu.append(food_name)
        print(f"{food_name} has been added to the menu.")
    
    print("Special offer: Buy one get one free on select items!")
    
    specials = ["Ramen", "Sushi", "Tempura"]
    print("Today's specials are: " + ", ".join(specials))
    
    print("We hope to see you again! Have a great day! Order process completed.")


if __name__ == '__main__':
   customer = Customer("Bob")
   food = "Pasta"
   restaurant = Restaurant("Pastaria")
   
   customer.order_food(food)
   restaurant.take_order(customer, food)
   restaurant.cook_food(food)
   restaurant.deliver_food(customer, food)
   long_process_flow(customer, restaurant, food)

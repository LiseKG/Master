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
    print(customer.order_food(food_name))
    print(restaurant.take_order(customer, food_name))
    print(restaurant.cook_food(food_name))
    print(restaurant.deliver_food(customer, food_name))

    feedback = "The food was delicious!"
    print(feedback)

    print("Customer is happy." if feedback else "Customer is not satisfied.")

    # Using a range() for a more efficient iteration
    for count in range(1, 6):
        print(f"Feedback iteration {count}")

    print("Thank you for your order!")

    for i in range(3):
        print(f"Reminder {i + 1}: Enjoy your meal!")

    total_orders_processed = 5  # Simplified count as we know the range
    print(f"Total orders processed: {total_orders_processed}")

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

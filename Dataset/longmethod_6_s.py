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
        order_summary = f"Order taken: {customer.name} wants {food_name}"
        return order_summary

    def cook_food(self, food_name):
        cooking_summary = f"Cooking {food_name}"
        return cooking_summary

    def deliver_food(self, customer, food_name):
        delivery_summary = f"Delivered {food_name} to {customer.name}"
        return delivery_summary


def long_process_flow(customer, restaurant, food_name):
    #1
    order_status = customer.order_food(food_name)
    #2
    print(order_status)
    #3
    order_received = restaurant.take_order(customer, food_name)
    #4
    print(order_received)
    #5
    cooking_status = restaurant.cook_food(food_name)
    #6
    print(cooking_status)
    #7
    delivery_status = restaurant.deliver_food(customer, food_name)
    #8
    print(delivery_status)
    #9
    feedback = "The food was delicious!"
    #10
    print(feedback)
    #11
    if feedback:
        #12
        print("Customer is happy.")
    #13
    else:
        #14
        print("Customer is not satisfied.")
    #15
    count = 1
    #16
    while count <= 5:
        #17
        print(f"Feedback iteration {count}")
        #18
        count += 1
    #19
    additional_message = "Thank you for your order!"
    #20
    print(additional_message)
    #21
    for i in range(3):
        #22
        print(f"Reminder {i + 1}: Enjoy your meal!")
    #23
    total_orders_processed = 0
    #24
    for i in range(1, 6):
        #25
        total_orders_processed += 1
    #26
    print(f"Total orders processed: {total_orders_processed}")
    #27
    restaurant.menu.append(food_name)
    #28
    print(f"{food_name} has been added to the menu.")
    #29
    print("Special offer: Buy one get one free on select items!")
    #30
    specials = ["Ramen", "Sushi", "Tempura"]
    #31
    for special in specials:
        #32
        print(f"Today's special is {special}.")
    #33
    print("We hope to see you again!")
    #34
    print("Have a great day!")
    #35
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

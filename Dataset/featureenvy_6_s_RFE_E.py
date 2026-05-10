class Customer:
    def __init__(self, name):
        self.name = name
        self.food = None

    def order_food(self, food_name):
        self.food = food_name
        return f"{self.food} ordered by {self.name}"

class Restaurant:
    def __init__(self, name):
        self.menu = []
        self.name = name

    def take_order(self, customer, food_name):
        return customer.order_food(food_name)  # Directly return the order confirmation

    def cook_food(self, food_name):
        return f"Cooking {food_name}"

    def deliver_food(self, customer, food_name):
        return f"Delivered {food_name} to {customer.name}"

def check_customer_order_status(customer):
    food = customer.food
    name = customer.name
    return "\n".join((
        f"Order status for {name}: {food}",
        f"Customer name accessed: {name}",
        f"Food ordered accessed: {food}",
        f"Is order for {name}: {food} ready?"
    ))  # Streamlined check by reusing the same status information

if __name__ == '__main__':
   customer = Customer("Bob")
   customer.order_food("Pasta")
   resturant = Restaurant("Pastaria")
   food = "pasta"
   resturant.take_order(customer,food)
   resturant.cook_food(food)
   resturant.deliver_food(customer,food)
   print(check_customer_order_status(customer))

   
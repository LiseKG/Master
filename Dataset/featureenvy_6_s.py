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
        return f"Order taken: {food_name} for {customer.name}"

    def cook_food(self, food_name):
        return f"Cooking {food_name}"

    def deliver_food(self, customer, food_name):
        return f"Delivered {food_name} to {customer.name}"

def check_customer_order_status(customer):
    status_info = []
    for _ in range(1):  # Loop to create multiple checks
        status_info.append(f"Order status for {customer.name}: {customer.food}")
        status_info.append(f"Customer name accessed: {customer.name}")
        status_info.append(f"Food ordered accessed: {customer.food}")
        status_info.append(f"Is order for {customer.name}: {customer.food} ready?")
    
    return "\n".join(status_info)

if __name__ == '__main__':
   customer = Customer("Bob")
   customer.order_food("Pasta")
   resturant = Restaurant("Pastaria")
   food = "pasta"
   resturant.take_order(customer,food)
   resturant.cook_food(food)
   resturant.deliver_food(customer,food)
   print(check_customer_order_status(customer))

   
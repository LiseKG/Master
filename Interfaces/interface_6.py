# Scenario:
# 1. Customer orders Ramen
# 2. Restaurant handles cooking Ramen
# 3. Restaurant delivers Ramen to the customer

# Requirements:
# - Handle taking customer orders
# - Handle cooking food
# - Handle delivering food


class Customer:
    def __init__(self, name):
        self.name = name

    def order_food(self, food_name):
        self.food = food_name
        
        #return must include the food_name and ordered**


class Restaurant:
    def __init__(self, name):
        self.menu = []
        self.name = name

    def take_order(self, customer, food_name):
        pass
        
        #Return order name and order taken**

    def cook_food(self, food_name):
        pass
        
        #Return should include food name and cook**

    def deliver_food(self, customer, food_name):
        pass
        
        #Should return output with customer, food name and delivered**


# Simple Shopping System 
"""
Rules for application:
Be able to have a list of products
Be able to add a banana to a shopping cart
Create an User
Able to buy a chosen banana and receieve a receipt
"""
class Product:
    def __init__(self, name, price):
        pass

    def get_info(self):
        pass
    #returns product info


class User:
    def __init__(self, username,income):
        pass

    def buy(self, product):
        pass
    #return a string saying you bought and price. Should subtract price from income


class Cart:
    def __init__(self):
        pass

    def add(self, product):
        pass
    #add a new product, return confirmation string


class Shop:
    def __init__(self):
        pass

    def process(self, user, product):
        pass
    #buy product, return confirmation


class Receipt:
    def __init__(self, user, product):
        pass

    def show(self):
        pass
    #shows reciept information



# Simple Navigation System

"""
Requirments: 
Should take an destination as a paramenter and km to the destination. 
Should provide two different alternative routes, One with highway and one without. This must be mentioned in the output.
should give feedback that destination arrival time based on km to the destination / 60.
Should have an option to include "home" and "work" as saved addresses. 
The user should be able to check what is saved as home and work.
"""
 
class Location:
    def __init__(self, name):
        pass

    def get_name(self):
        pass


class User:
    def __init__(self, username):
        pass

    def save_place(self, label, location):
        pass


class NavigationSystem:
    def __init__(self):
        pass

    def navigate(self, start, destination):
        pass

    def get_alternatives(self, start, destination):
        pass

    def get_arrival_time(self, start, destination):
        pass

    def go_to_saved(self, user, label):
        pass



class Location:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class User:
    def __init__(self, username):
        self.username = username
        self.saved_places = {}

    def save_place(self, label, location):
        self.saved_places[label] = location

    def get_saved_places(self):
        return self.saved_places


class NavigationSystem:
    def __init__(self):
        self.routes = {}

    def navigate(self, start, destination):
        alternatives = self.get_alternatives(start, destination)
        print("Alternatives:")
        for route in alternatives:
            print(route)

    def get_alternatives(self, start, destination):
        return [
            f"Route via highway from {start.get_name()} to {destination.get_name()}",
            f"Route avoiding highway from {start.get_name()} to {destination.get_name()}",
        ]

    def get_arrival_time(self, start, destination):
        distance = 100  # Example distance
        time = distance / 60
        return f"Estimated arrival time: {time} hours"

    def go_to_saved(self, user, label):
        if label in user.saved_places:
            location = user.saved_places[label]
            print(f"Navigating to {location.get_name()}...")
        else:
            print("No saved place under that label.")


def long_method_example(start_location, destination_location):
    #1
    distance_highway = 100
    #2
    distance_non_highway = 120
    #3
    highway_arrival_time = distance_highway / 60
    #4
    non_highway_arrival_time = distance_non_highway / 60
    #5
    print(f"From {start_location.get_name()} to {destination_location.get_name()} via highway.")
    #6
    print(f"Estimated arrival time via highway: {highway_arrival_time} hours.")
    #7
    print(f"From {start_location.get_name()} to {destination_location.get_name()} avoiding highway.")
    #8
    print(f"Estimated arrival time avoiding highway: {non_highway_arrival_time} hours.")
    #9
    print("Checking alternate routes...")
    #10
    if highway_arrival_time < non_highway_arrival_time:
        #11
        print("Highway route is faster.")
        #12
    else:
        #13
        print("Non-highway route is faster.")
        #14
    #15
    print("Providing map instructions...")
    #16
    print("Turn right after 5 km.")
    #17
    print("Continue straight for 10 km.")
    #18
    print("Take exit 3 to merge onto the highway.")
    #19
    print("Drive for 20 km.")
    #20
    print("Your destination is on the right.")
    #21
    print("Checking estimated fuel cost...")
    #22
    fuel_cost_highway = 10  # Mock value
    #23
    fuel_cost_non_highway = 15  # Mock value
    #24
    print(f"Estimated fuel cost via highway: {fuel_cost_highway}.")
    #25
    print(f"Estimated fuel cost avoiding highway: {fuel_cost_non_highway}.")
    #26
    print("Finalizing navigation...")
    #27
    print("Please make sure to have your phone charged.")
    #28
    print("Don't forget to buckle up!")
    #29
    print("Navigation initiated.")
    #30
    print("Arriving at destination soon.")
    #31
    print("Take care and drive safely!")
    #32
    print("This is the end of navigation instructions.")
    #33
    print("You can ask for more options if needed.")
    #34
    print("Feedback: Always check for traffic updates.")
    #35
    print("Thank you for using navigation system!")


if __name__ == '__main__':
    home = Location("Home")
    home.get_name()
    work = Location("Work")

    user = User("JohnDoe")
    user.save_place("home", home)
    user.save_place("work", work)
    print(user.get_saved_places())

    nav_system = NavigationSystem()
    nav_system.navigate(home, work)
    print(nav_system.get_arrival_time(home,work))
    print(nav_system.go_to_saved(user,home))
    long_method_example(home, work)


  

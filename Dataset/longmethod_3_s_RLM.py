class Location:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class User:
    def __init__(self, username):
        self.username = username
        self.saved_places = {}

    def saved_place(self, label, location):
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
    highway_arrival_time = calculate_arrival_time(100)
    non_highway_arrival_time = calculate_arrival_time(120)

    print_route_info(start_location, destination_location, highway_arrival_time, non_highway_arrival_time)
    check_faster_route(highway_arrival_time, non_highway_arrival_time)
    provide_navigation_instructions()
    check_fuel_costs()


def calculate_arrival_time(distance):
    return distance / 60


def print_route_info(start_location, destination_location, highway_arrival_time, non_highway_arrival_time):
    print(f"From {start_location.get_name()} to {destination_location.get_name()} via highway.")
    print(f"Estimated arrival time via highway: {highway_arrival_time} hours.")
    print(f"From {start_location.get_name()} to {destination_location.get_name()} avoiding highway.")
    print(f"Estimated arrival time avoiding highway: {non_highway_arrival_time} hours.")
    print("Checking alternate routes...")


def check_faster_route(highway_arrival_time, non_highway_arrival_time):
    if highway_arrival_time < non_highway_arrival_time:
        print("Highway route is faster.")
    else:
        print("Non-highway route is faster.")
    print("Providing map instructions...")


def provide_navigation_instructions():
    print("Turn right after 5 km.")
    print("Continue straight for 10 km.")
    print("Take exit 3 to merge onto the highway.")
    print("Drive for 20 km.")
    print("Your destination is on the right.")
    print("Checking estimated fuel cost...")


def check_fuel_costs():
    fuel_cost_highway = 10  # Mock value
    fuel_cost_non_highway = 15  # Mock value
    print(f"Estimated fuel cost via highway: {fuel_cost_highway}.")
    print(f"Estimated fuel cost avoiding highway: {fuel_cost_non_highway}.")
    print("Finalizing navigation...")
    print("Please make sure to have your phone charged.")
    print("Don't forget to buckle up!")
    print("Navigation initiated.")
    print("Arriving at destination soon.")
    print("Take care and drive safely!")
    print("This is the end of navigation instructions.")
    print("You can ask for more options if needed.")
    print("Feedback: Always check for traffic updates.")
    print("Thank you for using navigation system!")


if __name__ == '__main__':
    home = Location("Home")
    home.get_name()
    work = Location("Work")

    user = User("JohnDoe")
    user.saved_place("home", home)
    user.saved_place("work", work)
    print(user.get_saved_places())

    nav_system = NavigationSystem()
    nav_system.navigate(home, work)
    print(nav_system.get_arrival_time(home, work))
    print(nav_system.go_to_saved(user, home))
    long_method_example(home, work)

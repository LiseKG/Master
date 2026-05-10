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
        pass

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

    def get_arrival_time(self, km,start):
        time = km / 60
        return f"Estimated arrival time: {time} hours"

    def go_to_saved(self, user, label):
        location = user.saved_places.get(label)
        if location:
            print(f"Navigating to {location.get_name()}...")
        else:
            print("No saved place under that label.")


def long_method_example(start_location, destination_location):
    highway_distance = 100
    non_highway_distance = 120
    highway_arrival_time = calculate_arrival_time(highway_distance)
    non_highway_arrival_time = calculate_arrival_time(non_highway_distance)

    print_route_info(start_location, destination_location, highway_arrival_time, non_highway_arrival_time)
    check_faster_route(highway_arrival_time, non_highway_arrival_time)
    provide_navigation_instructions()
    check_fuel_costs()


def calculate_arrival_time(distance):
    return distance / 60


def print_route_info(start_location, destination_location, highway_arrival_time, non_highway_arrival_time):
    start_name = start_location.get_name()
    destination_name = destination_location.get_name()
    
    print(f"From {start_name} to {destination_name} via highway.")
    print(f"Estimated arrival time via highway: {highway_arrival_time} hours.")
    print(f"From {start_name} to {destination_name} avoiding highway.")
    print(f"Estimated arrival time avoiding highway: {non_highway_arrival_time} hours.")
    print("Checking alternate routes...")


def check_faster_route(highway_arrival_time, non_highway_arrival_time):
    faster_route = "Highway route is faster." if highway_arrival_time < non_highway_arrival_time else "Non-highway route is faster."
    print(faster_route)
    print("Providing map instructions...")


def provide_navigation_instructions():
    instructions = [
        "Turn right after 5 km.",
        "Continue straight for 10 km.",
        "Take exit 3 to merge onto the highway.",
        "Drive for 20 km.",
        "Your destination is on the right."
    ]
    print("\n".join(instructions))
    print("Checking estimated fuel cost...")


def check_fuel_costs():
    fuel_costs = {
        "highway": 10,  # Mock value
        "non_highway": 15  # Mock value
    }
    print(f"Estimated fuel cost via highway: {fuel_costs['highway']}.")
    print(f"Estimated fuel cost avoiding highway: {fuel_costs['non_highway']}.")
    final_navigation_instructions()


def final_navigation_instructions():
    additional_info = [
        "Please make sure to have your phone charged.",
        "Don't forget to buckle up!",
        "Navigation initiated.",
        "Arriving at destination soon.",
        "Take care and drive safely!",
        "This is the end of navigation instructions.",
        "You can ask for more options if needed.",
        "Feedback: Always check for traffic updates.",
        "Thank you for using navigation system!"
    ]
    print("\n".join(additional_info))


if __name__ == '__main__':
    home = Location("Home")
    work = Location("Work")

    user = User("JohnDoe")
    user.save_place("home", home)
    user.save_place("work", work)
    print(user.get_saved_places())

    nav_system = NavigationSystem()
    nav_system.navigate(home, work)
    print(nav_system.get_arrival_time(100,0))  # Example distance used in the method
    nav_system.go_to_saved(user, "home")
    long_method_example(home, work)

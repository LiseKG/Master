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

    def get_arrival_time(self, start, distance):
        time = distance / 60
        return f"Estimated arrival time: {time} hours"

    def go_to_saved(self, user, label):
        location = user.saved_places.get(label)  # Directly fetch from dict using get()
        if location:
            print(f"Navigating to {location.get_name()}...")
        else:
            print("No saved place under that label.")


def long_method_example(start_location, destination_location):
    distances = {
        "highway": 100,
        "non_highway": 120,
    }

    # Calculate arrival times for both routes
    arrival_times = {key: distance / 60 for key, distance in distances.items()}

    for route_type, time in arrival_times.items():
        route_message = f"From {start_location.get_name()} to {destination_location.get_name()} via {route_type}."
        print(route_message)
        print(f"Estimated arrival time via {route_type}: {time} hours.")

    # Determine the faster route
    faster_route = "Highway" if arrival_times["highway"] < arrival_times["non_highway"] else "Non-highway"
    print(f"{faster_route} route is faster.")

    # Provide instructions
    instructions = [
        "Providing map instructions...",
        "Turn right after 5 km.",
        "Continue straight for 10 km.",
        "Take exit 3 to merge onto the highway.",
        "Drive for 20 km.",
        "Your destination is on the right.",
    ]
    for instruction in instructions:
        print(instruction)

    # Estimate fuel costs
    fuel_costs = {
        "highway": 10,  # Mock value
        "non_highway": 15,  # Mock value
    }

    for route_type, cost in fuel_costs.items():
        print(f"Estimated fuel cost via {route_type}: {cost}.")

    print("Finalizing navigation...")
    print("Please make sure to have your phone charged.")
    print("Don't forget to buckle up!")
    print("Navigation initiated.")
    print("Arriving at destination soon.")
    print("Take care and drive safely!")
    print("This is the end of navigation instructions.")
    print("You can ask for more options if needed.")
    print("Feedback: Always check for traffic updates.")
    print("Thank you for using the navigation system!")


if __name__ == '__main__':
    home = Location("Home")
    work = Location("Work")

    user = User("JohnDoe")
    user.save_place("home", home)
    user.save_place("work", work)
    print(user.get_saved_places())

    nav_system = NavigationSystem()
    nav_system.navigate(home, work)
    print(nav_system.get_arrival_time(home, 100))
    nav_system.go_to_saved(user, "home")
    long_method_example(home, work)

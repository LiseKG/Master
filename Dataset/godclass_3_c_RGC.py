
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
        self.name = name
        self.km = 0

    def get_name(self):
        return self.name

    def set_distance(self, km):
        self.km = km


class User:
    def __init__(self, username):
        self.username = username
        self.saved_places = {}

    def save_place(self, label, location):
        self.saved_places[label] = location

    def get_saved(self, label):
        place = self.saved_places.get(label)
        if place:
            return place.get_name()
        return "No " + label + " address saved"

    def check_addresses(self):
        home = self.get_saved("home")
        work = self.get_saved("work")
        return "Home: " + home + " | Work: " + work


class RouteCalculator:
    def __init__(self, highway_speed, normal_speed):
        self.highway_speed = highway_speed
        self.normal_speed = normal_speed
        self.traffic_multiplier = 1.0

    def apply_traffic(self, multiplier):
        self.traffic_multiplier = multiplier

    def format_time(self, hours):
        total_minutes = int(hours * 60)
        h = total_minutes // 60
        m = total_minutes % 60
        return str(h) + "h " + str(m) + "min"

    def highway_time(self, km):
        hours = (km / self.highway_speed) * self.traffic_multiplier
        return round(hours, 2)

    def normal_time(self, km):
        hours = (km / self.normal_speed) * self.traffic_multiplier
        return round(hours, 2)

    def highway_route_str(self, start, destination, km):
        formatted = self.format_time(self.highway_time(km))
        return ("Route via HIGHWAY: " + start.get_name() + " -> " +
                destination.get_name() + " | Distance: " + str(km) +
                " km | ETA: " + formatted)

    def normal_route_str(self, start, destination, km):
        formatted = self.format_time(self.normal_time(km))
        return ("Route via NORMAL ROADS: " + start.get_name() + " -> " +
                destination.get_name() + " | Distance: " + str(km) +
                " km | ETA: " + formatted)

    def alternatives_str(self, start, destination):
        km = destination.km
        highway = self.highway_route_str(start, destination, km)
        normal = self.normal_route_str(start, destination, km)
        return highway + "\n" + normal

    def arrival_time_str(self, start, destination):
        km = destination.km
        formatted = self.format_time(km / self.normal_speed)
        return ("Arrival time from " + start.get_name() + " to " +
                destination.get_name() + ": " + formatted)


class RouteHistory:
    def __init__(self):
        self.entries = []

    def log(self, start, destination):
        self.entries.append(start.get_name() + " -> " + destination.get_name())

    def summary(self):
        if not self.entries:
            return "No routes navigated yet."
        return "Route history: " + ", ".join(self.entries)


class UserRegistry:
    def __init__(self):
        self.users = {}
        self.current_user = None

    def method1_register_user(self, username):
        user = User(username)
        self.users[username] = user
        return user

    def method2_set_current_user(self, username):
        if username in self.users:
            self.current_user = self.users[username]


class LocationFactory:
    def method3_create_location(self, name):
        return Location(name)

    def method4_set_distance(self, location, km):
        location.set_distance(km)


class NavigationSystem:
    def __init__(self):
        self.calculator = RouteCalculator(highway_speed=100, normal_speed=60)
        self.history = RouteHistory()

    def navigate(self, start, destination):
        self.history.log(start, destination)
        alternatives = self.calculator.alternatives_str(start, destination)
        arrival = self.calculator.arrival_time_str(start, destination)
        return alternatives + "\n" + arrival

    def get_alternatives(self, start, destination):
        return self.calculator.alternatives_str(start, destination)

    def get_arrival_time(self, start, destination):
        return self.calculator.arrival_time_str(start, destination)

    def go_to_saved(self, user, label):
        place = user.saved_places.get(label)
        current = Location("Current Location")
        if place:
            return self.navigate(current, place)
        return "No saved address found for label: " + label


# --- Demo run ---
if __name__ == "__main__":
    registry = UserRegistry()
    factory = LocationFactory()
    nav = NavigationSystem()

    alice = registry.method1_register_user("alice")
    registry.method2_set_current_user("alice")

    home_loc = factory.method3_create_location("Home")
    factory.method4_set_distance(home_loc, 15)

    work_loc = factory.method3_create_location("Work")
    factory.method4_set_distance(work_loc, 40)

    alice.save_place("home", home_loc)
    alice.save_place("work", work_loc)

    print("=== Saved Addresses ===")
    print(alice.check_addresses())

    airport = factory.method3_create_location("Airport")
    factory.method4_set_distance(airport, 80)

    current = factory.method3_create_location("City Center")

    print("\n=== Navigate to Airport ===")
    print(nav.navigate(current, airport))

    print("\n=== Route Alternatives (with traffic) ===")
    nav.calculator.apply_traffic(1.3)
    print(nav.get_alternatives(current, airport))

    print("\n=== Arrival Time ===")
    print(nav.get_arrival_time(current, airport))

    print("\n=== Go to Saved Work ===")
    print(nav.go_to_saved(alice, "work"))

    print("\n=== Go to Saved Home ===")
    print(nav.go_to_saved(alice, "home"))

    print("\n=== Route History ===")
    print(nav.history.summary())

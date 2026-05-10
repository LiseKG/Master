
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


class User:
    def __init__(self, username):
        self.username = username
        self.saved_places = {}

    def save_place(self, label, location):
        self.saved_places[label] = location


class NavigationSystem:
    def __init__(self):
        self.users = {}
        self.current_user = None
        self.route_history = []
        self.highway_speed = 100
        self.normal_speed = 60
        self.traffic_multiplier = 1.0

    def method1_register_user(self, username):
        user = User(username)
        self.users[username] = user
        return user

    def method2_set_current_user(self, username):
        if username in self.users:
            self.current_user = self.users[username]

    def method3_create_location(self, name):
        location = Location(name)
        return location

    def method4_set_distance(self, location, km):
        location.km = km

    def method5_save_home(self, user, location):
        user.save_place("home", location)

    def method6_save_work(self, user, location):
        user.save_place("work", location)

    def method7_get_saved_home(self, user):
        place = user.saved_places.get("home")
        if place:
            return place.get_name()
        return "No home address saved"

    def method8_get_saved_work(self, user):
        place = user.saved_places.get("work")
        if place:
            return place.get_name()
        return "No work address saved"

    def method9_calculate_highway_time(self, km):
        hours = (km / self.highway_speed) * self.traffic_multiplier
        return round(hours, 2)

    def method10_calculate_normal_time(self, km):
        hours = (km / self.normal_speed) * self.traffic_multiplier
        return round(hours, 2)

    def method11_format_time(self, hours):
        total_minutes = int(hours * 60)
        h = total_minutes // 60
        m = total_minutes % 60
        return str(h) + "h " + str(m) + "min"

    def method12_get_highway_route(self, start, destination, km):
        time = self.method9_calculate_highway_time(km)
        formatted = self.method11_format_time(time)
        return ("Route via HIGHWAY: " + start.get_name() + " -> " +
                destination.get_name() + " | Distance: " + str(km) +
                " km | ETA: " + formatted)

    def method13_get_normal_route(self, start, destination, km):
        time = self.method10_calculate_normal_time(km)
        formatted = self.method11_format_time(time)
        return ("Route via NORMAL ROADS: " + start.get_name() + " -> " +
                destination.get_name() + " | Distance: " + str(km) +
                " km | ETA: " + formatted)

    def method14_log_route(self, start, destination):
        entry = start.get_name() + " -> " + destination.get_name()
        self.route_history.append(entry)

    def method15_get_route_history(self):
        if not self.route_history:
            return "No routes navigated yet."
        return "Route history: " + ", ".join(self.route_history)

    def method16_apply_traffic(self, multiplier):
        self.traffic_multiplier = multiplier

    def method17_check_saved_addresses(self, user):
        home = self.method7_get_saved_home(user)
        work = self.method8_get_saved_work(user)
        return "Home: " + home + " | Work: " + work

    def method18_get_arrival_time(self, start, destination):
        km = destination.km
        time_hours = km / self.normal_speed
        formatted = self.method11_format_time(time_hours)
        return ("Arrival time from " + start.get_name() + " to " +
                destination.get_name() + ": " + formatted)

    def method19_get_alternatives(self, start, destination):
        km = destination.km
        highway = self.method12_get_highway_route(start, destination, km)
        normal = self.method13_get_normal_route(start, destination, km)
        return highway + "\n" + normal

    def method20_navigate(self, start, destination):
        km = destination.km
        self.method4_set_distance(destination, km)
        self.method14_log_route(start, destination)
        alternatives = self.method19_get_alternatives(start, destination)
        arrival = self.method18_get_arrival_time(start, destination)
        return alternatives + "\n" + arrival

    def method21_navigate_to_saved(self, user, label, start):
        place = user.saved_places.get(label)
        if place:
            return self.method20_navigate(start, place)
        return "No saved address found for label: " + label

    def navigate(self, start, destination):
        return self.method20_navigate(start, destination)

    def get_alternatives(self, start, destination):
        return self.method19_get_alternatives(start, destination)

    def get_arrival_time(self, start, destination):
        return self.method18_get_arrival_time(start, destination)

    def go_to_saved(self, user, label):
        current = self.method3_create_location("Current Location")
        return self.method21_navigate_to_saved(user, label, current)


# --- Demo run ---
if __name__ == "__main__":
    nav = NavigationSystem()

    alice = nav.method1_register_user("alice")
    nav.method2_set_current_user("alice")

    home_loc = nav.method3_create_location("Home")
    nav.method4_set_distance(home_loc, 15)

    work_loc = nav.method3_create_location("Work")
    nav.method4_set_distance(work_loc, 40)

    nav.method5_save_home(alice, home_loc)
    nav.method6_save_work(alice, work_loc)

    print("=== Saved Addresses ===")
    print(nav.method17_check_saved_addresses(alice))

    airport = nav.method3_create_location("Airport")
    nav.method4_set_distance(airport, 80)

    current = nav.method3_create_location("City Center")

    print("\n=== Navigate to Airport ===")
    print(nav.navigate(current, airport))

    print("\n=== Route Alternatives (with traffic) ===")
    nav.method16_apply_traffic(1.3)
    print(nav.get_alternatives(current, airport))

    print("\n=== Arrival Time ===")
    print(nav.get_arrival_time(current, airport))

    print("\n=== Go to Saved Work ===")
    print(nav.go_to_saved(alice, "work"))

    print("\n=== Go to Saved Home ===")
    print(nav.go_to_saved(alice, "home"))

    print("\n=== Route History ===")
    print(nav.method15_get_route_history())

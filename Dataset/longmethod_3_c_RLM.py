
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

    def get_name(self):
        return self.name


class User:
    def __init__(self, username):
        self.username = username
        self.saved_places = {}

    def save_place(self, label, location):
        self.saved_places[label] = location
        return "Saved " + str(location.get_name()) + " as " + str(label)


class NavigationSystem:
    def __init__(self):
        self.routes = []

    def navigate(self, start, destination):
        return "Navigating from " + str(start.get_name()) + " to " + str(destination.get_name())

    def get_alternatives(self, start, destination):
        highway = "Route 1 (highway): " + str(start.get_name()) + " -> highway -> " + str(destination.get_name())
        no_highway = "Route 2 (no highway): " + str(start.get_name()) + " -> local roads -> " + str(destination.get_name())
        return highway, no_highway

    def get_arrival_time(self, start, destination):
        return "Arrival time calculation requires km parameter"

    def go_to_saved(self, user, label):
        location = user.saved_places.get(label)
        if location:
            return "Going to saved place: " + str(location.get_name())
        return "No saved place found for label: " + str(label)


def extract_location_info(start: Location, destination: Location, user: User):
    start_name = start.get_name()
    print("plan_navigation: start location name: " + str(start_name))
    destination_name = destination.get_name()
    print("plan_navigation: destination location name: " + str(destination_name))
    user_name = user.username
    print("plan_navigation: user name: " + str(user_name))
    return start_name, destination_name, user_name


def run_navigation(nav: NavigationSystem, start: Location, destination: Location, km: int):
    nav_result = nav.navigate(start, destination)
    print("plan_navigation: navigate() returned: " + str(nav_result))
    highway_route, no_highway_route = nav.get_alternatives(start, destination)
    print("plan_navigation: get_alternatives() highway route: " + str(highway_route))
    print("plan_navigation: get_alternatives() no-highway route: " + str(no_highway_route))
    arrival_base = nav.get_arrival_time(start, destination)
    print("plan_navigation: get_arrival_time() returned: " + str(arrival_base))
    arrival_hours = km / 60
    print("plan_navigation: computed arrival time (hours): " + str(arrival_hours))
    arrival_str = "Estimated arrival in " + str(arrival_hours) + " hours"
    print("plan_navigation: arrival time string: " + arrival_str)
    return nav_result


def save_and_check_places(user: User, nav: NavigationSystem, start: Location, destination: Location):
    save_home_result = user.save_place("home", start)
    print("plan_navigation: save_place('home') returned: " + str(save_home_result))
    save_work_result = user.save_place("work", destination)
    print("plan_navigation: save_place('work') returned: " + str(save_work_result))
    home_location = user.saved_places.get("home")
    print("plan_navigation: saved home location: " + str(home_location.get_name()))
    work_location = user.saved_places.get("work")
    print("plan_navigation: saved work location: " + str(work_location.get_name()))
    go_home_result = nav.go_to_saved(user, "home")
    print("plan_navigation: go_to_saved('home') returned: " + str(go_home_result))
    go_work_result = nav.go_to_saved(user, "work")
    print("plan_navigation: go_to_saved('work') returned: " + str(go_work_result))


def log_summary(start_name: str, destination_name: str, km: int, nav_result: str):
    km_str = str(km)
    print("plan_navigation: km as string: " + km_str)
    route_count = 2
    print("plan_navigation: number of alternative routes: " + str(route_count))
    navigation_complete = True
    print("plan_navigation: navigation_complete flag: " + str(navigation_complete))
    summary = "Trip from " + start_name + " to " + destination_name + " is " + km_str + " km"
    print("plan_navigation: trip summary: " + summary)
    print("plan_navigation: final result: " + nav_result)


def plan_navigation(user: User, nav: NavigationSystem, start: Location, destination: Location, km: int) -> str:
    print("plan_navigation: starting execution")
    print("plan_navigation: received user parameter")
    print("plan_navigation: received nav parameter")
    print("plan_navigation: received start parameter")
    print("plan_navigation: received destination parameter")
    print("plan_navigation: received km parameter: " + str(km))
    start_name, destination_name, _ = extract_location_info(start, destination, user)
    nav_result = run_navigation(nav, start, destination, km)
    save_and_check_places(user, nav, start, destination)
    log_summary(start_name, destination_name, km, nav_result)
    print("plan_navigation: execution complete, returning result")
    return nav_result


if __name__ == "__main__":
    start = Location("Home Base")
    destination = Location("Office")
    user = User("Alice")
    nav = NavigationSystem()
    start.get_name()
    destination.get_name()
    user.save_place("home", start)
    user.save_place("work", destination)
    nav.navigate(start, destination)
    nav.get_alternatives(start, destination)
    nav.get_arrival_time(start, destination)
    nav.go_to_saved(user, "home")
    result = plan_navigation(user, nav, start, destination, 120)
    print("main: result = " + result)




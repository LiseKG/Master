
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
    def __init__(self, name, km=0):
        self.name = name
        self.km = km

    def get_name(self):
        return self.name


class User:
    def __init__(self, username):
        self.username = username
        self.saved_places = {}

    def save_place(self, label, location):
        self.saved_places[label] = location

    def get_saved_place(self, label):
        return self.saved_places.get(label, None)

    def show_saved_places(self):
        if not self.saved_places:
            print(f"{self.username} has no saved places.")
        else:
            for label, loc in self.saved_places.items():
                print(f"  {label}: {loc.get_name()} ({loc.km} km away)")


class NavigationSystem:
    def __init__(self):
        self.routes = []

    def navigate(self, start, destination):
        print(f"\nNavigating from {start.get_name()} to {destination.get_name()} ({destination.km} km)")
        self.get_alternatives(start, destination)
        self.get_arrival_time(start, destination)

    def get_alternatives(self, start, destination):
        print(f"  Route 1 (with highway): Take the highway from {start.get_name()} directly to {destination.get_name()}.")
        print(f"  Route 2 (without highway): Take local roads from {start.get_name()} to {destination.get_name()}.")

    def get_arrival_time(self, start, destination):
        hours = destination.km / 60
        print(f"  Estimated arrival time: {hours:.2f} hours")

    def go_to_saved(self, user, label):
        location = user.get_saved_place(label)
        if location is None:
            print(f"No saved place found for label '{label}'.")
        else:
            start = Location("Current Location", 0)
            self.navigate(start, location)

    def plan_outbound(self, start, destination):
        self.routes = []
        self.routes.append(destination.get_name())
        self.get_alternatives(start, destination)
        self.get_arrival_time(start, destination)
        self.routes.append("via highway")
        self.routes.append("via local roads")

    def plan_return(self, start, destination):
        self.get_alternatives(destination, start)
        self.get_arrival_time(destination, start)
        self.routes.append("return trip planned")

    def plan_saved_stops(self, user):
        print(f"Total legs in self.routes: {len(self.routes)}")
        self.go_to_saved(user, "home")
        self.go_to_saved(user, "work")
        self.routes.append("trip complete")
        print(f"Final routes: {self.routes}")

    def plan_full_trip(self, user, destination):
        start = Location("Home Base", 0)
        self.plan_outbound(start, destination)
        self.plan_return(start, destination)
        self.plan_saved_stops(user)


def plan_full_trip(nav, user, destination):
    nav.plan_full_trip(user, destination)


if __name__ == "__main__":
    nav = NavigationSystem()
    user = User("Alice")

    home = Location("Home", 5)
    work = Location("Work", 20)
    user.save_place("home", home)
    user.save_place("work", work)

    print("=== Saved Places ===")
    user.show_saved_places()

    destination = Location("Airport", 45)
    nav.navigate(Location("City Center", 0), destination)

    print("\n=== Go to saved 'work' ===")
    nav.go_to_saved(user, "work")

    print("\n=== Full Trip Plan ===")
    plan_full_trip(nav, user, destination)

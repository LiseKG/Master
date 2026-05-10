class Location:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class User:
    def __init__(self, username):
        self.username = username
        self.saved_locations = {}

    def save_place(self, label, location):
        self.saved_locations[label] = location

    def get_saved_places(self):
        return self.saved_locations

    def get_home(self):
        return self.saved_locations.get("home", "Not set")

    def get_work(self):
        return self.saved_locations.get("work", "Not set")


class NavigationSystem:
    def __init__(self):
        self.users = {}
        # Storing routes in a dictionary for efficient access
        self.routes = {
            "highway": "A1 highway",
            "non-highway": "B2 non-highway"
        }
        self.default_distance = 100  # Default distance for calculations

    def navigate(self, start, destination):
        return f'Navigating from {start.get_name()} to {destination.get_name()}'

    def get_alternatives(self, start, destination):
        # No need to instantiate location object for alternatives
        return list(self.routes.values())

    def get_arrival_time(self, start, destination):
        # Use pre-defined distance to calculate arrival time
        return self.default_distance / 60  # Assuming speed is 60 km/h

    def go_to_saved(self, username, label):
       if username in self.users:
            location = self.users[username].get_saved_places().get(label)
            if location:
                self.navigate(Location("Current Location"), location)




def calculate_trip_info(user, nav_system, destination_name, km_to_destination):
    destination = Location(destination_name)

    # Fetching alternatives without creating unnecessary Location instances
    route_highway, route_non_highway = nav_system.get_alternatives(None, None)
    arrival_time = nav_system.get_arrival_time(None, destination)

    # Directly access home and work for clarity
    saved_home = user.get_home()
    saved_work = user.get_work()

    destination_info = (
        f'Destination: {destination.get_name()}\n'
        f'Routes: {route_highway}, {route_non_highway}\n'
        f'Estimated Arrival Time: {arrival_time:.2f} hours\n'
        f"Home: {saved_home}\n"
        f"Work: {saved_work}\n"
        f"User saved places: {user.get_saved_places()}\n"
        f"User username: {user.username}\n"
        f"Destination name length: {destination.get_name()}\n"
        f"Total saved locations: {user.saved_locations}\n"
    )

    # Using a generator expression to avoid repeated calls to get_name() 
    additional_info = "\n".join(f"Label: {label}, Location: {location.get_name()}"
                                 for label, location in user.saved_locations.items())
    
    if additional_info:  # Only append if there are saved locations
        destination_info += additional_info

    return destination_info


if __name__ == '__main__':
    calculate_trip_info(User("Test"),NavigationSystem(),Location("Test"),50)
    loc = Location("name")
    loc.get_name()
    user = User("name")
    print(user.save_place("home","A"))
    nav = NavigationSystem()
    print(nav.navigate(loc,loc))
    print(nav.get_alternatives("A","B"))
    print(nav.get_arrival_time(100,loc))
    print(nav.go_to_saved(user,loc))
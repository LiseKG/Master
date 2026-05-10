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

    def get_saved_place(self, label):
        return self.saved_locations.get(label, "Not set")


class NavigationSystem:
    def __init__(self):
        self.routes = {
            "highway": "A1 highway",
            "non-highway": "B2 non-highway"
        }

    def navigate(self, start, destination):
        return f'Navigating from {start.get_name()} to {destination.get_name()}'

    def get_alternatives(self,A,B):
        return list(self.routes.values())

    def get_arrival_time(self, destination,start):
        km_to_destination = destination
        return km_to_destination / 60  # Assuming speed is 60 km/h

    def go_to_saved(self, user, label):
        location = user.get_saved_place(label)
        if location != "Not set":
            return f'Going to {location.get_name()}'
        return "Address not found"


def calculate_trip_info(user, nav_system, destination_name, km_to_destination):
    destination = Location(destination_name)
    
    routes = nav_system.get_alternatives("A","B")

    arrival_time = nav_system.get_arrival_time(km_to_destination,"A")

    saved_home = user.get_saved_place("home")
    saved_work = user.get_saved_place("work")

    destination_info = (
        f'Destination: {destination.get_name()}\n'
        f'Routes: {routes[0]}, {routes[1]}\n'
        f'Estimated Arrival Time: {arrival_time:.2f} hours\n'
        f"Home: {saved_home}\n"
        f"Work: {saved_work}\n"
        f"User saved places: {user.get_saved_places()}\n"
        f"User username: {user.username}\n"
        f"Destination name length: {destination.get_name()}\n"
        f"Total saved locations: {user.get_saved_places()}\n"
    )
    
    for label, loc in user.get_saved_places().items():
        destination_info += f"Label: {label}, Location: {loc.get_name()}\n"

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
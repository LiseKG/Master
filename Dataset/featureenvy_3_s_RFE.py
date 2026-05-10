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


class NavigationSystem:
    def __init__(self):
        self.users = {}
        self.routes = {
            "highway": "A1 Highway",
            "non-highway": "B2 non-highway"
        }

    def navigate(self, start, destination):
        return f'Navigating from {start.get_name()} to {destination.get_name()}'

    def get_alternatives(self, start, destination):
        return [self.routes['highway'], self.routes['non-highway']]

    def get_arrival_time(self, start, destination):
        distance = 100  # just a placeholder for distance calculation
        return distance / 60  # Assuming speed is 60 km/h

    def go_to_saved(self, username, label):
        if username in self.users:
            location = self.users[username].get_saved_places().get(label)
            if location:
                self.navigate(Location("Current Location"), location)


def calculate_trip_info(user, nav_system, destination_name, km_to_destination):
    destination = Location(destination_name)

    route_highway, route_non_highway = nav_system.get_alternatives(Location("Current Position"), destination)

    arrival_time = nav_system.get_arrival_time(Location("Current Position"), destination)

    destination_info = (
        f'Destination: {destination.get_name()}\n'
        f'Routes: {route_highway}, {route_non_highway}\n'
        f'Estimated Arrival Time: {arrival_time:.2f} hours\n'
        f"Home: {user.saved_locations.get('home', 'Not set')}\n"
        f"Work: {user.saved_locations.get('work', 'Not set')}\n"
        f"User saved places: {user.get_saved_places()}\n"
        f"User username: {user.username}\n"
        f"Destination name length: {destination.get_name()}\n"
    )

    for label, location in user.get_saved_places().items():
        destination_info += f"Label: {label}, Location: {location.get_name()}\n"

    destination_info += f"Total saved locations: {len(user.get_saved_places())}\n"

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
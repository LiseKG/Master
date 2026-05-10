
# File featureenvy smelly version: featureenvy_3_s.py

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
        self.routes = {
            "highway": "A1 highway",
            "non-highway": "B2 non-highway"
        }

    def navigate(self, start, destination):
        return f'Navigating from {start.get_name()} to {destination.get_name()}'

    def get_alternatives(self, start, destination):
        return [self.routes['highway'], self.routes['non-highway']]

    def get_arrival_time(self, start, destination):
        distance = 100  # just a placeholder for distance calculation
        return distance / 60  # Assuming speed is 60 km/h

    def go_to_saved(self, user, label):
        if label in user.saved_locations:
            return f'Going to {user.saved_locations[label].get_name()}'
        return "Address not found"


def calculate_trip_info(user, nav_system, destination_name, km_to_destination):
    destination = Location(destination_name)
    
    route_highway = nav_system.get_alternatives(Location("Current Position"), destination)[0]
    route_non_highway = nav_system.get_alternatives(Location("Current Position"), destination)[1]

    arrival_time = nav_system.get_arrival_time(Location("Current Position"), destination)

    saved_home = user.get_saved_places()
    saved_work = user.get_saved_places()
    
    destination_info = f'Destination: {destination.get_name()}\n'
    destination_info += f'Routes: {route_highway}, {route_non_highway}\n'
    destination_info += f'Estimated Arrival Time: {arrival_time:.2f} hours\n'
    
    # Excessive feature envy: using user's method and attributes excessively
    destination_info += f"Home: {saved_home}\n"
    destination_info += f"Work: {saved_work}\n"
    destination_info += f"User saved places: {user.get_saved_places()}\n"
    destination_info += f"User username: {user.username}\n"
    destination_info += f"Destination name length: {(destination.get_name())}\n"
    
    # Accessing User attributes multiple times
    for label in user.get_saved_places():
        destination_info += f"Label: {label}, Location: {user.saved_places[label].get_name()}\n"
        
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
   
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
        self.users = {}

    def add_user(self, user):
        self.users[user.username] = user

    def navigate(self, username, destination_name):
        user = self.users.get(username)
        if user:
            arrival_time = self.get_arrival_time(0, destination_name)
            alternatives = self.get_alternatives(0, destination_name)
            return arrival_time, alternatives
        return None, None

    def get_alternatives(self, start, destination_name):
        # Create two alternatives with highway and scenic route
        return [
            f"Route with highway to {destination_name}.",
            f"Scenic route to {destination_name}."
        ]

    def get_arrival_time(self, start, destination_name):
        distance = self.calculate_distance(start, destination_name)
        time = distance / 60  # Assuming speed of 60 km/h
        return f"Estimated arrival time: {time} hours."

    def go_to_saved(self, username, label):
        user = self.users.get(username)
        if user and label in user.get_saved_places():
            destination_name = user.get_saved_places()[label].get_name()
            return self.navigate(username, destination_name)
        return None

    def get_user_saved_places(self, username):
        user = self.users.get(username)
        return user.get_saved_places() if user else {}

    def calculate_distance(self, start, destination_name):
        return 120  # Assume a sample distance of 120 km

    def clear_saved_places(self, username):
        user = self.users.get(username)
        if user:
            user.saved_places.clear()

    def list_users(self):
        return list(self.users.keys())

    def user_count(self):
        return len(self.users)

    def user_exists(self, username):
        return username in self.users

    def remove_user(self, username):
        self.users.pop(username, None)

    def update_location_name(self, username, label, new_name):
        user = self.users.get(username)
        if user and label in user.saved_places:
            user.saved_places[label].name = new_name

    def get_user_info(self, username):
        user = self.users.get(username)
        return (user.username, user.get_saved_places()) if user else (None, None)

    def get_distance_to_saved(self, username, label):
        user = self.users.get(username)
        if user and label in user.get_saved_places():
            return self.calculate_distance(0, user.get_saved_places()[label].get_name())
        return None


class RouteManager:
    def __init__(self, navigation_system):
        self.navigation_system = navigation_system

    def get_route_options(self, username, destination_name):
        return self.navigation_system.get_alternatives(0, destination_name)

    def road_type(self, route_choice):
        return "Highway Route" if route_choice == 1 else "Scenic Route"

    def trip_summary(self, username, destination_name):
        arrival_time, alternatives = self.navigation_system.navigate(username, destination_name)
        return {
            "arrival_time": arrival_time,
            "alternatives": alternatives
        }

    def track_trip(self, username, destination_name):
        user = self.navigation_system.users.get(username)
        if user:
            summary = self.trip_summary(username, destination_name)
            return f"Trip Summary for {user.username}: {summary}"
        return None

    def has_saved_places(self, username):
        user = self.navigation_system.users.get(username)
        return bool(user.saved_places) if user else False

    def get_user_summary(self, username):
        user_info = self.navigation_system.get_user_info(username)
        return f"User {user_info[0]} has saved places: {user_info[1]}"

    def choose_route(self, username, label):
        user = self.navigation_system.users.get(username)
        if user:
            return self.navigation_system.get_alternatives(0, label)



if __name__ == "__main__":
    # Create system
    nav = NavigationSystem()
    route_manager = RouteManager(nav)

    # Create users
    user1 = User("alice")
    user2 = User("bob")

    # Add users
    nav.add_user(user1)
    nav.add_user(user2)

    # Create locations
    home = Location("Home")
    work = Location("Work")

    # Test Location and User methods
    home.get_name()
    user1.save_place("home", home)
    user1.save_place("work", work)
    print(user1.get_saved_places())

    # Navigation features (these internally test other methods)
    print(nav.navigate("alice", "City Center"))
    print(nav.go_to_saved("alice", "home"))
    route_manager.choose_route("alice", "home")
    route_manager.get_route_options("alice", "Mall")
    route_manager.track_trip("alice", "Airport")

    # User information features
    print(nav.get_user_saved_places("alice"))
    route_manager.get_user_summary("alice")
    nav.get_distance_to_saved("alice", "home")

    # Route type logic
    route_manager.road_type(1)
    route_manager.road_type(2)

    # User management features
    print(nav.list_users())
    print(nav.user_count())
    print(nav.user_exists("alice"))
    print(route_manager.has_saved_places("alice"))

    # Update location
    nav.update_location_name("alice", "home", "New Home")

    # Clear saved places
    nav.clear_saved_places("alice")
    print(route_manager.has_saved_places("alice"))

    # Remove user
    nav.remove_user("bob")
    print(nav.list_users())
    print(nav.user_count())

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
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def navigate(self, username, destination_name):
        user = self.find_user(username)
        if user:
            destination = Location(destination_name)
            arrival_time = self.get_arrival_time(0, destination_name)
            alternatives = self.get_alternatives(0, destination_name)
            return arrival_time, alternatives
        return None, None

    def get_alternatives(self, start, destination_name):
        return [
            f"Route with highway to {destination_name}.",
            f"Scenic route to {destination_name}."
        ]

    def get_arrival_time(self, start, destination_name):
        distance = self.calculate_distance(start, destination_name)
        time = distance / 60  # Assuming speed of 60 km/h
        return f"Estimated arrival time: {time} hours."

    def go_to_saved(self, username, label):
        user = self.find_user(username)
        if user and label in user.get_saved_places():
            destination_name = user.get_saved_places()[label].get_name()
            return self.navigate(username, destination_name)
        return None

    def find_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

    def get_user_saved_places(self, username):
        user = self.find_user(username)
        if user:
            return user.get_saved_places()
        return {}

    def calculate_distance(self, start, destination_name):
        # Simple mock distances for illustration
        return 120  # Assume a sample distance of 120 km

    def clear_saved_places(self, username):
        user = self.find_user(username)
        if user:
            user.saved_places.clear()

    def list_users(self):
        return [user.username for user in self.users]

    def user_count(self):
        return len(self.users)

    def user_exists(self, username):
        return self.find_user(username) is not None

    def remove_user(self, username):
        self.users = [user for user in self.users if user.username != username]

    def update_location_name(self, username, label, new_name):
        user = self.find_user(username)
        if user and label in user.saved_places:
            location = user.saved_places[label]
            location.name = new_name

    def get_user_info(self, username):
        user = self.find_user(username)
        if user:
            return user.username, user.get_saved_places()
        return None, None

    def get_distance_to_saved(self, username, label):
        user = self.find_user(username)
        if user and label in user.get_saved_places():
            destination_name = user.get_saved_places()[label].get_name()
            return self.calculate_distance(0, destination_name)
        return None

    def road_type(self, route_choice):
        if route_choice == 1:
            return "Highway Route"
        else:
            return "Scenic Route"

    def choose_route(self, username, label):
        user = self.find_user(username)
        if user:
            return self.get_alternatives(0, label)

    def trip_summary(self, username, destination_name):
        arrival_time, alternatives = self.navigate(username, destination_name)
        return {
            "arrival_time": arrival_time,
            "alternatives": alternatives
        }

    def track_trip(self, username, destination_name):
        user = self.find_user(username)
        if user:
            summary = self.trip_summary(username, destination_name)
            return f"Trip Summary for {user.username}: {summary}"
        return None

    def has_saved_places(self, username):
        user = self.find_user(username)
        return bool(user.get_saved_places())

    def get_user_summary(self, username):
        user_info = self.get_user_info(username)
        return f"User {user_info[0]} has saved places: {user_info[1]}"

    def get_route_options(self, username, destination_name):
        return self.get_alternatives(0, destination_name)

if __name__ == "__main__":
    # Create system
    nav = NavigationSystem()

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
    user1.save_place("home", home)
    user1.save_place("work", work)
    print(user1.get_saved_places())

    # Navigation features (these internally test other methods)
    print(nav.navigate("alice", "City Center"))
    print(nav.go_to_saved("alice", "home"))
    nav.choose_route("alice", "home")
    nav.get_route_options("alice", "Mall")
    nav.track_trip("alice", "Airport")

    # User information features
    print(nav.get_user_saved_places("alice"))
    nav.get_user_summary("alice")
    nav.get_distance_to_saved("alice", "home")

    # Route type logic
    nav.road_type(1)
    nav.road_type(2)

    # User management features
    print(nav.list_users())
    print(nav.user_count())
    print(nav.user_exists("alice"))
    print(nav.has_saved_places("alice"))

    # Update location
    nav.update_location_name("alice", "home", "New Home")

    # Clear saved places
    nav.clear_saved_places("alice")
    print(nav.has_saved_places("alice"))

    # Remove user
    nav.remove_user("bob")
    print(nav.list_users())
    print(nav.user_count())

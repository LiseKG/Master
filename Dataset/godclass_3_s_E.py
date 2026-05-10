
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
        self.users[user.username] = user  # Use dictionary for faster access

    def navigate(self, username, destination_name):
        user = self.find_user(username)
        if user:
            arrival_time = self.get_arrival_time(0, destination_name)
            alternatives = self.get_alternatives(destination_name)
            return arrival_time, alternatives
        return None, None

    def get_alternatives(self, destination_name):
        return [
            f"Route with highway to {destination_name}.",
            f"Scenic route to {destination_name}."
        ]

    def get_arrival_time(self, start, destination_name):
        distance = self.calculate_distance(start, destination_name)
        time = distance / 60  # Assuming speed of 60 km/h
        return f"Estimated arrival time: {time:.2f} hours."  # Formatting for better readability

    def go_to_saved(self, username, label):
        user = self.find_user(username)
        if user and label in user.get_saved_places():
            destination_name = user.get_saved_places()[label].get_name()
            return self.navigate(username, destination_name)
        return None

    def find_user(self, username):
        return self.users.get(username)  # Use dictionary to simplify user lookup

    def get_user_saved_places(self, username):
        user = self.find_user(username)
        return user.get_saved_places() if user else {}

    def calculate_distance(self, start, destination_name):
        return 120  # Assume a sample fixed distance for illustration

    def clear_saved_places(self, username):
        user = self.find_user(username)
        if user:
            user.saved_places.clear()

    def list_users(self):
        return list(self.users.keys())  # Return list of usernames

    def user_count(self):
        return len(self.users)

    def user_exists(self, username):
        return username in self.users

    def remove_user(self, username):
        if username in self.users:
            del self.users[username]  # Remove user directly from dictionary

    def update_location_name(self, username, label, new_name):
        user = self.find_user(username)
        if user and label in user.saved_places:
            user.saved_places[label].name = new_name

    def get_user_info(self, username):
        user = self.find_user(username)
        return (user.username, user.get_saved_places()) if user else (None, None)

    def get_distance_to_saved(self, username, label):
        user = self.find_user(username)
        if user and label in user.get_saved_places():
            return self.calculate_distance(0, user.get_saved_places()[label].get_name())
        return None

    def road_type(self, route_choice):
        return "Highway Route" if route_choice == 1 else "Scenic Route"

    def choose_route(self, username, label):
        user = self.find_user(username)
        if user:
            return self.get_alternatives(label)

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
        return bool(user.get_saved_places()) if user else False

    def get_user_summary(self, username):
        user_info = self.get_user_info(username)
        return f"User {user_info[0]} has saved places: {user_info[1]}"

    def get_route_options(self, username, destination_name):
        return self.get_alternatives(destination_name)



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

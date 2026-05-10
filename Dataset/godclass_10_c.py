# Rental Movie Streaming Platform - God Class Design

# Requirements:
# - Alice should get a list of available movies
# - Should be able to add 3 movies and check that all movies are saved.
# - Alice should be able to rent "Barbie".
# - Alice should get information about playtime, movie age restrictions. (PG-13, 1hour and 54 min)
# - Alice should be able to give a list over all rented movies
# - Return a list over all returned movies


class User:
    def __init__(self, username):
        self.username = username
        self.rented = []
        self.returned = []
        self.wishlist = []


class MovieStreamingPlatform:
    def __init__(self, user_name):
        self.username = user_name
        self.moviesrented = []
        self.movies = []
        self.catalog = []
        self.rental_records = []
        self.event_log = []
        self.active_user = None

    # Method 1
    def register_user(self, user: User):
        self.active_user = user
        print(f"User '{user.username}' registered.")

    # Method 2
    def log_event(self, message):
        self.event_log.append(message)

    # Method 3
    def add_movies(self, title, playtime, age):
        movie = {"title": title, "playtime": playtime, "age": age, "available": True}
        self.catalog.append(movie)
        self.movies.append(movie)
        print(f"Movie '{title}' added (playtime: {playtime}, age: {age}).")
        return movie

    # Method 4
    def find_movie(self, movie_name):
        for movie in self.catalog:
            if movie["title"].lower() == movie_name.lower():
                return movie
        return None

    # Method 5
    def list_movies(self):
        available = [m["title"] for m in self.catalog if m["available"]]
        print(f"Available movies: {available}")
        return available

    # Method 6
    def rent_movie(self, movie_name):
        movie = self.find_movie(movie_name)
        if movie is None:
            print(f"'{movie_name}' not found.")
            return f"'{movie_name}' not found."
        if not movie["available"]:
            print(f"'{movie_name}' is not available.")
            return f"'{movie_name}' not available."
        movie["available"] = False
        self.rental_records.append({"username": self.username, "title": movie_name, "status": "rented"})
        self.moviesrented.append({"title": movie_name, "status": "rented"})
        if self.active_user is not None:
            self.active_user.rented.append(movie_name)
        self.log_event(f"'{movie_name}' rented by '{self.username}'.")
        print(f"{movie_name} rented")
        return f"{movie_name} rented"

    # Method 7
    def return_movie(self, movie_name):
        movie = self.find_movie(movie_name)
        if movie is not None:
            movie["available"] = True
        for record in self.rental_records:
            if record["title"] == movie_name and record["status"] == "rented":
                record["status"] = "returned"
        for entry in self.moviesrented:
            if entry["title"] == movie_name:
                entry["status"] = "returned"
        if self.active_user is not None and movie_name in self.active_user.rented:
            self.active_user.rented.remove(movie_name)
            self.active_user.returned.append(movie_name)
        self.log_event(f"'{movie_name}' returned by '{self.username}'.")
        print(f"'{movie_name}' returned.")
        return f"'{movie_name}' returned."

    # Method 8
    def get_movie_info(self, movie_name):
        movie = self.find_movie(movie_name)
        if movie is None:
            print(f"'{movie_name}' not found.")
            return f"'{movie_name}' not found."
        info = f"{movie['title']} | Playtime: {movie['playtime']} | Age restriction: {movie['age']}"
        print(info)
        return info

    # Method 9
    def get_rented_movies(self):
        rented = [e["title"] for e in self.moviesrented if e["status"] == "rented"]
        print(f"Currently rented: {rented}")
        return rented

    # Method 10
    def get_returned_movies(self):
        returned = [e["title"] for e in self.moviesrented if e["status"] == "returned"]
        print(f"Returned movies: {returned}")
        return returned

    # Method 11
    def show_user_status(self):
        rented = self.get_rented_movies()
        returned = self.get_returned_movies()
        print(f"User: {self.username} | Rented: {rented} | Returned: {returned}")

    # Method 12
    def check_all_movies_saved(self):
        titles = [m["title"] for m in self.catalog]
        print(f"All saved movies ({len(titles)}): {titles}")
        return titles

    # Method 13
    def add_to_wishlist(self, user: User, movie_name):
        if movie_name not in user.wishlist:
            user.wishlist.append(movie_name)
            self.log_event(f"'{movie_name}' added to {user.username}'s wishlist.")
            print(f"'{movie_name}' added to wishlist.")

    # Method 14
    def show_wishlist(self, user: User):
        print(f"{user.username}'s wishlist: {user.wishlist}")
        return user.wishlist

    # Method 15
    def check_availability(self, movie_name):
        movie = self.find_movie(movie_name)
        if movie is None:
            print(f"'{movie_name}' not in catalog.")
            return False
        status = "available" if movie["available"] else "not available"
        print(f"'{movie_name}' is {status}.")
        return movie["available"]

    # Method 16
    def show_rental_history(self):
        print("Rental history:")
        for record in self.rental_records:
            print(f"  {record['username']} | {record['title']} | {record['status']}")
        return self.rental_records

    # Method 17
    def get_movies_by_age(self, age_restriction):
        matches = [m["title"] for m in self.catalog if m["age"] == age_restriction]
        print(f"Movies with age restriction '{age_restriction}': {matches}")
        return matches

    # Method 18
    def show_event_log(self):
        print("Event log:")
        for entry in self.event_log:
            print(f"  {entry}")

    # Method 19
    def count_available_movies(self):
        count = sum(1 for m in self.catalog if m["available"])
        print(f"Available movies count: {count}")
        return count

    # Method 20
    def clear_wishlist(self, user: User):
        user.wishlist = []
        self.log_event(f"{user.username}'s wishlist cleared.")
        print(f"{user.username}'s wishlist cleared.")

    # Method 21
    def show_platform_summary(self):
        total = len(self.catalog)
        available = self.count_available_movies()
        print(f"Platform '{self.username}': {total} total movie(s), {available} available.")

    # Method 22
    def get_user_rental_count(self, user: User):
        count = len(user.rented)
        print(f"{user.username} currently has {count} rented movie(s).")
        return count


if __name__ == "__main__":
    platform = MovieStreamingPlatform("StreamZone")

    alice = User("Alice")

    # Method 1 - register_user
    platform.register_user(alice)

    # Method 3 - add_movies
    platform.add_movies("Barbie", "1h 54min", "PG-13")
    platform.add_movies("Oppenheimer", "3h 0min", "R")
    platform.add_movies("Inside Out 2", "1h 40min", "PG")

    # Method 12 - check_all_movies_saved (standalone)
    platform.check_all_movies_saved()

    # Method 5 - list_movies (standalone)
    platform.list_movies()

    # Method 8 - get_movie_info (calls find_movie)
    platform.get_movie_info("Barbie")

    # Method 15 - check_availability (calls find_movie)
    platform.check_availability("Barbie")

    # Method 6 - rent_movie (calls find_movie, log_event)
    platform.rent_movie("Barbie")
    platform.rent_movie("Oppenheimer")

    # Method 9 - get_rented_movies (standalone)
    platform.get_rented_movies()

    # Method 11 - show_user_status (calls get_rented_movies, get_returned_movies)
    platform.show_user_status()

    # Method 7 - return_movie (calls find_movie, log_event)
    platform.return_movie("Barbie")

    # Method 10 - get_returned_movies (standalone)
    platform.get_returned_movies()

    # Method 13 - add_to_wishlist (calls log_event)
    platform.add_to_wishlist(alice, "Inside Out 2")

    # Method 14 - show_wishlist (standalone)
    platform.show_wishlist(alice)

    # Method 16 - show_rental_history (standalone)
    platform.show_rental_history()

    # Method 17 - get_movies_by_age (standalone)
    platform.get_movies_by_age("PG-13")

    # Method 19 - count_available_movies (standalone)
    platform.count_available_movies()

    # Method 21 - show_platform_summary (calls count_available_movies)
    platform.show_platform_summary()

    # Method 22 - get_user_rental_count (standalone)
    platform.get_user_rental_count(alice)

    # Method 20 - clear_wishlist (calls log_event)
    platform.clear_wishlist(alice)

    # Method 18 - show_event_log (standalone)
    platform.show_event_log()

    # Method 2 - log_event (standalone, called directly)
    platform.log_event("Session ended.")

    # Method 4 - find_movie (standalone, called directly)
    found = platform.find_movie("Inside Out 2")
    print(f"Found: {found['title'] if found else 'None'}")




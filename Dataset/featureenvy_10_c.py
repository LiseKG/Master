
# Rental Movie Streaming Platform - Single-Class God Design

# Requirements:
# - Alice should get a list of available movies
# - Should be able to add 3 movies and check that all movies are saved.
# - Alice should be able to rent "Barbie".
# - Alice should get information about playtime, movie age restrictions. (PG-13 , 1hour and 54 min)
# - Alice should be able to give a list over all rented movies
# - Return a list over all returned movies


class MovieStreamingPlatform:
    def __init__(self, user_name):
        self.username = user_name
        self.moviesrented = []
        self.movies = []
        self.returned = []
        self.actions = []

    def list_movies(self):
        return [m["title"] for m in self.movies]

    def rent_movie(self, movie_name):
        for m in self.movies:
            if m["title"] == movie_name:
                self.moviesrented.append({"title": movie_name, "status": "rented"})
                return f"{movie_name} rented"
        return f"{movie_name} not found"

    def get_movie_info(self, movie_name):
        for m in self.movies:
            if m["title"] == movie_name:
                return f"{m['title']} | Playtime: {m['playtime']} | Age: {m['age']}"
        return "Not found"

    def get_rented_movies(self):
        return [m["title"] for m in self.moviesrented if m["status"] == "rented"]

    def show_user_status(self):
        print(f"User: {self.username} | Rented: {len(self.moviesrented)} | Returned: {len(self.returned)}")

    def add_movies(self, title, playtime, age):
        self.movies.append({"title": title, "playtime": playtime, "age": age})


def run_rental_session(platform, movie_name):
    platform.actions = []
    platform.actions.append("session started")
    print(platform.list_movies())
    platform.actions.append(platform.rent_movie(movie_name))
    print(platform.get_movie_info(movie_name))
    platform.actions.append(platform.get_movie_info(movie_name))
    print(platform.get_rented_movies())
    platform.actions.append(str(platform.get_rented_movies()))
    platform.show_user_status()
    platform.returned.append(movie_name)
    platform.actions.append("returned " + movie_name)
    platform.show_user_status()
    print(f"Total actions: {len(platform.actions)}")
    print(f"Actions log: {platform.actions}")


if __name__ == "__main__":
    platform = MovieStreamingPlatform("Alice")

    platform.add_movies("Barbie", "1h 54min", "PG-13")
    platform.add_movies("Inception", "2h 28min", "PG-13")
    platform.add_movies("Interstellar", "2h 49min", "PG")

    print(platform.list_movies())
    print(len(platform.movies) == 3)
    print(platform.rent_movie("Barbie"))
    print(platform.get_movie_info("Barbie"))
    print(platform.get_rented_movies())
    platform.show_user_status()

    run_rental_session(platform, "Inception")





# Rental Movie Streaming Platform - Single-Class God Design

# Requirements:
# - Alice should get a list of available movies
# - Should be able to add 3 movies and check that all movies are saved.
# - Alice should be able to rent "Barbie".
# - Alice should get information about playtime, movie age restrictions. (PG-13 , 1hour and 54 min)
# - Alice should be able to give a list over all rented movies
# - Return a list over all returned movies


def run_rental_session(platform, user_name, movie1, movie2, movie3):
    platform.add_movies(movie1, "1h 54min", "PG-13")
    platform.add_movies(movie2, "2h 10min", "R")
    platform.add_movies(movie3, "1h 30min", "PG")
    available = platform.list_movies()
    result = []
    result.append(available)
    info1 = platform.get_movie_info(movie1)
    result.append(info1)
    info2 = platform.get_movie_info(movie2)
    result.append(info2)
    info3 = platform.get_movie_info(movie3)
    result.append(info3)
    rent1 = platform.rent_movie(movie1)
    result.append(rent1)
    rent2 = platform.rent_movie(movie2)
    result.append(rent2)
    rent3 = platform.rent_movie(movie3)
    result.append(rent3)
    rented = platform.get_rented_movies()
    result.append(rented)
    status = platform.show_user_status()
    result.append(status)
    check1 = platform.get_movie_info(movie1)
    result.append(check1)
    check2 = platform.get_movie_info(movie2)
    result.append(check2)
    check3 = platform.get_movie_info(movie3)
    result.append(check3)
    available2 = platform.list_movies()
    result.append(available2)
    rented2 = platform.get_rented_movies()
    result.append(rented2)
    status2 = platform.show_user_status()
    result.append(status2)
    summary = ""
    summary = summary + str(rent1)
    summary = summary + " "
    summary = summary + str(rent2)
    summary = summary + " "
    summary = summary + str(rent3)
    result.append(summary)
    result.append(user_name)
    return result


class MovieStreamingPlatform:
    def __init__(self, user_name):
        self.username = user_name
        self.moviesrented = []
        self.movies = [{}]

    # Movie Browsing & Rental
    def list_movies(self):
        titles = []
        for movie in self.movies:
            if "title" in movie:
                titles.append(movie["title"])
        return titles

    def rent_movie(self, movie_name):
        self.moviesrented.append(movie_name)
        return movie_name + " rented"

    # Movie Information
    def get_movie_info(self, movie_name):
        for movie in self.movies:
            if "title" in movie and movie["title"] == movie_name:
                return movie_name + " | " + movie["playtime"] + " | " + movie["age"]
        return movie_name + " not found"

    def get_rented_movies(self):
        return self.moviesrented

    # User Info
    def show_user_status(self):
        return self.username + " | Rented: " + str(len(self.moviesrented))

    def add_movies(self, title, playtime, age):
        self.movies.append({"title": title, "playtime": playtime, "age": age})

if __name__ == "__main__":
    alice = MovieStreamingPlatform("Alice")
    alice.add_movies("Barbie", "1h 54min", "PG-13")
    alice.add_movies("Inception", "2h 28min", "PG-13")
    alice.add_movies("Frozen", "1h 42min", "PG")

    print(alice.list_movies())
    print(alice.rent_movie("Barbie"))
    print(alice.get_movie_info("Barbie"))
    print(alice.get_rented_movies())

    run_rental_session(alice, "Alice", "Barbie", "Inception", "Frozen")

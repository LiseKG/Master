
# Rental Movie Streaming Platform - Single-Class God Design

# Requirements:
# - Alice should get a list of available movies
# - Should be able to add 3 movies and check that all movies are saved.
# - Alice should be able to rent "Barbie".
# - Alice should get information about playtime, movie age restrictions. (PG-13 , 1hour and 54 min)
# - Alice should be able to give a list over all rented movies
# - Return a list over all returned movies


def run_rental_session(platform, user_name, movie1, movie2, movie3):
    titles = [movie1, movie2, movie3]
    for title, playtime, age in [(movie1, "1h 54min", "PG-13"), (movie2, "2h 10min", "R"), (movie3, "1h 30min", "PG")]:
        platform.add_movies(title, playtime, age)
    result = [platform.list_movies()]
    result.extend(platform.get_movie_info(t) for t in titles)
    rents = [platform.rent_movie(t) for t in titles]
    result.extend(rents)
    result.append(platform.get_rented_movies())
    result.append(platform.show_user_status())
    result.extend(platform.get_movie_info(t) for t in titles)
    result.append(platform.list_movies())
    result.append(platform.get_rented_movies())
    result.append(platform.show_user_status())
    result.append(" ".join(str(r) for r in rents))
    result.append(user_name)
    return result


class MovieStreamingPlatform:
    def __init__(self, user_name):
        self.username = user_name
        self.moviesrented = []
        self.movies = [{}]

    # Movie Browsing & Rental
    def list_movies(self):
        return [movie["title"] for movie in self.movies if "title" in movie]

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

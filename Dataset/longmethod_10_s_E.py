class MovieStreamingPlatform:
    def __init__(self, user_name):
        self.username = user_name
        self.moviesrented = []  # information about the movie and status (rented, returned, wishlist)
        self.movies = []  # List containing information and available movies

    # Movie Browsing & Rental
    def list_movies(self):
        return self.movies

    def rent_movie(self, movie_name):
        for movie in self.movies:
            if movie_name == movie["title"]:  # Directly compare movie titles
                self.moviesrented.append(movie_name)
                return f"{movie_name} has been rented."
        return f"{movie_name} is not available."

    # Movie Information
    def get_movie_info(self, movie_name):
        for movie in self.movies:
            if movie_name == movie["title"]:  # Directly compare movie titles
                return f"{movie_name} - {movie['age']}, {movie['playtime']}"
        return f"{movie_name} is not found."

    def get_rented_movies(self):
        return self.moviesrented

    def add_movies(self, title, playtime, age):
        self.movies.append({"title": title, "playtime": playtime, "age": age})


def long_method(movie_platform):
    # Movies to add
    movies_to_add = [
        ("Barbie2", "1 hour and 54 min", "PG-13"),
        ("Inception", "2 hours and 28 min", "PG-13"),
        ("The Lion King", "1 hour and 58 min", "G")
    ]

    # Add movies in a single loop
    for title, playtime, age in movies_to_add:
        movie_platform.add_movies(title, playtime, age)

    available_movies = movie_platform.list_movies()
    print(f"Available movies: {available_movies}")

    rented_message = movie_platform.rent_movie("Barbie2")
    print(rented_message)

    # Getting and displaying movie info for added movies
    for title in ["Barbie2", "Inception", "The Lion King"]:
        info = movie_platform.get_movie_info(title)
        print(f"Movie Info: {info}")

    rented_movies = movie_platform.get_rented_movies()
    print(f"Rented Movies: {rented_movies}")

    # Check rental status of specific movies
    for title in ["Barbie2", "Inception", "The Lion King"]:
        rental_status = "currently rented." if title in rented_movies else "not rented."
        print(f"{title} is {rental_status}")

    # Display returned movies
    returned_movies = rented_movies  # assuming no movies have actually been returned yet
    print(f"Returned Movies: {returned_movies}")
    
    if returned_movies:
        for movie in returned_movies:
            print(f"{movie} has been returned.")
    else:
        print("No movies have been returned.")

    print("Movie rental summary completed.")
    print(f"Available movies after renting: {movie_platform.list_movies()}")
    print("End of long method.")


# Example of usage
# Example of usage
if __name__ == '__main__':
   msp = MovieStreamingPlatform("Netfilm")
   msp.list_movies()
   msp.add_movies("Barbie","PG-16","1:50")
   msp.rent_movie("Barbie")
   msp.get_movie_info("Barbie")
   msp.get_rented_movies()
   long_method(MovieStreamingPlatform("Testing"))
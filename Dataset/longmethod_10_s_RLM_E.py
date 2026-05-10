class MovieStreamingPlatform:
    def __init__(self, user_name):
        self.username = user_name
        self.movies_rented = []  # List containing titles of rented movies
        self.movies = []  # List containing information about available movies

    # Movie Browsing & Rental
    def list_movies(self):
        return self.movies

    def rent_movie(self, movie_name):
        for movie in self.movies:
            if movie_name == movie["title"]:
                self.movies_rented.append(movie_name)
                return f"{movie_name} has been rented."
        return f"{movie_name} is not available."

    # Movie Information
    def get_movie_info(self, movie_name):
        for movie in self.movies:
            if movie_name == movie["title"]:
                return f"{movie_name} - {movie['age']}, {movie['playtime']}"
        return f"{movie_name} is not found."

    def get_rented_movies(self):
        return self.movies_rented

    def add_movies(self, title, playtime, age):
        self.movies.append({"title": title, "playtime": playtime, "age": age})

    def display_movies_info(self):
        for movie in ["Barbie2", "Inception", "The Lion King"]:
            info = self.get_movie_info(movie)
            print(f"Movie Info: {info}")

    def check_rented_status(self, movie_name):
        if movie_name in self.movies_rented:
            print(f"{movie_name} is currently rented.")
        else:
            print(f"{movie_name} is not rented.")

    def return_movies_and_summary(self):
        if not self.movies_rented:
            print("No movies have been returned.")
            return
        
        for movie in self.movies_rented:
            print(f"{movie} has been returned.")
        self.movies_rented.clear()  # Reset rented movies after summary

def long_method(movie_platform):
    # Add movies in one go to minimize repetitive function calls
    movies_to_add = [
        ("Barbie2", "1 hour and 54 min", "PG-13"),
        ("Inception", "2 hours and 28 min", "PG-13"),
        ("The Lion King", "1 hour and 58 min", "G")
    ]
    for movie in movies_to_add:
        movie_platform.add_movies(*movie)

    print(f"Available movies: {movie_platform.list_movies()}")

    print(movie_platform.rent_movie("Barbie2"))

    movie_platform.display_movies_info()

    print(f"Rented Movies: {movie_platform.get_rented_movies()}")

    for title in ["Barbie2", "Inception", "The Lion King"]:
        movie_platform.check_rented_status(title)

    movie_platform.return_movies_and_summary()
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
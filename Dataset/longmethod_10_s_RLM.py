class MovieStreamingPlatform:
    def __init__(self, user_name):
        self.username = user_name
        self.moviesrented = []  # information about the movie and status (rented, returned, wishlist)
        self.movies = []  # List containing information and available movies

    # Movie Browsing & Rental
    def list_movies(self):
        return self.movies

    def rent_movie(self, movie_name):
        listofmovies = self.list_movies()
        for movie in listofmovies:
            if movie_name in movie["title"]:
                self.moviesrented.append(movie_name)
                return f"{movie_name} has been rented."
        return f"{movie_name} is not available."

    # Movie Information
    def get_movie_info(self, movie_name):
        listofmovies = self.list_movies()
        for movie in listofmovies:
            if movie_name in movie["title"]:
                return f"{movie_name} - PG-13, 1 hour and 54 min"

        return f"{movie_name} is not found."

    def get_rented_movies(self):
        return self.moviesrented

    def add_movies(self, title, playtime, age):
        self.movies.append({"title": title, "playtime": playtime, "age": age})

    def display_movies_info(self):
        for title in ["Barbie2", "Inception", "The Lion King"]:
            info = self.get_movie_info(title)
            print(f"Movie Info: {info}")

    def check_rented_status(self, movie_name):
        if movie_name in self.get_rented_movies():
            print(f"{movie_name} is currently rented.")
        else:
            print(f"{movie_name} is not rented.")

    def return_movies_and_summary(self):
        returned_movies = self.get_rented_movies()
        for movie in returned_movies:
            print(f"{movie} has been returned.")
        if not returned_movies:
            print("No movies have been returned.")

def long_method(movie_platform):
    movie_platform.add_movies("Barbie2", "1 hour and 54 min", "PG-13")
    movie_platform.add_movies("Inception", "2 hours and 28 min", "PG-13")
    movie_platform.add_movies("The Lion King", "1 hour and 58 min", "G")

    available_movies = movie_platform.list_movies()
    print(f"Available movies: {available_movies}")

    rented_message = movie_platform.rent_movie("Barbie2")
    print(rented_message)

    movie_platform.display_movies_info()

    rented_movies = movie_platform.get_rented_movies()
    print(f"Rented Movies: {rented_movies}")

    movie_platform.check_rented_status("Barbie2")
    movie_platform.check_rented_status("Inception")
    movie_platform.check_rented_status("The Lion King")

    movie_platform.return_movies_and_summary()
    print("Movie rental summary completed.")

    available_movies_after_rent = movie_platform.list_movies()
    print(f"Available movies after renting: {available_movies_after_rent}")
    print("End of long method.")

# Example of usage
if __name__ == '__main__':
   msp = MovieStreamingPlatform("Netfilm")
   msp.list_movies()
   msp.add_movies("Barbie","PG-16","1:50")
   msp.rent_movie("Barbie")
   msp.get_movie_info("Barbie")
   msp.get_rented_movies()
   long_method(MovieStreamingPlatform("Testing"))
class MovieStreamingPlatform:
    def __init__(self, user_name):
        self.username = user_name
        self.moviesrented = []  # information about the movie and status (rented, returned, wishlist)
        self.movies = []  # List containing information and available movies

    # Movie Browsing & Rental
    def list_movies(self):
        return self.movies

    def rent_movie(self, movie_name):
        listofmovies= self.list_movies()
        for movie in listofmovies:
            if movie_name in movie["title"]:
                self.moviesrented.append(movie_name)
                return f"{movie_name} has been rented."
        return f"{movie_name} is not available."

    # Movie Information
    def get_movie_info(self, movie_name):
        listofmovies= self.list_movies()
        for movie in listofmovies:
            if movie_name in movie["title"]:
                return f"{movie_name} - PG-13, 1 hour and 54 min"
        
        return f"{movie_name} is not found."

    def get_rented_movies(self):
        return self.moviesrented

    def add_movies(self, title, playtime, age):
        self.movies.append({"title": title, "playtime": playtime, "age": age})


def long_method(movie_platform):
    #1
    movie_platform.add_movies("Barbie2", "1 hour and 54 min", "PG-13")
    #2
    movie_platform.add_movies("Inception", "2 hours and 28 min", "PG-13")
    #3
    movie_platform.add_movies("The Lion King", "1 hour and 58 min", "G")
    #4
    available_movies = movie_platform.list_movies()
    #5
    print(f"Available movies: {available_movies}")
    #6
    rented_message = movie_platform.rent_movie("Barbie2")
    #7
    print(rented_message)
    #8
    info = movie_platform.get_movie_info("Barbie2")
    #9
    print(f"Movie Info: {info}")
    #10
    info_inception = movie_platform.get_movie_info("Inception")
    #11
    print(f"Movie Info: {info_inception}")
    #12
    rented_movies = movie_platform.get_rented_movies()
    #13
    print(f"Rented Movies: {rented_movies}")
    #14
    if "Barbie2" in rented_movies:
        #15
        print("Barbie2 is currently rented.")
    #16
    else:
        #17
        print("Barbie2 is not rented.")
    #18
    if "Inception" in rented_movies:
        #19
        print("Inception is currently rented.")
    #20
    else:
        #21
        print("Inception is not rented.")
    #22
    if "The Lion King" in rented_movies:
        #23
        print("The Lion King is currently rented.")
    #24
    else:
        #25
        print("The Lion King is not rented.")
    #26
    returned_movies = movie_platform.get_rented_movies()
    #27
    print(f"Returned Movies: {returned_movies}")
    #28
    for movie in returned_movies:
        #29
        print(f"{movie} has been returned.")
    #30
    if not returned_movies:
        #31
        print("No movies have been returned.")
    #32
    print("Movie rental summary completed.")
    #33
    available_movies_after_rent = movie_platform.list_movies()
    #34
    print(f"Available movies after renting: {available_movies_after_rent}")
    #35
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
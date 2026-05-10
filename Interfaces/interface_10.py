
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
        self.moviesrented = [] #information about the movie and status (rented,returned, wishlist)
        self.movies = [{}] #Dict conaining information and available movies

    # Movie Browsing & Rental
    def list_movies(self):
        pass

    def rent_movie(self, movie_name):
        pass
    #return a string saying movie name rented and add to movies rented list

    # Movie Information
    def get_movie_info(self, movie_name):
        pass
    #Get information about the movie and return them in a string

    def get_rented_movies(self):
        pass
    #return list of rented movies

    # User Info
    def show_user_status(self):
        pass

    def add_movies(self,title,playtime,age):
        pass
    #append movie information, title,playtime and age restriction


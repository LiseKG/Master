class MovieStreamingPlatform:
    def __init__(self, user_name):
        self.username = user_name
        self.movies_rented = []  # information about the movie and status (rented, returned, wishlist)
        self.movies = []  # List containing information about available movies

    # Movie Browsing & Rental
    def list_movies(self):
        return self.movies

    def rent_movie(self, movie_name):
        for movie in self.movies:
            if movie['title'] == movie_name:
                self.movies_rented.append(movie)
                return f"{movie_name} rented."
        return f"{movie_name} not available."

    # Movie Information
    def get_movie_info(self, movie_name):
        for movie in self.movies:
            if movie['title'] == movie_name:
                return f"Title: {movie['title']}, Playtime: {movie['playtime']}, Age Restriction: {movie['age']}"
        return f"{movie_name} not found."

    def get_rented_movies(self):
        return [movie['title'] for movie in self.movies_rented]

    # User Info
    def show_user_status(self):
        return f"User: {self.username}, Rented Movies: {len(self.movies_rented)}"

    def add_movies(self, title, playtime, age):
        self.movies.append({'title': title, 'playtime': playtime, 'age': age})


def list_rented_movies_info(platform):
    info = []
    rented_movie_titles = {movie['title']: movie for movie in platform.movies_rented}

    for title, movie in rented_movie_titles.items():
        info.append(f"Title: {title}")
        info.append(f"Playtime: {movie['playtime']}")
        info.append(f"Age Restriction: {movie['age']}")
        info.append("Rented Status: rented")
    
    # Gather user status information once, reducing unnecessary I/O operations
    user_info = f"User: {platform.username}, Total Rented: {len(platform.movies_rented)}"
    info.append(user_info)

    # Create a list of available movies instead of accessing it multiple times
    available_movies = [f"Available Movie: {m['title']}" for m in platform.movies]
    info.extend(available_movies)

    return "\n".join(info)

if __name__ == '__main__':
   msp = MovieStreamingPlatform("Netfilm")
   msp.list_movies()
   msp.add_movies("Barbie","PG-16","1:50")
   msp.rent_movie("Barbie")
   msp.get_movie_info("Barbie")
   msp.get_rented_movies()
   msp.show_user_status()
   print(list_rented_movies_info(msp))
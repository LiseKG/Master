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
            if movie['title'] == movie_name:
                self.moviesrented.append(movie)
                return f"{movie_name} rented."
        return f"{movie_name} not available."

    # Movie Information
    def get_movie_info(self, movie_name):
        for movie in self.movies:
            if movie['title'] == movie_name:
                return f"Title: {movie['title']}, Playtime: {movie['playtime']}, Age Restriction: {movie['age']}"
        return f"{movie_name} not found."

    def get_rented_movies(self):
        return [movie['title'] for movie in self.moviesrented]

    # User Info
    def show_user_status(self):
        return f"User: {self.username}, Rented Movies: {len(self.moviesrented)}"

    def add_movies(self, title, playtime, age):
        self.movies.append({'title': title, 'playtime': playtime, 'age': age})


def list_rented_movies_info(platform):
    info = []
    for movie in platform.moviesrented:
        info.append(get_movie_details(movie))
    
    info.append(get_user_details(platform))
    return "\n".join(info)


def get_movie_details(movie):
    return (
        f"Title: {movie['title']}\n"
        f"Playtime: {movie['playtime']}\n"
        f"Age Restriction: {movie['age']}\n"
        f"Rented Status: rented"
    )


def get_user_details(platform):
    user_info = []
    user_info.append(f"User: {platform.username}")
    user_info.append(f"Total Rented: {len(platform.moviesrented)}")
    user_info.append("Available Movies:")
    for movie in platform.movies:
        user_info.append(f"Available Movie: {movie['title']}")
    return "\n".join(user_info)

if __name__ == '__main__':
   msp = MovieStreamingPlatform("Netfilm")
   msp.list_movies()
   msp.add_movies("Barbie","PG-16","1:50")
   msp.rent_movie("Barbie")
   msp.get_movie_info("Barbie")
   msp.get_rented_movies()
   msp.show_user_status()
   print(list_rented_movies_info(msp))
   print(get_movie_details({"title":"Barbie","age":"PG-16","playtime":"1:50"}))
   print(get_user_details(msp))
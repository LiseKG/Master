class Movie:
    def __init__(self, title, playtime, age):
        self.title = title
        self.playtime = playtime
        self.age = age
        self.status = 'available'


class MovieStreamingPlatform:
    def __init__(self,name):
        self.name = name
        self.available_movies = []
        self.movies_rented = []

    def clear_rented_movies(self):
        self.movies_rented.clear()  # Clear the list efficiently

    def list_movies(self):
        return self.available_movies

    def add_movies(self, title, playtime, age):
        movie = Movie(title, playtime, age)
        self.available_movies.append(movie)

    def rent_movie(self, movie_name):
        for movie in self.available_movies:
            if movie.title == movie_name and movie.status == 'available':
                movie.status = 'rented'
                self.movies_rented.append(movie)
                return f"{movie_name} has been rented."
        return f"{movie_name} is not available for rent."

    def return_movie(self, movie_name):
        for movie in self.movies_rented:
            if movie.title == movie_name:
                movie.status = 'returned'
                self.movies_rented.remove(movie)  # Clear from rented list directly
                return f"{movie_name} has been returned."
        return f"{movie_name} is not in your rented movies."

    def get_movie_info(self, movie_name):
        for movie in self.available_movies:
            if movie.title == movie_name:
                return f"{movie.title} - Playtime: {movie.playtime} - Age restriction: {movie.age} movie status: {movie.status}"
        return f"No information found for {movie_name}."

    def get_rented_movies(self):
        return [movie.title for movie in self.movies_rented]

    def update_movie_status(self, title, status):
        for movie in self.available_movies:
            if movie.title == title:
                movie.status = status
                return f"Updated the status of {title} to {status}."
        return f"{title} does not exist."

    def search_movie_by_title(self, title):
        title_lower = title.lower()  # Save some computations
        results = [self.get_movie_info(movie.title) for movie in self.available_movies if title_lower in movie.title.lower()]
        return results if results else "No movies found matching your search."

    def get_age_restricted_movies(self, min_age):
        return [movie.title for movie in self.available_movies if movie.age > min_age]

    def get_movies_based_on_restriction(self, age):
        return [movie.title for movie in self.available_movies if movie.age <= age]

    def get_movies_by_age_range(self, min_age, max_age):
        return [movie.title for movie in self.available_movies if min_age < movie.age < max_age]

    def get_movies_with_playtime_above(self, minutes):
        return [movie.title for movie in self.available_movies if int(movie.playtime.split()[0]) > minutes]


class User:
    def __init__(self, user_name, rental_manager):
        self.username = user_name
        self.rental_manager = rental_manager

    def show_user_status(self):
        rented_titles = self.rental_manager.get_rented_movies()
        return f"{self.username}, you have rented: {', '.join(rented_titles) if rented_titles else 'No rented movies.'}"

    def get_user_name(self):
        return self.username


# Example usage
if __name__ == "__main__":
    rental_manager = MovieStreamingPlatform("Flix")
    user = User("Alice", rental_manager)

    # --- Add Movies ---
    rental_manager.add_movies("Inception", "148 minutes", 13)
    rental_manager.add_movies("Toy Story", "81 minutes", 0)
   
    multiple_movies = [
        {"title": "The Matrix", "playtime": "136 minutes", "age": 16},
        {"title": "Frozen", "playtime": "102 minutes", "age": 0},
    ]
    for movie in multiple_movies:
        rental_manager.add_movies(movie['title'], movie['playtime'], movie['age'])

    # --- List Movies ---
    print("All movie titles:", [movie.title for movie in rental_manager.list_movies()])
    print("List movies:",   [rental_manager.get_movie_info(movie.title) for movie in rental_manager.available_movies])
    print("Total movies:", len(rental_manager.available_movies))

    # --- Movie Info ---
    print(rental_manager.get_movie_info("Inception"))
    print(rental_manager.get_movie_info("Unknown"))

    # --- Check Availability ---
    print("Is Inception available?", rental_manager.rent_movie("Inception"))
    print("Does Matrix exist?", any(movie.title == "The Matrix" for movie in rental_manager.available_movies))
    print("Does Avatar exist?", any(movie.title == "Avatar" for movie in rental_manager.available_movies))

    # --- Rent Movie ---
    print(rental_manager.rent_movie("Inception"))
    print("Rented movies:", rental_manager.get_rented_movies())
    print("Total rented movies:", len(rental_manager.movies_rented))
    print("Is Inception available now?", rental_manager.rent_movie("Inception"))

     # --- Get Movie Status ---
    print(rental_manager.get_movie_info("Inception"))

    # --- Return Movie ---
    print(rental_manager.return_movie("Inception"))
    print("Rented movies after return:", user.show_user_status())

    # --- Update Movie Status ---
    print(rental_manager.update_movie_status("Toy Story", "maintenance"))
    print(rental_manager.get_movie_info("Toy Story"))

    # --- Search Movie ---
    print("Search 'matrix':", rental_manager.search_movie_by_title("matrix"))
    print("Search 'xyz':", rental_manager.search_movie_by_title("xyz"))

    # --- Movies Based on Age Restriction ---
    print("Movies allowed for age 10:", rental_manager.get_movies_based_on_restriction(10))
    print("Age restricted movies above 10:", rental_manager.get_age_restricted_movies(10))
    print("Movies between age 5 and 15:", rental_manager.get_movies_by_age_range(5, 15))

    # --- Movies by Playtime ---
    print("Movies longer than 100 minutes:", rental_manager.get_movies_with_playtime_above(100))

    # --- Rent Multiple & Show Detailed Rented Info ---
    print(rental_manager.rent_movie("The Matrix"))
    print(rental_manager.rent_movie("Frozen"))
    #print("Rented movies with info:", rental_manager.list_rented_movies_with_info())
    print("Rented movies with info:", [rental_manager.get_movie_info(movie) for movie in rental_manager.get_rented_movies()])

    # --- User Info ---
    print(user.show_user_status())
    print("Username:", user.get_user_name())

    # --- Clear Rented Movies ---
    rental_manager.clear_rented_movies()
    print("Rented movies after clearing:", rental_manager.get_rented_movies())
    print("Total rented movies after clearing:", len(rental_manager.movies_rented))
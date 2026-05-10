# Rental Movie Streaming Platform - Single-Class God Design

class MovieStreamingPlatform:
    def __init__(self, user_name):
        self.username = user_name
        self.movies_rented = []  # List of rented movies
        self.available_movies = []  # List of available movies

    # Movie Browsing & Rental
    def list_movies(self):
        return self.available_movies

    def rent_movie(self, movie_name):
        for movie in self.available_movies:
            if movie['title'] == movie_name and movie['status'] == 'available':
                movie['status'] = 'rented'
                self.movies_rented.append(movie)
                return f"{movie_name} has been rented."
        return f"{movie_name} is not available for rent."

    def return_movie(self, movie_name):
        for movie in self.movies_rented:
            if movie['title'] == movie_name:
                movie['status'] = 'returned'
                self.movies_rented.remove(movie)
                return f"{movie_name} has been returned."
        return f"{movie_name} is not in your rented movies."

    # Adding Movies
    def add_movies(self, title, playtime, age):
        movie_info = {
            'title': title,
            'playtime': playtime,
            'age': age,
            'status': 'available'
        }
        self.available_movies.append(movie_info)

    def add_multiple_movies(self, movie_list):
        for movie in movie_list:
            self.add_movies(movie['title'], movie['playtime'], movie['age'])

    # Movie Information
    def get_movie_info(self, movie_name):
        for movie in self.available_movies:
            if movie['title'] == movie_name:
                return f"{movie['title']} - Playtime: {movie['playtime']} - Age restriction: {movie['age']}"
        return f"No information found for {movie_name}."

    def get_rented_movies(self):
        return [movie['title'] for movie in self.movies_rented]

    def get_all_movie_titles(self):
        return [movie['title'] for movie in self.available_movies]

    # User Info
    def show_user_status(self):
        rented_titles = self.get_rented_movies()
        return f"{self.username}, you have rented: {', '.join(rented_titles) if rented_titles else 'No rented movies.'}"

    def get_user_name(self):
        return self.username

    def is_movie_available(self, movie_name):
        for movie in self.available_movies:
            if movie['title'] == movie_name and movie['status'] == 'available':
                return True
        return False

    def get_movies_based_on_restriction(self, age):
        return [movie['title'] for movie in self.available_movies if movie['age'] <= age]

    # Utility Methods
    def get_total_movies(self):
        return len(self.available_movies)

    def get_total_rented_movies(self):
        return len(self.movies_rented)

    def get_movies_with_playtime_above(self, minutes):
        return [movie['title'] for movie in self.available_movies if int(movie['playtime'].split()[0]) > minutes]

    def clear_rented_movies(self):
        self.movies_rented = []

    def movie_exists(self, title):
        return any(movie for movie in self.available_movies if movie['title'] == title)

    def get_movie_status(self, title):
        for movie in self.available_movies:
            if movie['title'] == title:
                return f"{movie['title']} is currently {movie['status']}."
        return f"{title} does not exist."

    def update_movie_status(self, title, status):
        for movie in self.available_movies:
            if movie['title'] == title:
                movie['status'] = status
                return f"Updated the status of {title} to {status}."
        return f"{title} does not exist."

    def search_movie_by_title(self, title):
        results = [movie for movie in self.available_movies if title.lower() in movie['title'].lower()]
        return results if results else "No movies found matching your search."

    def list_rented_movies_with_info(self):
        return [(movie['title'], movie['playtime'], movie['age']) for movie in self.movies_rented]

    def get_age_restricted_movies(self, min_age):
        return [movie['title'] for movie in self.available_movies if movie['age'] > min_age]

    def get_movies_by_age_range(self, min_age, max_age):
        return [movie['title'] for movie in self.available_movies if min_age < movie['age'] < max_age]

# Example usage
if __name__ == "__main__":
    platform = MovieStreamingPlatform("Alice")

    # --- Add Movies ---
    platform.add_movies("Inception", "148 minutes", 13)
    platform.add_movies("Toy Story", "81 minutes", 0)

    multiple_movies = [
        {"title": "The Matrix", "playtime": "136 minutes", "age": 16},
        {"title": "Frozen", "playtime": "102 minutes", "age": 0},
    ]
    platform.add_multiple_movies(multiple_movies)

    # --- List Movies ---
    print("All movie titles:", platform.get_all_movie_titles())
    print("List movies:", platform.list_movies())
    print("Total movies:", platform.get_total_movies())

    # --- Movie Info ---
    print(platform.get_movie_info("Inception"))
    print(platform.get_movie_info("Unknown"))

    # --- Check Availability ---
    print("Is Inception available?", platform.is_movie_available("Inception"))
    print("Does Matrix exist?", platform.movie_exists("The Matrix"))
    print("Does Avatar exist?", platform.movie_exists("Avatar"))

    # --- Rent Movie ---
    print(platform.rent_movie("Inception"))
    print("Rented movies:", platform.get_rented_movies())
    print("Total rented movies:", platform.get_total_rented_movies())
    print("Is Inception available now?", platform.is_movie_available("Inception"))

    # --- Get Movie Status ---
    print(platform.get_movie_status("Inception"))

    # --- Return Movie ---
    print(platform.return_movie("Inception"))
    print("Rented movies after return:", platform.get_rented_movies())

    # --- Update Movie Status ---
    print(platform.update_movie_status("Toy Story", "maintenance"))
    print(platform.get_movie_status("Toy Story"))

    # --- Search Movie ---
    print("Search 'matrix':", platform.search_movie_by_title("matrix"))
    print("Search 'xyz':", platform.search_movie_by_title("xyz"))

    # --- Movies Based on Age Restriction ---
    print("Movies allowed for age 10:", platform.get_movies_based_on_restriction(10))
    print("Age restricted movies above 10:", platform.get_age_restricted_movies(10))
    print("Movies between age 5 and 15:", platform.get_movies_by_age_range(5, 15))

    # --- Movies by Playtime ---
    print("Movies longer than 100 minutes:", platform.get_movies_with_playtime_above(100))

    # --- Rent Multiple & Show Detailed Rented Info ---
    print(platform.rent_movie("The Matrix"))
    print(platform.rent_movie("Frozen"))
    print("Rented movies with info:", platform.list_rented_movies_with_info())

    # --- User Info ---
    print(platform.show_user_status())
    print("Username:", platform.get_user_name())

    # --- Clear Rented Movies ---
    platform.clear_rented_movies()
    print("Rented movies after clearing:", platform.get_rented_movies())
    print("Total rented movies after clearing:", platform.get_total_rented_movies())


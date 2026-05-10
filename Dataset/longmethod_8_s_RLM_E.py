class User:
    def __init__(self, username):
        self.username = username


class SocialMediaPlatform:
    def __init__(self):
        self.platform = []
        self.pictures = {}  # User : [list of pictures posted - {each picture and number of likes}] 

    def add_picture(self, user, picture_name):
        if user not in self.pictures:
            self.pictures[user] = []
        self.pictures[user].append({"name": picture_name, "likes": 0})
        return f"{user.username} posted a picture: {picture_name}"

    def _find_picture(self, picture_name):
        """ Helper function to find the picture and return it if exists. """
        for user_pictures in self.pictures.values():
            for pic in user_pictures:
                if pic["name"] == picture_name:
                    return pic
        return None

    def add_like(self, user, picture_name):
        pic = self._find_picture(picture_name)
        if pic is not None:
            pic["likes"] += 1
            return f"{user.username} liked the picture: {picture_name}"
        return "Picture not found."

    def remove_like(self, user, picture_name):
        pic = self._find_picture(picture_name)
        if pic is not None and pic["likes"] > 0:
            pic["likes"] -= 1
            return f"{user.username} unliked the picture: {picture_name}"
        return "Picture not found."

    def show_total_likes(self, user, picture_name):
        pic = self._find_picture(picture_name)
        if pic is not None:
            return f"Total likes for {picture_name}: {pic['likes']}"
        return "Picture not found."

    def show_picture_details(self, picture_name):
        pic = self._find_picture(picture_name)
        if pic is not None:
            return f"Picture name: {picture_name}, likes: {pic['likes']}"
        return "Picture not found."


def give_likes(platform, user):
    post_two_pictures(platform, user)
    add_likes_to_pictures(platform)


def post_two_pictures(platform, user):
    """ Posts two pictures for the user. """
    pictures = ["Sunset", "Beach"]
    for picture in pictures:
        platform.add_picture(user, picture)


def add_likes_to_pictures(platform):
    users = [User("Jon Pork"), User("Chris P Bacon")]
    pictures = ["Sunset", "Beach"]
    
    # Adding likes with reduced repetition
    for picture in pictures:
        for user in users:
            platform.add_like(user, pictures[0])
            platform.add_like(user, pictures[0])
            platform.remove_like(user, pictures[0])  # Unlike once for both users

    display_likes(platform, users[0], users[1], pictures)


def display_likes(platform, user_like1, user_like2, pictures):
    for picture in pictures:
        likes1 = platform.show_total_likes(user_like1, picture)
        likes2 = platform.show_total_likes(user_like2, picture)
        print(likes1)
        print(likes2)
        platform.show_picture_details(picture)

    new_users_likes(platform)


def new_users_likes(platform):
    new_users = [User(f"User{i}") for i in range(1, 6)]
    pictures = ["Sunset","beach"]

    # Likes from new users
    for user in new_users:
        platform.add_like(user, pictures[0])  # All like Sunset
    #platform.add_like(new_users[4], pictures[1])  # Only User5 likes Beach


if __name__ == "__main__":
    # Create platform and main user
    platform = SocialMediaPlatform()
    main_user = User("Alice")

    # Directly test add_picture
    result_post = platform.add_picture(main_user, "Mountain")
    print(result_post)

    # Directly test add_like
    liker = User("Bob")
    result_like = platform.add_like(liker, "Mountain")
    print(result_like)

    # Directly test remove_like
    result_unlike = platform.remove_like(liker, "Mountain")
    print(result_unlike)

    # Directly test show_total_likes
    total_likes = platform.show_total_likes(liker, "Mountain")
    print(total_likes)

    # Directly test show_picture_details
    details = platform.show_picture_details("Mountain")
    print(details)

    # Test the long function give_likes (covers all platform methods again)
    give_likes(platform, main_user)

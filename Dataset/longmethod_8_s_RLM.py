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

    def add_like(self, user, picture_name):
        for user_pictures in self.pictures.values():
            for pic in user_pictures:
                if pic["name"] == picture_name:
                    pic["likes"] += 1
                    return f"{user.username} liked the picture: {picture_name}"
        return "Picture not found."

    def remove_like(self, user, picture_name):
        for user_pictures in self.pictures.values():
            for pic in user_pictures:
                if pic["name"] == picture_name and pic["likes"] > 0:
                    pic["likes"] -= 1
                    return f"{user.username} unliked the picture: {picture_name}"
        return "Picture not found."

    def show_total_likes(self, user, picture_name):
        for user_pictures in self.pictures.values():
            for pic in user_pictures:
                if pic["name"] == picture_name:
                    return f"Total likes for {picture_name}: {pic['likes']}"
        return "Picture not found."

    def show_picture_details(self, picture_name):
        for user_pictures in self.pictures.values():
            for pic in user_pictures:
                if pic["name"] == picture_name:
                    return f"Picture name: {picture_name}, likes: {pic['likes']}"
        return "Picture not found."


def give_likes(platform, user):
    post_two_pictures(platform, user)
    add_likes_to_pictures(platform)


def post_two_pictures(platform, user):
    picture1 = "Sunset"
    picture2 = "Beach"
    platform.add_picture(user, picture1)
    platform.add_picture(user, picture2)


def add_likes_to_pictures(platform):
    user_like1 = User("Jon Pork")
    user_like2 = User("Chris P Bacon")
    picture1 = "Sunset"
    picture2 = "Beach"
    
    platform.add_like(user_like1, picture1)
    platform.add_like(user_like2, picture1)
    platform.add_like(user_like1, picture2)
    platform.add_like(user_like2, picture2)
    platform.add_like(user_like1, picture1)
    platform.add_like(user_like2, picture1)
    platform.remove_like(user_like1, picture2)
    platform.add_like(user_like2, picture1)
    platform.remove_like(user_like1, picture1)
    platform.remove_like(user_like2, picture2)

    display_likes(platform, user_like1, user_like2, picture1, picture2)


def display_likes(platform, user_like1, user_like2, picture1, picture2):
    likes1 = platform.show_total_likes(user_like1, picture1)
    likes2 = platform.show_total_likes(user_like2, picture1)
    likes3 = platform.show_total_likes(user_like1, picture2)
    platform.show_picture_details(picture1)
    platform.show_picture_details(picture2)
    
    print(likes1)
    print(likes2)
    print(likes3)

    new_users_likes(platform)


def new_users_likes(platform):
    new_user1 = User("User1")
    new_user2 = User("User2")
    new_user3 = User("User3")
    new_user4 = User("User4")
    new_user5 = User("User5")
    picture1 = "Sunset"
    picture2 = "Beach"

    platform.add_like(new_user1, picture1)
    platform.add_like(new_user2, picture1)
    platform.add_like(new_user3, picture1)
    platform.add_like(new_user4, picture1)
    platform.add_like(new_user5, picture2)
    platform.add_like(new_user1, picture2)


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
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
    #1
    picture1 = "Sunset"
    #2
    picture2 = "Beach"
    #3
    platform.add_picture(user, picture1)
    #4
    platform.add_picture(user, picture2)
    #5
    user_like1 = User("Jon Pork")
    #6
    user_like2 = User("Chris P Bacon")
    #7
    platform.add_like(user_like1, picture1)
    #8
    platform.add_like(user_like2, picture1)
    #9
    platform.add_like(user_like1, picture2)
    #10
    platform.add_like(user_like2, picture2)
    #11
    platform.add_like(user_like1, picture1)
    #12
    platform.add_like(user_like2, picture1)
    #13
    platform.remove_like(user_like1, picture2)
    #14
    platform.add_like(user_like2, picture1)
    #15
    platform.remove_like(user_like1, picture1)
    #16
    platform.remove_like(user_like2, picture2)
    #17
    likes1 = platform.show_total_likes(user_like1, picture1)
    #18
    likes2 = platform.show_total_likes(user_like2, picture1)
    #19
    likes3 = platform.show_total_likes(user_like1, picture2)
    #20
    platform.show_picture_details(picture1)
    #21
    platform.show_picture_details(picture2)
    #22
    print(likes1)
    #23
    print(likes2)
    #24
    print(likes3)
    #25
    new_user1 = User("User1")
    #26
    new_user2 = User("User2")
    #27
    new_user3 = User("User3")
    #28
    new_user4 = User("User4")
    #29
    new_user5 = User("User5")
    #30
    platform.add_like(new_user1, picture1)
    #31
    platform.add_like(new_user2, picture1)
    #32
    platform.add_like(new_user3, picture1)
    #33
    platform.add_like(new_user4, picture1)
    #34
    platform.add_like(new_user5, picture2)
    #35
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
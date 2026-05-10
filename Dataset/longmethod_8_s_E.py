class User:
    def __init__(self, username):
        self.username = username


class SocialMediaPlatform:
    def __init__(self):
        self.pictures = {}  # User : [list of pictures posted - {each picture and number of likes}] 

    def add_picture(self, user, picture_name):
        if user not in self.pictures:
            self.pictures[user] = []
        self.pictures[user].append({"name": picture_name, "likes": 0})
        return f"{user.username} posted a picture: {picture_name}"

    def _find_picture(self, picture_name):
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
    picture1 = "Sunset"
    picture2 = "Beach"
    platform.add_picture(user, picture1)
    platform.add_picture(user, picture2)
    
    users_likes = [
        User("Jon Pork"),
        User("Chris P Bacon"),
        User("User1"),
        User("User2"),
        User("User3"),
        User("User4"),
        User("User5"),
    ]

    for user_like in users_likes[:2]:  # Jon Pork and Chris P Bacon like the first two pictures
        platform.add_like(user_like, picture1)
        platform.add_like(user_like, picture2)

    platform.add_like(users_likes[0], picture1)  # Jon likes the first picture again
    platform.add_like(users_likes[1], picture1)  # Chris likes the first picture again
    platform.remove_like(users_likes[0], picture2)  # Jon unlikes the second picture
    platform.add_like(users_likes[1], picture1)  # Chris likes the first picture again
    platform.remove_like(users_likes[0], picture1)  # Jon unlikes the first picture
    platform.remove_like(users_likes[1], picture2)  # Chris unlikes the second picture

    for user_like in users_likes[:2]:  # Show likes for Jon and Chris
        print(platform.show_total_likes(user_like, picture1))
        print(platform.show_total_likes(user_like, picture2))

    platform.show_picture_details(picture1)
    platform.show_picture_details(picture2)

    for new_user in users_likes[2:]:  # The other users liking the pictures
        platform.add_like(new_user, picture1)  # 4 out of 5 like the first picture
        if new_user.username == "User5":
            platform.add_like(new_user, picture2)  # Only User5 likes the second picture

if __name__ == "__main__":
    platform = SocialMediaPlatform()
    main_user = User("Alice")

    result_post = platform.add_picture(main_user, "Mountain")
    print(result_post)

    liker = User("Bob")
    result_like = platform.add_like(liker, "Mountain")
    print(result_like)

    result_unlike = platform.remove_like(liker, "Mountain")
    print(result_unlike)

    total_likes = platform.show_total_likes(liker, "Mountain")
    print(total_likes)

    details = platform.show_picture_details("Mountain")
    print(details)

    give_likes(platform, main_user)

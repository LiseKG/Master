# Social Media Platform

# Requirements:
# - Alice can post a picture
# - Jon Pork and Chris P Bacon can like the picture
# - Show total number of likes
# - Jon can unlike, decreasing total likes


class User:
    def __init__(self, username):
        self.username = username

    def give_likes(self, platform, user):
        platform.add_like(user, platform.pictures[0]["name"] if platform.pictures else "")


class SocialMediaPlatform:
    def __init__(self):
        self.platform = []
        self.pictures = []

    def add_picture(self, user, picture_name):
        self.pictures.append({"user": user.username, "name": picture_name, "likes": 0})
        return f"{user.username} posted {picture_name}"

    def add_like(self, user, picture_name):
        for pic in self.pictures:
            if pic["name"] == picture_name:
                pic["likes"] += 1
        return f"{user.username} liked {picture_name}"

    def remove_like(self, user, picture_name):
        for pic in self.pictures:
            if pic["name"] == picture_name and pic["likes"] > 0:
                pic["likes"] -= 1
        return f"{user.username} unliked {picture_name}"

    def show_total_likes(self, user, picture_name):
        for pic in self.pictures:
            if pic["name"] == picture_name:
                return pic["likes"]
        return 0

    def show_picture_details(self, picture_name):
        for pic in self.pictures:
            if pic["name"] == picture_name:
                return pic["name"]
        return "Not found"

    def validate_platform(self):
        pictures = self.pictures
        platform_list = self.platform

        if pictures is None:
            return False
        if platform_list is None:
            return False
        if len(pictures) == 0:
            return False
        if pictures[0]["likes"] < 0:
            return False
        if self.show_total_likes(None, pictures[0]["name"]) < 0:
            return False
        if pictures[0]["name"] == "":
            return False
        if self.show_picture_details(pictures[0]["name"]) == "Not found":
            return False
        if len(platform_list) < 0:
            return False
        if pictures[-1]["likes"] < 0:
            return False
        if self.show_total_likes(None, pictures[-1]["name"]) < 0:
            return False
        if self.show_picture_details(pictures[-1]["name"]) == "":
            return False
        return pictures is not None


def validate_platform(platform):
    return platform.validate_platform()


def post_two_pictures_with_likes(user, platform):
    platform.add_picture(user, "photo1.jpg")
    platform.add_picture(user, "photo2.jpg")
    likers = [User("Jon"), User("Chris"), User("Bob"), User("Eve"), User("Sam")]
    for liker in likers:
        platform.add_like(liker, "photo1.jpg")
        platform.add_like(liker, "photo2.jpg")


if __name__ == "__main__":
    alice = User("Alice")
    jon = User("Jon")
    chris = User("Chris P Bacon")
    platform = SocialMediaPlatform()

    print(platform.add_picture(alice, "sunset.jpg"))
    print(platform.add_like(jon, "sunset.jpg"))
    print(platform.add_like(chris, "sunset.jpg"))
    print(platform.show_total_likes(alice, "sunset.jpg"))
    print(platform.remove_like(jon, "sunset.jpg"))
    print(platform.show_total_likes(alice, "sunset.jpg"))
    print(platform.show_picture_details("sunset.jpg"))
    jon.give_likes(platform, jon)

    post_two_pictures_with_likes(alice, platform)

    print(validate_platform(platform))



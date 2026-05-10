# Social Media Platform

# Requirements:
# - Alice can post a picture
# - Jon Pork and Chris P Bacon can like the picture
# - Show total number of likes
# - Jon can unlike, decreasing total likes


def post_and_interact(platform, username, pic1, pic2):
    pics = [pic1, pic2]
    likers = [User(n) for n in ["LikerOne", "LikerTwo", "LikerThree", "LikerFour", "LikerFive"]]
    for pic in pics:
        platform.add_picture(username, pic)
    for liker in likers:
        for pic in pics:
            platform.add_like(liker.username, pic)
    totals = [platform.show_total_likes(username, pic) for pic in pics]
    result = totals + [platform.show_picture_details(pic) for pic in pics]
    for liker in likers[:2]:
        platform.remove_like(liker.username, pic1)
    result.extend(platform.show_total_likes(username, pic) for pic in pics)
    result.append(" ".join(str(t) for t in totals))
    return result


class User:
    def __init__(self, username):
        self.username = username

    def give_likes(self, platform, user):
        for pic in platform.pictures.get(user, {}):
            platform.add_like(self.username, pic)


class SocialMediaPlatform:
    def __init__(self):
        self.platform = []
        self.pictures = {}

    def add_picture(self, user, picture_name):
        if user not in self.pictures:
            self.pictures[user] = {}
        self.pictures[user][picture_name] = []
        return user + " posted " + picture_name

    def add_like(self, user, picture_name):
        for owner in self.pictures:
            if picture_name in self.pictures[owner]:
                if user not in self.pictures[owner][picture_name]:
                    self.pictures[owner][picture_name].append(user)
                return user + " liked " + picture_name
        return "picture not found"

    def remove_like(self, user, picture_name):
        for owner in self.pictures:
            if picture_name in self.pictures[owner]:
                if user in self.pictures[owner][picture_name]:
                    self.pictures[owner][picture_name].remove(user)
                return user + " unliked " + picture_name
        return "picture not found"

    def show_total_likes(self, user, picture_name):
        if user in self.pictures:
            if picture_name in self.pictures[user]:
                return len(self.pictures[user][picture_name])
        return 0

    def show_picture_details(self, picture_name):
        for owner in self.pictures:
            if picture_name in self.pictures[owner]:
                return "Picture: " + picture_name
        return "not found"

if __name__ == "__main__":
    alice = User("Alice")
    jon = User("Jon Pork")
    chris = User("Chris P Bacon")

    smp = SocialMediaPlatform()
    smp.add_picture(alice.username, "sunset.jpg")
    smp.add_picture(alice.username, "beach.jpg")

    smp.add_like(jon.username, "sunset.jpg")
    smp.add_like(chris.username, "sunset.jpg")
    print(smp.show_total_likes(alice.username, "sunset.jpg"))

    smp.remove_like(jon.username, "sunset.jpg")
    print(smp.show_total_likes(alice.username, "sunset.jpg"))

    post_and_interact(smp, alice.username, "mountains.jpg", "forest.jpg")

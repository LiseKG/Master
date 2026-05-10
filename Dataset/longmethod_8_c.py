# Social Media Platform

# Requirements:
# - Alice can post a picture
# - Jon Pork and Chris P Bacon can like the picture
# - Show total number of likes
# - Jon can unlike, decreasing total likes


def post_and_interact(platform, username, pic1, pic2):
    platform.add_picture(username, pic1)
    platform.add_picture(username, pic2)
    user1 = User("LikerOne")
    user2 = User("LikerTwo")
    user3 = User("LikerThree")
    user4 = User("LikerFour")
    user5 = User("LikerFive")
    platform.add_like(user1.username, pic1)
    platform.add_like(user2.username, pic1)
    platform.add_like(user3.username, pic1)
    platform.add_like(user4.username, pic1)
    platform.add_like(user5.username, pic1)
    platform.add_like(user1.username, pic2)
    platform.add_like(user2.username, pic2)
    platform.add_like(user3.username, pic2)
    platform.add_like(user4.username, pic2)
    platform.add_like(user5.username, pic2)
    total1 = platform.show_total_likes(username, pic1)
    total2 = platform.show_total_likes(username, pic2)
    details1 = platform.show_picture_details(pic1)
    details2 = platform.show_picture_details(pic2)
    result = []
    result.append(total1)
    result.append(total2)
    result.append(details1)
    result.append(details2)
    platform.remove_like(user1.username, pic1)
    platform.remove_like(user2.username, pic1)
    updated1 = platform.show_total_likes(username, pic1)
    updated2 = platform.show_total_likes(username, pic2)
    result.append(updated1)
    result.append(updated2)
    summary = ""
    summary = summary + str(total1)
    summary = summary + " "
    summary = summary + str(total2)
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

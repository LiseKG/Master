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
            for picture in user_pictures:
                if picture["name"] == picture_name:
                    picture["likes"] += 1
                    return f"{user.username} liked the picture: {picture_name}"
        return "Picture not found."

    def remove_like(self, user, picture_name):
        for user_pictures in self.pictures.values():
            for picture in user_pictures:
                if picture["name"] == picture_name and picture["likes"] > 0:
                    picture["likes"] -= 1
                    return f"{user.username} unliked the picture: {picture_name}"
        return "Picture not found or no likes to remove."

    def show_total_likes(self, user, picture_name):
        for user_pictures in self.pictures.values():
            for picture in user_pictures:
                if picture["name"] == picture_name:
                    return f"Total likes for {picture_name}: {picture['likes']}"
        return "Picture not found."

    def show_picture_details(self, picture_name):
        for user_pictures in self.pictures.values():
            for picture in user_pictures:
                if picture["name"] == picture_name:
                    return f"Picture: {picture['name']} has {picture['likes']} likes."
        return "Picture not found."

def give_likes(platform, user):
    platform.add_picture(user, "Pic 1")
    platform.add_picture(user, "Pic 2")
    
    # Creating 5 new users to like the pictures
    user1 = User("User1")
    user2 = User("User2")
    user3 = User("User3")
    user4 = User("User4")
    user5 = User("User5")
    
    platform.add_like(user1, "Pic 1")
    platform.add_like(user2, "Pic 1")
    platform.add_like(user3, "Pic 1")
    platform.add_like(user4, "Pic 1")
    platform.add_like(user5, "Pic 1")
    platform.add_like(user1, "Pic 2")
    platform.add_like(user2, "Pic 2")
    platform.add_like(user3, "Pic 2")
    platform.add_like(user4, "Pic 2")
    platform.add_like(user5, "Pic 2")
    
    total_likes_pic1 = platform.show_total_likes(user1, "Pic 1")
    total_likes_pic2 = platform.show_total_likes(user2, "Pic 2")
    
    print(total_likes_pic1)
    print(total_likes_pic2)
    
    platform.remove_like(user3, "Pic 1")
    total_likes_pic1_after_unlike = platform.show_total_likes(user1, "Pic 1")
    
    print(total_likes_pic1_after_unlike)

if __name__ == '__main__':
   user = User("bob")
   sm = SocialMediaPlatform()
   print(sm.add_picture(user,"sunset"))
   print(sm.add_like(user,"sunset"))
   print(sm.show_total_likes(user,"sunset"))
   print(sm.remove_like(user,"sunset"))
   print(sm.show_total_likes(user,"sunset"))
   print(sm.show_picture_details("sunset"))
   print("---")
   print(sm.add_like(user,"sunset"))
   give_likes(sm,user)
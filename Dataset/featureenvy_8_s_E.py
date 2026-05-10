class User:
    def __init__(self, username):
        self.username = username

class SocialMediaPlatform:
    def __init__(self):
        self.platform = []
        self.pictures = {}  # User : [list of pictures posted with their names and likes] 

    def add_picture(self, user, picture_name):
        if user not in self.pictures:
            self.pictures[user] = []
        # Append picture name and initialize likes to 0
        self.pictures[user].append({"name": picture_name, "likes": 0})
        return f"{user.username} posted a picture: {picture_name}"

    # Helper function to find a picture by name, returns the picture data if found
    def _find_picture(self, picture_name):
        for user_pictures in self.pictures.values():
            for picture in user_pictures:
                if picture["name"] == picture_name:
                    return picture
        return None

    def add_like(self, user, picture_name):
        picture = self._find_picture(picture_name)
        if picture:
            picture["likes"] += 1
            return f"{user.username} liked the picture: {picture_name}"
        return "Picture not found."

    def remove_like(self, user, picture_name):
        picture = self._find_picture(picture_name)
        if picture and picture["likes"] > 0:
            picture["likes"] -= 1
            return f"{user.username} unliked the picture: {picture_name}"
        return "Picture not found or no likes to remove."

    def show_total_likes(self, user, picture_name):
        picture = self._find_picture(picture_name)
        if picture:
            return f"Total likes for {picture_name}: {picture['likes']}"
        return "Picture not found."

    def show_picture_details(self, picture_name):
        picture = self._find_picture(picture_name)
        if picture:
            return f"Picture: {picture['name']} has {picture['likes']} likes."
        return "Picture not found."

def give_likes(platform, user):
    platform.add_picture(user, "Pic 1")
    platform.add_picture(user, "Pic 2")
    
    # Creating and liking the pictures with new users
    likes_users = [User(f"User{i}") for i in range(1, 6)]
    
    for pic in ["Pic 1", "Pic 2"]:
        for like_user in likes_users:
            platform.add_like(like_user, pic)
    
    total_likes_pic1 = platform.show_total_likes(user, "Pic 1")
    total_likes_pic2 = platform.show_total_likes(user, "Pic 2")
    
    print(total_likes_pic1)
    print(total_likes_pic2)
    
    platform.remove_like(likes_users[2], "Pic 1")  # Unliking by the third user
    total_likes_pic1_after_unlike = platform.show_total_likes(user, "Pic 1")
    
    print(total_likes_pic1_after_unlike)

if __name__ == '__main__':
   user = User("bob")
   sm = SocialMediaPlatform()
   print(sm.add_picture(user, "sunset"))
   print(sm.add_like(user, "sunset"))
   print(sm.show_total_likes(user, "sunset"))
   print(sm.remove_like(user, "sunset"))
   print(sm.show_total_likes(user, "sunset"))
   print(sm.show_picture_details("sunset"))
   print("---")
   print(sm.add_like(user, "sunset"))
   give_likes(sm, user)

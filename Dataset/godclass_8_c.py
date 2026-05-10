# Social Media Platform

# Requirements:
# - Alice can post a picture
# - Jon Pork and Chris P Bacon can like the picture
# - Show total number of likes
# - Jon can unlike, decreasing total likes
# - method that takes a user and posts 2 pictures using add_picture
# - Creates 5 new users that like the pictures


class Picture:
    def __init__(self, name, owner_username):
        self.name = name
        self.owner_username = owner_username
        self.likes = []


class User:
    def __init__(self, username):
        self.username = username

    def give_likes(self, platform, picture_name):
        platform.add_like(self, picture_name)


class SocialMediaPlatform:
    def __init__(self):
        self.platform = []
        self.pictures = {}

    # Method 1
    def register_user(self, user: User):
        self.platform.append(user)
        self.log_action(f"User '{user.username}' registered.")

    # Method 2
    def log_action(self, message):
        print(f"[LOG] {message}")

    # Method 3
    def create_picture(self, user: User, picture_name):
        picture = Picture(picture_name, user.username)
        self.pictures[picture_name] = picture
        self.log_action(f"Picture '{picture_name}' created by '{user.username}'.")
        return picture

    # Method 4
    def add_picture(self, user: User, picture_name):
        self.create_picture(user, picture_name)
        print(f"{user.username} posted")
        return f"{user.username} posted"

    # Method 5
    def find_picture(self, picture_name):
        return self.pictures.get(picture_name, None)

    # Method 6
    def add_like(self, user: User, picture_name):
        picture = self.find_picture(picture_name)
        if picture is None:
            print(f"Picture '{picture_name}' not found.")
            return f"Picture '{picture_name}' not found."
        if user.username not in picture.likes:
            picture.likes.append(user.username)
        self.log_action(f"'{user.username}' liked '{picture_name}'.")
        print(f"{user.username} liked")
        return f"{user.username} liked"

    # Method 7
    def remove_like(self, user: User, picture_name):
        picture = self.find_picture(picture_name)
        if picture is None:
            return f"Picture '{picture_name}' not found."
        if user.username in picture.likes:
            picture.likes.remove(user.username)
            self.log_action(f"'{user.username}' unliked '{picture_name}'.")
            print(f"{user.username} unliked")
            return f"{user.username} unliked"
        return f"{user.username} has not liked '{picture_name}'."

    # Method 8
    def show_total_likes(self, user: User, picture_name):
        picture = self.find_picture(picture_name)
        if picture is None:
            print(f"Picture '{picture_name}' not found.")
            return 0
        total = len(picture.likes)
        print(f"'{picture_name}' has {total} like(s).")
        return total

    # Method 9
    def show_picture_details(self, picture_name):
        picture = self.find_picture(picture_name)
        if picture is None:
            print(f"Picture '{picture_name}' not found.")
            return
        print(f"Name: {picture.name} | Owner: {picture.owner_username} | Likes: {len(picture.likes)}")

    # Method 10
    def post_two_pictures(self, user: User, name1, name2):
        self.add_picture(user, name1)
        self.add_picture(user, name2)
        self.log_action(f"'{user.username}' posted two pictures: '{name1}' and '{name2}'.")

    # Method 11
    def register_and_like(self, username, picture_name):
        user = User(username)
        self.register_user(user)
        self.add_like(user, picture_name)
        return user

    # Method 12
    def bulk_like(self, usernames, picture_name):
        for username in usernames:
            self.register_and_like(username, picture_name)
        self.log_action(f"Bulk like on '{picture_name}' by {len(usernames)} users.")

    # Method 13
    def show_all_pictures(self, user: User):
        user_pics = [p for p in self.pictures.values() if p.owner_username == user.username]
        print(f"Pictures by '{user.username}':")
        for pic in user_pics:
            print(f"  - {pic.name} ({len(pic.likes)} like(s))")
        return user_pics

    # Method 14
    def get_most_liked(self):
        if not self.pictures:
            print("No pictures available.")
            return None
        top = max(self.pictures.values(), key=lambda p: len(p.likes))
        print(f"Most liked picture: '{top.name}' with {len(top.likes)} like(s).")
        self.show_picture_details(top.name)
        return top

    # Method 15
    def transfer_likes(self, from_picture, to_picture):
        src = self.find_picture(from_picture)
        dst = self.find_picture(to_picture)
        if src is None or dst is None:
            print("One or both pictures not found.")
            return
        for username in src.likes:
            if username not in dst.likes:
                dst.likes.append(username)
        src.likes = []
        self.log_action(f"Likes transferred from '{from_picture}' to '{to_picture}'.")
        self.show_total_likes(dst, to_picture)

    # Method 16
    def show_platform_summary(self):
        total_users = len(self.platform)
        total_pics = len(self.pictures)
        total_likes = sum(len(p.likes) for p in self.pictures.values())
        print(f"Platform summary: {total_users} user(s), {total_pics} picture(s), {total_likes} total like(s).")
        self.get_most_liked()


if __name__ == "__main__":
    platform = SocialMediaPlatform()

    alice = User("Alice")
    jon = User("Jon Pork")
    chris = User("Chris P Bacon")

    # Method 1 - register_user (calls log_action)
    platform.register_user(alice)
    platform.register_user(jon)
    platform.register_user(chris)

    # Method 10 - post_two_pictures (calls add_picture x2 -> create_picture -> log_action)
    platform.post_two_pictures(alice, "sunset.jpg", "beach.jpg")

    # Method 6 - add_like (calls find_picture, log_action)
    platform.add_like(jon, "sunset.jpg")
    platform.add_like(chris, "sunset.jpg")

    # User.give_likes calls platform.add_like
    jon.give_likes(platform, "beach.jpg")
    chris.give_likes(platform, "beach.jpg")

    # Method 8 - show_total_likes (calls find_picture)
    platform.show_total_likes(alice, "sunset.jpg")
    platform.show_total_likes(alice, "beach.jpg")

    # Method 7 - remove_like (calls find_picture, log_action)
    platform.remove_like(jon, "sunset.jpg")
    platform.show_total_likes(alice, "sunset.jpg")

    # Method 9 - show_picture_details (calls find_picture)
    platform.show_picture_details("sunset.jpg")

    # Method 12 - bulk_like (calls register_and_like -> register_user + add_like, log_action)
    platform.bulk_like(["User1", "User2", "User3", "User4", "User5"], "beach.jpg")

    # Method 13 - show_all_pictures (calls find_picture indirectly via list comp)
    platform.show_all_pictures(alice)

    # Method 15 - transfer_likes (calls find_picture, log_action, show_total_likes)
    platform.transfer_likes("beach.jpg", "sunset.jpg")

    # Method 16 - show_platform_summary (calls get_most_liked -> show_picture_details)
    platform.show_platform_summary()

    # Method 11 - register_and_like (calls register_user, add_like; called via bulk_like above, also direct)
    platform.register_and_like("ExtraUser", "sunset.jpg")

    # Method 5 - find_picture (standalone, called directly)
    pic = platform.find_picture("sunset.jpg")
    print(f"Found picture: {pic.name if pic else 'None'}")



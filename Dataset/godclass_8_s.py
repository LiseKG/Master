class User:
    def __init__(self, username):
        self.username = username


class SocialMediaPlatform:
    def __init__(self):
        self.platform = []
        self.pictures = {}  # User: [list of pictures posted - {each picture and number of likes}]

    def add_picture(self, user, picture_name):
        if user.username not in self.pictures:
            self.pictures[user.username] = []
        self.pictures[user.username].append({'name': picture_name, 'likes': 0})
        return f"{user.username} posted a picture: {picture_name}"

    def add_like(self, user, picture_name):
        for pics in self.pictures.values():
            for pic in pics:
                if pic['name'] == picture_name:
                    pic['likes'] += 1
                    return f"{user.username} liked the picture: {picture_name}"
        return f"Picture {picture_name} not found."

    def remove_like(self, user, picture_name):
        for pics in self.pictures.values():
            for pic in pics:
                if pic['name'] == picture_name and pic['likes'] > 0:
                    pic['likes'] -= 1
                    return f"{user.username} unliked the picture: {picture_name}"
        return f"Picture {picture_name} not found or no likes to remove."

    def show_total_likes(self, user, picture_name):
        for pics in self.pictures.values():
            for pic in pics:
                if pic['name'] == picture_name:
                    return f"Total likes for {picture_name}: {pic['likes']}"
        return f"Picture {picture_name} not found."

    def show_picture_details(self, picture_name):
        for pics in self.pictures.values():
            for pic in pics:
                if pic['name'] == picture_name:
                    return f"Picture: {pic['name']} has {pic['likes']} likes."
        return f"Picture {picture_name} not found."

    def get_all_pictures(self):
        all_pictures = []
        for pics in self.pictures.values():
            for pic in pics:
                all_pictures.append(pic['name'])
        return all_pictures

    def user_pictures(self, user):
        return self.pictures.get(user.username, [])

    def total_users(self):
        return len(self.pictures)

    def get_all_likes(self):
        total_likes = 0
        for pics in self.pictures.values():
            for pic in pics:
                total_likes += pic['likes']
        return total_likes

    def delete_picture(self, user, picture_name):
        if user.username in self.pictures:
            self.pictures[user.username] = [pic for pic in self.pictures[user.username] if pic['name'] != picture_name]
            return f"{user.username} deleted the picture: {picture_name}"
        return f"Picture {picture_name} not found for user {user.username}."

    def print_all_details(self):
        details = ""
        for user, pics in self.pictures.items():
            details += f"User: {user}, Pictures: {pics}\n"
        return details

    def is_picture_exists(self, picture_name):
        for pics in self.pictures.values():
            if any(pic['name'] == picture_name for pic in pics):
                return True
        return False

    def clear_user_pictures(self, user):
        if user.username in self.pictures:
            del self.pictures[user.username]
            return f"All pictures deleted for user {user.username}."
        return f"No pictures found for user {user.username}."

    def get_likes_by_user(self, user):
        likes = 0
        for pics in self.pictures.values():
            for pic in pics:
                if pic['likes'] > 0: 
                    likes += pic['likes']
        return f"Total likes by {user.username}: {likes}"

    def find_picture_owner(self, picture_name):
        for username, pics in self.pictures.items():
            for pic in pics:
                if pic['name'] == picture_name:
                    return f"The owner of {picture_name} is {username}."
        return f"No owner found for picture {picture_name}."

    def list_all_users(self):
        return list(self.pictures.keys())

    def total_pictures(self):
        return sum(len(pics) for pics in self.pictures.values())

    def get_picture_likes(self, picture_name):
        for pics in self.pictures.values():
            for pic in pics:
                if pic['name'] == picture_name:
                    return f"Likes for {picture_name}: {pic['likes']}"
        return f"Picture {picture_name} not found."

    def find_most_liked_picture(self):
        max_likes = 0
        most_liked = None
        for pics in self.pictures.values():
            for pic in pics:
                if pic['likes'] > max_likes:
                    max_likes = pic['likes']
                    most_liked = pic['name']
        return f"The most liked picture is {most_liked} with {max_likes} likes." if most_liked else "No pictures available."

    def reset_platform(self):
        self.platform.clear()
        self.pictures.clear()
        return "Social media platform has been reset."

    def is_user_exists(self, user):
        return user.username in self.pictures



if __name__ == '__main__':
    user = User("bob")
    sm = SocialMediaPlatform()
    sm.add_picture(user,"sunset")
    sm.add_like(user,"sunset")
    sm.remove_like(user,"sunset")
    sm.show_total_likes(user,"sunset")
    sm.show_picture_details("sunset")
    platform = SocialMediaPlatform()

    # Create users
    user1 = User("Alice")
    user2 = User("Bob")
    user3 = User("Charlie")

    # Add pictures
    print(platform.add_picture(user1, "sunset.jpg"))
    print(platform.add_picture(user1, "beach.png"))
    print(platform.add_picture(user2, "mountain.jpg"))

    # Like pictures
    print(platform.add_like(user2, "sunset.jpg"))
    print(platform.add_like(user3, "sunset.jpg"))
    print(platform.add_like(user1, "mountain.jpg"))

    # Remove like
    print(platform.remove_like(user3, "sunset.jpg"))

    # Show total likes for a picture
    print(platform.show_total_likes(user1, "sunset.jpg"))

    # Show picture details
    print(platform.show_picture_details("sunset.jpg"))

    # Get all pictures
    print("All pictures:", platform.get_all_pictures())

    # Get pictures by user
    print("Alice's pictures:", platform.user_pictures(user1))

    # Total users
    print("Total users:", platform.total_users())

    # Get all likes in platform
    print("Total likes in platform:", platform.get_all_likes())

    # Delete picture
    print(platform.delete_picture(user1, "beach.png"))

    # Print all details
    print("All platform details:")
    print(platform.print_all_details())

    # Check if picture exists
    print("Does 'sunset.jpg' exist?", platform.is_picture_exists("sunset.jpg"))
    print("Does 'unknown.jpg' exist?", platform.is_picture_exists("unknown.jpg"))

    # Get likes by user
    print(platform.get_likes_by_user(user1))

    # Find picture owner
    print(platform.find_picture_owner("sunset.jpg"))

    # List all users
    print("All users:", platform.list_all_users())

    # Total pictures
    print("Total pictures:", platform.total_pictures())

    # Get picture likes
    print(platform.get_picture_likes("sunset.jpg"))

    # Find most liked picture
    print(platform.find_most_liked_picture())

    # Check if user exists
    print("Is Alice exists?", platform.is_user_exists(user1))
    print("Is Charlie exists?", platform.is_user_exists(user3))

    # Clear user pictures
    print(platform.clear_user_pictures(user2))

    # Reset platform
    print(platform.reset_platform())

    # Final state check
    print("All users after reset:", platform.list_all_users())
    print("Total pictures after reset:", platform.total_pictures())

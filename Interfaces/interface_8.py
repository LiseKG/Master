# Social Media Platform

# Requirements:
# - Alice can post a picture
# - Jon Pork and Chris P Bacon can like the picture
# - Show total number of likes
# - Jon can unlike, decreasing total likes


class User:
    def __init__(self, username):
        self.username = username

class SocialMediaPlatform:
    def __init__(self):
        self.platform = []
        self.pictures = {{}} #User : [list of pcitures posted - {each picture and number of likes}] 

    def add_picture(self, user, picture_name):
        pass
        #add picture_name to pictures and return string saying posted

    def add_like(self, user, picture_name):
        pass
        #return a string saying liked

    def remove_like(self, user, picture_name):
        pass
        #return a string saying unliked

    def show_total_likes(self, user, picture_name):
        pass
        #show number of likes

    def show_picture_details(self, picture_name):
        pass
        #Show name.

def give_likes(self,platform,user):
    pass
#method that takes a user and post 2 pictures for the user using add pciture.
#  Creates 5 new users that likes the pictures.

# Simple Email Service

# Requirements:
# - Track emails (from, to, content)
# * Check that a mail from Alice, sent to Jon, contains a message saying hi
# - Show mailbox with new mails
# - Send a new emails to Jon saying Hello!
# - Send an email containing an image


class User:
    def __init__(self, email_address:str):
        self.email_address = email_address
        self.email = []

    def view_mailbox(self):
        pass #view emails
        
    def add_mail(self):
        pass #add emails to email list


class EmailSystem:
    def __init__(self):
        self.mailbox = []

    def send_email(self,sender:User, receiver:User, content:str):
        pass
    #return a string saying email is sent to user with content, append email to users mailbox

    def get_mailbox(self, user:User):
        pass
    #get mailbox to a user

    def track_email(self, sender:User, receiver:User, content:str):
        pass
    #return status either sent or recived.

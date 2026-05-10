class User:
    def __init__(self, email_address:str):
        self.email_address = email_address
        self.email = []

    def view_mailbox(self):
        for mail in self.email:
            print(f"From: {mail['from']}, To: {mail['to']}, Content: {mail['content']}")
        return self.email
        
    def add_mail(self, from_address:str, to_address:str, content:str):
        self.email.append({"from": from_address, "to": to_address, "content": content})


class EmailSystem:
    def __init__(self):
        self.mailbox = []

    def send_email(self,sender:User, receiver:User, content:str):
        receiver.add_mail(sender.email_address, receiver.email_address, content)
        return f"Email sent to {receiver.email_address} with content: {content}"

    def get_mailbox(self, user:User):
        return user.email

    def track_email(self, sender:User, receiver:User, content:str):
        return "Email sent"


def feature_envy_function(email_system: EmailSystem, user: User):
    # This function showcases feature envy as it directly accesses the attributes of User and EmailSystem
    email_system.send_email(User("alice@example.com"), user, "Hi")    
    email_system.send_email(User("alice@example.com"), user, "This is a test email.")
    email_system.send_email(User("alice@example.com"), user, "Enjoy this beautiful day.")
    email_system.send_email(User("alice@example.com"), user, "How are you?")
    email_system.send_email(User("alice@example.com"), user, "Hope you're well.")
    email_system.send_email(User("alice@example.com"), user, "See you soon.")
    email_system.send_email(User("alice@example.com"), user, "Don't forget to reply!")
    email_system.send_email(User("alice@example.com"), user, "Here's an image link.")
    email_system.send_email(User("alice@example.com"), user, "Check out my latest project.")
    email_system.send_email(User("alice@example.com"), user, "Let me know your thoughts.")



if __name__ == '__main__':
    email_system = EmailSystem()
    
    # Create user instances
    alice = User("alice@example.com")
    jon = User("jon@example.com")

    alice.view_mailbox()
    email_system.send_email(alice,jon,"Hi!")
    email_system.send_email(jon,alice,"Hello!")
    print(email_system.get_mailbox(jon),"Jons email")
    print(email_system.get_mailbox(alice),"Alice email")
    print(email_system.track_email(alice,jon,"Hi!"))
    print("alice mailbox before",len(alice.view_mailbox()))
    feature_envy_function(email_system,alice)
    print("alice mailbox after",len(alice.view_mailbox()))

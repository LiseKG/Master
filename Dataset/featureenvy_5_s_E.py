class User:
    def __init__(self, email_address: str):
        self.email_address = email_address
        self.email = []

    def view_mailbox(self):
        # Use a single print statement to reduce I/O operations
        print("Mailbox:")
        for mail in self.email:
            print(f"From: {mail['from']}, To: {mail['to']}, Content: {mail['content']}")
        return self.email
        
    def add_mail(self, from_address: str, to_address: str, content: str):
        self.email.append({"from": from_address, "to": to_address, "content": content})


class EmailSystem:
    def __init__(self):
        self.mailbox = []

    def send_email(self, sender: User, receiver: User, content: str):
        receiver.add_mail(sender.email_address, receiver.email_address, content)
        return f"Email sent to {receiver.email_address} with content: {content}"

    def get_mailbox(self, user: User):
        return user.email

    def track_email(self, sender: User, receiver: User, content: str):
        return "Email sent"


def feature_envy_function(email_system: EmailSystem, user: User):
    # Streamlined email sending to reduce redundancy
    emails = [
        "Hi", 
        "This is a test email.", 
        "Enjoy this beautiful day.", 
        "How are you?", 
        "Hope you're well.", 
        "See you soon.", 
        "Don't forget to reply!", 
        "Here's an image link.", 
        "Check out my latest project.", 
        "Let me know your thoughts."
    ]
    
    for email_content in emails:
        email_system.send_email(User("alice@example.com"), user, email_content)



if __name__ == '__main__':
    email_system = EmailSystem()
    
    # Create user instances
    alice = User("alice@example.com")
    jon = User("jon@example.com")

    alice.view_mailbox()
    email_system.send_email(alice, jon, "Hi!")
    email_system.send_email(jon, alice, "Hello!")
    
    print(email_system.get_mailbox(jon), "Jon's email")
    print(email_system.get_mailbox(alice), "Alice's email")
    print(email_system.track_email(alice, jon, "Hi!"))
    
    print("Alice's mailbox before:", len(alice.view_mailbox()))
    feature_envy_function(email_system, alice)
    print("Alice's mailbox after:", len(alice.view_mailbox()))

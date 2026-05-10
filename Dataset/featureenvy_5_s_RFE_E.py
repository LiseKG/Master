class User:
    def __init__(self, email_address: str):
        self.email_address = email_address
        self.email = []

    def view_mailbox(self):
        # Return a formatted string for each mail instead of printing during the view
        return "\n".join(f"From: {mail['from']}, To: {mail['to']}, Content: {mail['content']}" for mail in self.email)

    def add_mail(self, from_address: str, to_address: str, content: str):
        # Append mail directly, which is necessary for the User's mailbox
        self.email.append({"from": from_address, "to": to_address, "content": content})


class EmailSystem:
    def __init__(self):
        self.mailbox = []

    def send_email(self, sender: User, receiver: User, content: str):
        # Directly add mail to user's mailbox without excessive calls
        receiver.add_mail(sender.email_address, receiver.email_address, content)
        return f"Email sent to {receiver.email_address} with content: '{content}'"

    def get_mailbox(self, user: User):
        # Return user's mailbox without unnecessary computation
        return user.email

    def track_email(self, sender: User, receiver: User, content: str):
        # Return a status message indicating action instead of just a string
        return "Tracking: Email sent"


def send_multiple_emails(email_system: EmailSystem, sender: User, receiver: User, messages: list):
    # Send a batch of emails, reducing the overhead of multiple function calls
    for message in messages:
        email_system.send_email(sender, receiver, message)


def feature_envy_function(email_system: EmailSystem, user: User):
    sender = User("alice@example.com")
    messages = [
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
    send_multiple_emails(email_system, sender, user, messages)


if __name__ == '__main__':
    email_system = EmailSystem()
    
    # Create user instances
    alice = User("alice@example.com")
    jon = User("jon@example.com")

    print(alice.view_mailbox()) #Empty
    print(email_system.send_email(alice, jon, "Hi!"))
    print(email_system.send_email(jon, alice, "Hello!"))
    print(email_system.get_mailbox(jon), "Jon's email")
    print(email_system.get_mailbox(alice), "Alice's email")
    print(email_system.track_email(alice, jon, "Hi!"))
    print("Alice's mailbox before:", len(alice.email))
    feature_envy_function(email_system, alice)
    print("Alice's mailbox after:", len(alice.email))

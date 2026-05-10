class User:
    def __init__(self, email_address: str):
        self.email_address = email_address
        self.email = []

    def view_mailbox(self):
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


def send_multiple_emails(email_system: EmailSystem, sender: User, receiver: User, messages: list):
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

    
    alice.view_mailbox() #empty
    email_system.send_email(alice,jon,"Hi!")
    email_system.send_email(jon,alice,"Hello!")
    print(email_system.get_mailbox(jon),"Jons email")
    print(email_system.get_mailbox(alice),"Alice email")
    print(email_system.track_email(alice,jon,"Hi!"))
    print("alice mailbox before",len(alice.view_mailbox()))
    feature_envy_function(email_system,alice)
    print("alice mailbox after",len(alice.view_mailbox()))

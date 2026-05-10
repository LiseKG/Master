class User:
    def __init__(self, email_address: str):
        self.email_address = email_address
        self.emails = []

    def view_mailbox(self):
        return self.emails


class EmailSystem:
    def __init__(self):
        self.mailbox = []

    def send_email(self, sender: User, receiver: User, content: str):
        email_data = self.compose_email(sender, receiver, content)
        self.mailbox.append(email_data)
        self.track_email(sender, receiver, content)

    def compose_email(self, sender: User, receiver: User, content: str):
        return {
            'from': sender.email_address,
            'to': receiver.email_address,
            'content': content
        }

    def get_mailbox(self, user: User):
        return [email for email in self.mailbox if email['to'] == user.email_address]

    def track_email(self, sender: User, receiver: User, content: str):
        print(f'Tracked email from {sender.email_address} to {receiver.email_address}: {content}')

    def check_message(self, sender: User, receiver: User):
        return any(email['from'] == sender.email_address and 'hi' in email['content'] for email in self.get_mailbox(receiver))

    def show_mailbox(self, user: User):
        for email in self.get_mailbox(user):
            print(f"From: {email['from']} To: {email['to']} Content: {email['content']}")

    def send_welcome_email(self, user: User):
        self.send_email(User("admin@example.com"), user, "Welcome to the Email System!")

    def send_image_email(self, sender: User, receiver: User, image_path: str):
        self.send_email(sender, receiver, f"Here is an image: {image_path}")

    def count_emails(self, user: User):
        return len(self.get_mailbox(user))

    def delete_email(self, user: User, content: str):
        self.mailbox = [email for email in self.mailbox if not (email['to'] == user.email_address and email['content'] == content)]

    def search_in_mailbox(self, user: User, keyword: str):
        return [email for email in self.get_mailbox(user) if keyword in email['content']]

    def clear_mailbox(self, user: User):
        self.mailbox = [email for email in self.mailbox if email['to'] != user.email_address]

    def simulate_email_flow(self, user1: User, user2: User):
        self.send_email(user1, user2, "Hi")
        self.show_mailbox(user2)
        if self.check_message(user1, user2):
            print("Message found!")
        self.send_image_email(user1, user2, "image.png")

    def create_user(self, email_address: str):
        return User(email_address)

    def update_email_address(self, user: User, new_address: str):
        user.email_address = new_address

    def statistics(self):
        total_emails = len(self.mailbox)
        return f"Total emails sent: {total_emails}"

    def __str__(self):
        return f"Email System with {len(self.mailbox)} emails in the mailbox"


def test_email_system():
    email_system = EmailSystem()
    user1 = email_system.create_user("alice@example.com")
    user2 = email_system.create_user("bob@example.com")
    user3 = email_system.create_user("charlie@example.com")

    email_system.send_email(user1, user2, "hi Bob")
    email_system.show_mailbox(user2)
    email_system.check_message(user1, user2)
    
    email_system.send_welcome_email(user3)
    email_system.send_image_email(user1, user2, "image.png")

    email_system.count_emails(user2)
    email_system.search_in_mailbox(user2, "hi")
    email_system.send_email(user2, user3, "fwd hi bob!")
    email_system.send_email(user3, user1, "Hi Alice!")

    email_system.simulate_email_flow(user1, user2)
    email_system.update_email_address(user3, "new_charlie@example.com")
   
    print(email_system.mailbox)  # Changed to print the mailbox directly
    
    email_system.delete_email(user2, "hi Bob")
    email_system.clear_mailbox(user2)
    
    print(email_system.statistics())
    print(email_system)

    user1.view_mailbox()


if __name__ == "__main__":
    test_email_system()

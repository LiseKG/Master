class User:
    def __init__(self, email_address: str):
        self.email_address = email_address
        self.email = []

    def view_mailbox(self):
        return self.email


class EmailSystem:
    def __init__(self):
        self.mailbox = []

    def send_email(self, sender: User, receiver: User, content: str):
        email_data = {
            'from': sender.email_address,
            'to': receiver.email_address,
            'content': content
        }
        self.mailbox.append(email_data)
        self.track_email(sender, receiver, content)

    def get_mailbox(self, user: User):
        return [email for email in self.mailbox if email['to'] == user.email_address]

    def track_email(self, sender: User, receiver: User, content: str):
        print(f'Tracked email from {sender.email_address} to {receiver.email_address}: {content}')

    def check_message(self, sender: User, receiver: User):
        messages = self.get_mailbox(receiver)
        for email in messages:
            if email['from'] == sender.email_address and 'hi' in email['content']:
                return True
        return False

    def show_mailbox(self, user: User):
        mailbox_contents = self.get_mailbox(user)
        for email in mailbox_contents:
            print(f"From: {email['from']} To: {email['to']} Content: {email['content']}")

    def send_welcome_email(self, user: User):
        self.send_email(User("admin@example.com"), user, "Welcome to the Email System!")

    def send_image_email(self, sender: User, receiver: User, image_path: str):
        content = f"Here is an image: {image_path}"
        self.send_email(sender, receiver, content)

    def count_emails(self, user: User):
        return len(self.get_mailbox(user))

    def delete_email(self, user: User, content: str):
        self.mailbox = [email for email in self.mailbox if not (email['to'] == user.email_address and email['content'] == content)]

    def search_in_mailbox(self, user: User, keyword: str):
        mailbox_contents = self.get_mailbox(user)
        return [email for email in mailbox_contents if keyword in email['content']]

   
    def forward_email(self, user: User, original_sender: User, content: str, new_receiver: User):
        self.send_email(user, new_receiver, f"Fwd from {original_sender.email_address}: {content}")

    def reply_to_email(self, original_sender: User, user: User, reply_content: str):
        self.send_email(user, original_sender, reply_content)

    def simulate_email_flow(self, user1: User, user2: User):
        self.send_email(user1, user2, "Hi")
        self.show_mailbox(user2)
        self.check_message(user1, user2)
        self.send_image_email(user1, user2, "image.png")

    def create_user(self, email_address: str):
        return User(email_address)

    def update_email_address(self, user: User, new_address: str):
        user.email_address = new_address

    def list_all_mailboxes(self):
        return [user for user in self.mailbox]

    def clear_mailbox(self, user: User):
        self.mailbox = [email for email in self.mailbox if email['to'] != user.email_address]

    def statistics(self):
        total_emails = len(self.mailbox)
        return f"Total emails sent: {total_emails}"

    def str(self):
        return f"Email System with {len(self.mailbox)} emails in the mailbox"

def test_email_system():
    email_system = EmailSystem()

    # Create users (tests create_user)
    user1 = email_system.create_user("alice@example.com")
    user2 = email_system.create_user("bob@example.com")
    user3 = email_system.create_user("charlie@example.com")

    # Basic sending (tests send_email + track_email)
    email_system.send_email(user1, user2, "hi Bob")

    # Mailbox access (tests get_mailbox)
    email_system.get_mailbox(user2)

    # Check message (tests check_message)
    email_system.check_message(user1, user2)

    # Show mailbox (tests show_mailbox)
    email_system.show_mailbox(user2)

    # Send welcome email (internally tests send_email)
    email_system.send_welcome_email(user3)

    # Send image email (internally tests send_email)
    email_system.send_image_email(user1, user2, "image.png")

    # Count emails
    email_system.count_emails(user2)

    # Search mailbox
    email_system.search_in_mailbox(user2, "hi")


    # Forward email (internally tests send_email)
    email_system.forward_email(user2, user1, "hi Bob", user3)

    # Reply to email (internally tests send_email)
    email_system.reply_to_email(user1, user2, "Hello Alice")

    # Simulate full flow (internally tests multiple methods)
    email_system.simulate_email_flow(user1, user2)

    # Update email address
    email_system.update_email_address(user3, "new_charlie@example.com")

    # List all mailboxes
    email_system.list_all_mailboxes()

    # Delete specific email
    email_system.delete_email(user2, "hi Bob")

    # Clear mailbox
    email_system.clear_mailbox(user2)

    # Statistics
    email_system.statistics()

    # String representation
    email_system.str()

    # Test User method directly
    user1.view_mailbox()


if __name__ == "__main__":
    test_email_system()


# Simple Email Service

# Requirements:
# - Track emails (from, to, content)
# * Check that a mail from Alice, sent to Jon, contains a message saying hi
# - Show mailbox with new mails
# - Send a new emails to Jon saying Hello!
# - Send an email containing an image


class Email:
    def __init__(self, sender_address, receiver_address, subject, content):
        self.sender_address = sender_address
        self.receiver_address = receiver_address
        self.subject = subject
        self.content = content
        self.has_image = False
        self.read = False


class User:
    def __init__(self, email_address: str):
        self.email_address = email_address
        self.email = []
        self.pending_mail = None

    def view_mailbox(self):
        if not self.email:
            print(f"Mailbox for {self.email_address} is empty.")
        else:
            print(f"Mailbox for {self.email_address}:")
            for mail in self.email:
                status = "READ" if mail.read else "NEW"
                print(f"  [{status}] From: {mail.sender_address} | Subject: {mail.subject}")

    def add_mail(self):
        if self.pending_mail is not None:
            self.email.append(self.pending_mail)
            self.pending_mail = None


class EmailSystem:
    def __init__(self):
        self.mailbox = []
        self.users = {}
        self.event_log = []

    # Method 1
    def register_user(self, user: User):
        self.users[user.email_address] = user
        self.log_event(f"User '{user.email_address}' registered.")
        print(f"User '{user.email_address}' registered.")

    # Method 2
    def log_event(self, event: str):
        self.event_log.append(event)

    # Method 3
    def create_email(self, sender_address, receiver_address, subject, content):
        return Email(sender_address, receiver_address, subject, content)

    # Method 4
    def format_subject(self, subject):
        return subject.strip().title()

    # Method 5
    def deliver_email(self, receiver: User, mail: Email):
        receiver.pending_mail = mail
        receiver.add_mail()
        self.mailbox.append(mail)

    # Method 6
    def send_email(self, sender: User, receiver: User, content: str):
        subject = self.format_subject("new message")
        mail = self.create_email(sender.email_address, receiver.email_address, subject, content)
        self.deliver_email(receiver, mail)
        self.log_event(f"Email sent from {sender.email_address} to {receiver.email_address}")
        print(f"Email sent to {receiver.email_address} with content: {content}")
        return mail

    # Method 7
    def send_email_with_image(self, sender: User, receiver: User, content: str, image_name: str):
        mail = self.send_email(sender, receiver, content)
        mail.has_image = True
        self.log_event(f"Image '{image_name}' attached to email for {receiver.email_address}")
        print(f"Image '{image_name}' attached to email.")
        return mail

    # Method 8
    def get_mailbox(self, user: User):
        user.view_mailbox()
        return user.email

    # Method 9
    def get_unread_emails(self, user: User):
        return [mail for mail in user.email if not mail.read]

    # Method 10
    def show_new_emails(self, user: User):
        new_emails = self.get_unread_emails(user)
        print(f"{user.email_address} has {len(new_emails)} new email(s):")
        for mail in new_emails:
            print(f"  From: {mail.sender_address} | Subject: {mail.subject} | Content: {mail.content}")
        return new_emails

    # Method 11
    def mark_as_read(self, mail: Email):
        mail.read = True
        self.log_event(f"Email from {mail.sender_address} marked as read.")

    # Method 12
    def read_email(self, user: User, index: int):
        if index < 0 or index >= len(user.email):
            print("Email not found.")
            return None
        mail = user.email[index]
        self.mark_as_read(mail)
        print(f"Reading email from {mail.sender_address}: {mail.content}")
        return mail

    # Method 13
    def track_email(self, sender: User, receiver: User, content: str):
        for mail in self.mailbox:
            if (mail.sender_address == sender.email_address
                    and mail.receiver_address == receiver.email_address
                    and content in mail.content):
                return "received"
        return "sent"

    # Method 14
    def check_email_contains(self, sender: User, receiver: User, keyword: str):
        status = self.track_email(sender, receiver, keyword)
        if status == "received":
            print(f"Confirmed: email from {sender.email_address} to {receiver.email_address} contains '{keyword}'.")
            return True
        print(f"No matching email found containing '{keyword}'.")
        return False

    # Method 15
    def forward_email(self, original: Email, sender: User, new_receiver: User):
        forwarded_content = "FWD: " + original.content
        mail = self.send_email(sender, new_receiver, forwarded_content)
        self.log_event(f"Email forwarded to {new_receiver.email_address}")
        return mail

    # Method 16
    def delete_email(self, user: User, index: int):
        if index < 0 or index >= len(user.email):
            print("Email not found.")
            return
        removed = user.email.pop(index)
        self.log_event(f"Email from {removed.sender_address} deleted from {user.email_address}'s mailbox.")
        print(f"Email from {removed.sender_address} deleted.")

    # Method 17
    def send_bulk_emails(self, sender: User, receivers: list, content: str):
        for receiver in receivers:
            self.send_email(sender, receiver, content)
        self.log_event(f"Bulk email sent by {sender.email_address} to {len(receivers)} recipients.")
        print(f"Bulk email sent to {len(receivers)} recipient(s).")

    # Method 18
    def show_mailbox_summary(self, user: User):
        total = len(user.email)
        unread = len(self.get_unread_emails(user))
        print(f"Summary for {user.email_address}: {total} total, {unread} unread.")

    # Method 19
    def search_inbox(self, user: User, keyword: str):
        results = [mail for mail in user.email if keyword.lower() in mail.content.lower()]
        print(f"Search '{keyword}' in {user.email_address}'s inbox: {len(results)} found.")
        for mail in results:
            print(f"  From: {mail.sender_address} | Content: {mail.content}")
        return results

    # Method 20
    def show_event_log(self):
        print("Event log:")
        for entry in self.event_log:
            print(f"  {entry}")

    # Method 21
    def read_all_emails(self, user: User):
        unread = self.get_unread_emails(user)
        for mail in unread:
            self.mark_as_read(mail)
        print(f"Marked all {len(unread)} email(s) as read for {user.email_address}.")

    # Method 22
    def clear_mailbox(self, user: User):
        count = len(user.email)
        user.email = []
        self.log_event(f"Mailbox cleared for {user.email_address} ({count} emails removed).")
        print(f"Mailbox cleared for {user.email_address}.")


if __name__ == "__main__":
    system = EmailSystem()

    alice = User("alice@mail.com")
    jon = User("jon@mail.com")
    bob = User("bob@mail.com")

    # Method 1 - register_user (calls log_event)
    system.register_user(alice)
    system.register_user(jon)
    system.register_user(bob)

    # Method 6 - send_email (calls format_subject, create_email, deliver_email, log_event)
    system.send_email(alice, jon, "hi there!")
    system.send_email(jon, alice, "Hello back!")

    # Method 7 - send_email_with_image (calls send_email, log_event)
    system.send_email_with_image(alice, jon, "Check this out!", "photo.jpg")

    # Method 8 - get_mailbox (calls view_mailbox on User)
    system.get_mailbox(jon)

    # Method 13 - track_email
    status = system.track_email(alice, jon, "hi")
    print(f"Track status: {status}")

    # Method 14 - check_email_contains (calls track_email)
    system.check_email_contains(alice, jon, "hi")

    # Method 10 - show_new_emails (calls get_unread_emails)
    system.show_new_emails(jon)

    # Method 12 - read_email (calls mark_as_read which calls log_event)
    system.read_email(jon, 0)

    # Method 15 - forward_email (calls send_email, log_event)
    original = jon.email[0]
    system.forward_email(original, jon, bob)

    # Method 16 - delete_email (calls log_event)
    system.delete_email(jon, 0)

    # Method 17 - send_bulk_emails (calls send_email, log_event)
    system.send_bulk_emails(alice, [jon, bob], "Hello everyone!")

    # Method 18 - show_mailbox_summary (calls get_unread_emails)
    system.show_mailbox_summary(jon)
    system.show_mailbox_summary(bob)

    # Method 19 - search_inbox
    system.search_inbox(jon, "Hello")

    # Method 21 - read_all_emails (calls get_unread_emails, mark_as_read)
    system.read_all_emails(jon)

    # Method 22 - clear_mailbox (calls log_event)
    system.clear_mailbox(bob)

    # Method 20 - show_event_log
    system.show_event_log()

    # Method 9 - get_unread_emails (called by others but also directly)
    unread = system.get_unread_emails(alice)
    print(f"Alice unread count: {len(unread)}")

    # Method 11 - mark_as_read (called by others but also directly)
    if alice.email:
        system.mark_as_read(alice.email[0])

    # Methods 3 and 4 called via send_email above; call directly to ensure coverage
    mail = system.create_email("x@mail.com", "y@mail.com", "Test", "Test content")
    print(f"Created email subject: {system.format_subject('  test subject  ')}")
    print(f"Email has image: {mail.has_image}")

    # Method 5 - deliver_email (called via send_email above; call directly too)
    test_mail = system.create_email("a@mail.com", "b@mail.com", "Direct", "Direct delivery")
    system.deliver_email(jon, test_mail)
    print(f"Jon now has {len(jon.email)} email(s) after direct delivery.")




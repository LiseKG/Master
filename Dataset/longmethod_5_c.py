
# Simple Email Service

# Requirements:
# - Track emails (from, to, content)
# * Check that a mail from Alice, sent to Jon, contains a message saying hi
# - Show mailbox with new mails
# - Send a new emails to Jon saying Hello!
# - Send an email containing an image


class User:
    def __init__(self, email_address: str):
        self.email_address = email_address
        self.email = []

    def view_mailbox(self):
        print(f"Mailbox for {self.email_address}:")
        for mail in self.email:
            print(f"  From: {mail['from']} | Subject: {mail['content'][:20]}")

    def add_mail(self, mail: dict):
        self.email.append(mail)


class EmailSystem:
    def __init__(self):
        self.mailbox = []

    def send_email(self, sender: User, receiver: User, content: str):
        mail = {"from": sender.email_address, "to": receiver.email_address, "content": content}
        receiver.add_mail(mail)
        self.mailbox.append(mail)
        print(f"Email sent to {receiver.email_address} with content: {content}")

    def get_mailbox(self, user: User):
        user_mails = [m for m in self.mailbox if m["to"] == user.email_address]
        print(f"Mailbox for {user.email_address}: {len(user_mails)} email(s)")
        return user_mails

    def track_email(self, sender: User, receiver: User, content: str):
        for mail in self.mailbox:
            if mail["from"] == sender.email_address and mail["to"] == receiver.email_address and mail["content"] == content:
                print(f"Status: sent by {sender.email_address}, received by {receiver.email_address}")
                return "sent"
        print("Status: not found")
        return "not found"


def simulate_email_session(alice: User, jon: User, email_system: EmailSystem):
    content_0 = "Hi Jon, how are you?"
    content_1 = "Hello!"
    content_2 = "image:photo.png"
    content_3 = "Hi Alice, doing well!"
    content_4 = "Meeting at 3pm"
    content_5 = "image:diagram.png"
    content_6 = "Can we reschedule?"
    content_7 = "Sure, 4pm works"
    email_system.send_email(alice, jon, content_0)
    mailbox_jon_0 = email_system.get_mailbox(jon)
    email_system.send_email(alice, jon, content_1)
    mailbox_jon_1 = email_system.get_mailbox(jon)
    email_system.send_email(alice, jon, content_2)
    mailbox_jon_2 = email_system.get_mailbox(jon)
    email_system.send_email(jon, alice, content_3)
    mailbox_alice_0 = email_system.get_mailbox(alice)
    email_system.send_email(alice, jon, content_4)
    mailbox_jon_3 = email_system.get_mailbox(jon)
    email_system.send_email(jon, alice, content_5)
    mailbox_alice_1 = email_system.get_mailbox(alice)
    email_system.send_email(alice, jon, content_6)
    mailbox_jon_4 = email_system.get_mailbox(jon)
    email_system.send_email(jon, alice, content_7)
    mailbox_alice_2 = email_system.get_mailbox(alice)
    status_0 = email_system.track_email(alice, jon, content_0)
    status_1 = email_system.track_email(alice, jon, content_1)
    status_2 = email_system.track_email(alice, jon, content_2)
    status_3 = email_system.track_email(jon, alice, content_3)
    status_4 = email_system.track_email(alice, jon, content_4)
    status_5 = email_system.track_email(jon, alice, content_5)
    status_6 = email_system.track_email(alice, jon, content_6)
    status_7 = email_system.track_email(jon, alice, content_7)
    count_jon = len(mailbox_jon_4)
    count_alice = len(mailbox_alice_2)
    print(f"Jon received {count_jon} emails total")
    print(f"Alice received {count_alice} emails total")
    print(f"Track 0: {status_0}, Track 1: {status_1}, Track 2: {status_2}, Track 3: {status_3}")
    print(f"Track 4: {status_4}, Track 5: {status_5}, Track 6: {status_6}, Track 7: {status_7}")
    hi_found = any("hi" in m["content"].lower() for m in mailbox_jon_0)
    print(f"Jon received a 'hi' message from Alice: {hi_found}")
    jon.view_mailbox()
    alice.view_mailbox()
    jon_mails_mid = len(mailbox_jon_2)
    alice_mails_mid = len(mailbox_alice_1)
    print(f"Jon had {jon_mails_mid} emails after image, Alice had {alice_mails_mid} after image")
    delta_jon = count_jon - jon_mails_mid
    delta_alice = count_alice - alice_mails_mid
    print(f"Subsequent emails to Jon: {delta_jon}, to Alice: {delta_alice}")
    all_jon = [m["content"] for m in mailbox_jon_4]
    all_alice = [m["content"] for m in mailbox_alice_2]
    print(f"Jon's emails: {all_jon}")
    print(f"Alice's emails: {all_alice}")
    jon_has_image = any("image:" in c for c in all_jon)
    alice_has_image = any("image:" in c for c in all_alice)
    print(f"Jon received an image: {jon_has_image}")
    print(f"Alice received an image: {alice_has_image}")
    print(f"Jon emails after Hello: {len(mailbox_jon_1)}")
    print(f"Jon emails after reschedule: {len(mailbox_jon_3)}")
    print(f"Alice emails after first reply: {len(mailbox_alice_0)}")


if __name__ == "__main__":
    alice = User("alice@example.com")
    jon = User("jon@example.com")
    system = EmailSystem()

    system.send_email(alice, jon, "Hi Jon!")
    system.send_email(alice, jon, "Hello!")
    system.send_email(alice, jon, "image:photo.png")
    system.get_mailbox(jon)
    system.track_email(alice, jon, "Hi Jon!")
    jon.view_mailbox()
    alice.view_mailbox()

    simulate_email_session(alice, jon, system)

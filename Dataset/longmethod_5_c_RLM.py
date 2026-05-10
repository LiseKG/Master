
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
    exchanges = [
        (alice, jon, "Hi Jon, how are you?"), (alice, jon, "Hello!"),
        (alice, jon, "image:photo.png"),      (jon, alice, "Hi Alice, doing well!"),
        (alice, jon, "Meeting at 3pm"),        (jon, alice, "image:diagram.png"),
        (alice, jon, "Can we reschedule?"),    (jon, alice, "Sure, 4pm works"),
    ]
    snapshots = []
    for sender, receiver, content in exchanges:
        email_system.send_email(sender, receiver, content)
        snapshots.append(email_system.get_mailbox(receiver))

    statuses = [email_system.track_email(s, r, c) for s, r, c in exchanges]

    count_jon, count_alice = len(snapshots[6]), len(snapshots[7])
    print(f"Jon received {count_jon} emails total", f"Alice received {count_alice} emails total", sep="\n")
    print(f"Track 0: {statuses[0]}, Track 1: {statuses[1]}, Track 2: {statuses[2]}, Track 3: {statuses[3]}", f"Track 4: {statuses[4]}, Track 5: {statuses[5]}, Track 6: {statuses[6]}, Track 7: {statuses[7]}", sep="\n")
    print(f"Jon received a 'hi' message from Alice: {any('hi' in m['content'].lower() for m in snapshots[0])}")
    jon.view_mailbox()
    alice.view_mailbox()
    jon_mid, alice_mid = len(snapshots[2]), len(snapshots[5])
    print(f"Jon had {jon_mid} emails after image, Alice had {alice_mid} after image")
    print(f"Subsequent emails to Jon: {count_jon - jon_mid}, to Alice: {count_alice - alice_mid}")
    print(f"Jon's emails: {[m['content'] for m in snapshots[6]]}")
    print(f"Alice's emails: {[m['content'] for m in snapshots[7]]}")
    print(f"Jon received an image: {any('image:' in m['content'] for m in snapshots[6])}", f"Alice received an image: {any('image:' in m['content'] for m in snapshots[7])}", sep="\n")
    print(f"Jon emails after Hello: {len(snapshots[1])}")
    print(f"Jon emails after reschedule: {len(snapshots[4])}")
    print(f"Alice emails after first reply: {len(snapshots[3])}")


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

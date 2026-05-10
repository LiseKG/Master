
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
            print(f"  From: {mail['from']} | Content: {mail['content']}")

    def add_mail(self, mail):
        self.email.append(mail)


class EmailSystem:
    def __init__(self):
        self.mailbox = []

    def send_email(self, sender: User, receiver: User, content: str):
        mail = {"from": sender.email_address, "to": receiver.email_address, "content": content}
        receiver.add_mail(mail)
        self.mailbox.append(mail)
        return f"Email sent to {receiver.email_address} with content: {content}"

    def get_mailbox(self, user: User):
        return [mail for mail in self.mailbox if mail["to"] == user.email_address]

    def track_email(self, sender: User, receiver: User, content: str):
        for mail in self.mailbox:
            if mail["from"] == sender.email_address and mail["to"] == receiver.email_address and mail["content"] == content:
                return "sent" if mail["from"] == sender.email_address else "received"
        return "not found"


def generate_user_email_report(user):
    report = ""
    report += "Email Address: " + user.email_address + "\n"
    report += "Total emails: " + str(len(user.email)) + "\n"

    if len(user.email) == 0:
        report += user.email_address + " has no emails.\n"
    else:
        report += user.email_address + " has " + str(len(user.email)) + " email(s).\n"

    report += "Listing emails for " + user.email_address + ":\n"
    for mail in user.email:
        report += "  - From: " + mail["from"] + " | Content: " + mail["content"] + "\n"

    if user.email:
        report += "First email received by " + user.email_address + ": " + user.email[0]["content"] + "\n"
        report += "Last email received by " + user.email_address + ": " + user.email[-1]["content"] + "\n"

    report += "Summary for " + user.email_address + ": inbox size = " + str(len(user.email)) + "\n"

    return report


if __name__ == "__main__":
    alice = User("alice@mail.com")
    jon = User("jon@mail.com")
    system = EmailSystem()

    system.send_email(alice, jon, "hi")
    system.send_email(alice, jon, "Hello!")
    system.send_email(alice, jon, "[image attached]")

    print(system.track_email(alice, jon, "hi"))
    print(system.get_mailbox(jon))

    jon.view_mailbox()
    alice.view_mailbox()

    report = generate_user_email_report(jon)
    print(report)


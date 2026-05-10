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
        email = {
            "from": sender.email_address,
            "to": receiver.email_address,
            "content": content
        }
        self.mailbox.append(email)
        self.track_email(sender, receiver, content)

    def get_mailbox(self, user: User):
        return [email for email in self.mailbox if email["to"] == user.email_address]

    def track_email(self, sender: User, receiver: User, content: str):
        print(f"Email from {sender.email_address} to {receiver.email_address}: {content}")


def long_method_example(email_system: EmailSystem, user1: User, user2: User):
    email_system.send_email(user1, user2, "Hi Jon!")
    mailbox_contents = email_system.get_mailbox(user2)

    for email in mailbox_contents:
        if email["from"] == "alice@example.com" and email["to"] == "jon@example.com":
            print(f"Received email: {email['content']}")
            if "Hi" in email["content"]:
                print("This is a greeting email.")
            email_system.send_email(user2, user1, "Hello back!")
            
            # Eliminate unnecessary mailbox retrievals and repeated I/O
            reply_mailbox = email_system.get_mailbox(user1)
            for reply in reply_mailbox:
                print(f"{reply['from']} replied to you: {reply['content']}")
                if reply['content'] == "Hello back!":
                    print("You have a new message from Jon.")

            email_system.send_email(user1, user2, "Just checking in!")
            additional_email_contents = email_system.get_mailbox(user2)
            for additional_email in additional_email_contents:
                print(f"Jon received: {additional_email['content']}")
                if additional_email['content'] == "Just checking in!":
                    print("Jon is being messaged.")
                    email_system.send_email(user2, user1, "Thank you for checking in!")
                    followup_mailbox = email_system.get_mailbox(user1)
                    for followup in followup_mailbox:
                        print(f"Reply from Alice: {followup['content']}")
                        email_system.send_email(user1, user2, "Take care!")
                        final_email_contents = email_system.get_mailbox(user2)
                        for final_email in final_email_contents:
                            print(f"Final email to Jon: {final_email['content']}")
                            if final_email['content'] == "Take care!":
                                print("Communication cycle completed!")
                                email_system.send_email(user2, user1, "Bye!")
                                print("Jon said goodbye!")
                                email_system.send_email(user1, user2, "See you soon!")
                                print("Alice said see you soon!")
                                return  # Exit after the complete communication cycle


# Example of usage
if __name__ == '__main__':
    user = User("bob@online.no")
    user2 = User("centi@online.no")
    user.view_mailbox()
    es = EmailSystem()
    es.send_email(user,user2,"hi")
    es.get_mailbox(user2)
    es.track_email(user,user2,"hi")
    long_method_example(EmailSystem(),User("bobmail"),User("bobmail2"))
   

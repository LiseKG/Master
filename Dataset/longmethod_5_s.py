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
        user_emails = [email for email in self.mailbox if email["to"] == user.email_address]
        return user_emails

    def track_email(self, sender: User, receiver: User, content: str):
        print(f"Email from {sender.email_address} to {receiver.email_address}: {content}")


def long_method_example(email_system: EmailSystem, user1: User, user2: User):
    #1
    email_system.send_email(user1, user2, "Hi Jon!")
    #2
    mailbox_contents = email_system.get_mailbox(user2)
    #3
    for email in mailbox_contents:
        #4
        if email["from"] == "alice@example.com":
            #5
            if email["to"] == "jon@example.com":
                #6
                print(f"Received email: {email['content']}")
                #7
                if "Hi" in email["content"]:
                    #8
                    print("This is a greeting email.")
                #9
                email_system.send_email(user2, user1, "Hello back!")
                #10
                mailbox_contents = email_system.get_mailbox(user1)
                #11
                for reply in mailbox_contents:
                    #12
                    print(f"{reply['from']} replied to you: {reply['content']}")
                    #13
                    if reply['content'] == "Hello back!":
                        #14
                        print("You have a new message from Jon.")
                    #15
                    # Adding some redundancy
                    email_system.send_email(user1, user2, "Just checking in!")
                    #16
                    mailbox_contents = email_system.get_mailbox(user2)
                    #17
                    for additional_email in mailbox_contents:
                        #18
                        print(f"Jon received: {additional_email['content']}")
                        #19
                        if additional_email['content'] == "Just checking in!":
                            #20
                            print("Jon is being messaged.")
                            #21
                            email_system.send_email(user2, user1, "Thank you for checking in!")
                            #22
                            mailbox_contents = email_system.get_mailbox(user1)
                            #23
                            for followup in mailbox_contents:
                                #24
                                print(f"Reply from Alice: {followup['content']}")
                                #25
                                email_system.send_email(user1, user2, "Take care!")
                                #26
                                mailbox_contents = email_system.get_mailbox(user2)
                                #27
                                for final_email in mailbox_contents:
                                    #28
                                    print(f"Final email to Jon: {final_email['content']}")
                                    #29
                                    if final_email['content'] == "Take care!":
                                        #30
                                        print("Communication cycle completed!")
                                        #31
                                        email_system.send_email(user2, user1, "Bye!")
                                        #32
                                        print("Jon said goodbye!")
                                        #33
                                        email_system.send_email(user1, user2, "See you soon!")
                                        #34
                                        print("Alice said see you soon!")
                                        #35
                                        break  # Break to prevent infinite loop

# Example of usage
alice = User("alice@example.com")
jon = User("jon@example.com")
email_system = EmailSystem()

# Call the long method
if __name__ == '__main__':
    user = User("bob@online.no")
    user2 = User("centi@online.no")
    user.view_mailbox()
    es = EmailSystem()
    es.send_email(user,user2,"hi")
    es.get_mailbox(user2)
    es.track_email(user,user2,"hi")
    long_method_example(EmailSystem(),User("bobmail"),User("bobmail2"))
   

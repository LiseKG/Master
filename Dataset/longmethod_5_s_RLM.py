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
    email_system.send_email(user1, user2, "Hi Jon!")
    mailbox_contents = email_system.get_mailbox(user2)
    
    for email in mailbox_contents:
        if is_email_from_alice_to_jon(email):
            process_email_content(email, email_system, user1, user2)
            break  # Exit to prevent processing more than one email

def is_email_from_alice_to_jon(email):
    return email["from"] == "alice@example.com" and email["to"] == "jon@example.com"

def process_email_content(email, email_system, user1, user2):
    print(f"Received email: {email['content']}")
    if "Hi" in email["content"]:
        print("This is a greeting email.")
    
    email_system.send_email(user2, user1, "Hello back!")
    handle_replies(email_system, user1, user2)

def handle_replies(email_system, user1, user2):
    mailbox_contents = email_system.get_mailbox(user1)
    
    for reply in mailbox_contents:
        print(f"{reply['from']} replied to you: {reply['content']}")
        
        if reply['content'] == "Hello back!":
            print("You have a new message from Jon.")
        
        followup_communication(email_system, user1, user2)

def followup_communication(email_system, user1, user2):
    email_system.send_email(user1, user2, "Just checking in!")
    mailbox_contents = email_system.get_mailbox(user2)
    
    for additional_email in mailbox_contents:
        print(f"Jon received: {additional_email['content']}")
        
        if additional_email['content'] == "Just checking in!":
            print("Jon is being messaged.")
            email_system.send_email(user2, user1, "Thank you for checking in!")
            handle_final_replies(email_system, user1, user2)

def handle_final_replies(email_system, user1, user2):
    mailbox_contents = email_system.get_mailbox(user1)
    
    for followup in mailbox_contents:
        print(f"Reply from Alice: {followup['content']}")
        email_system.send_email(user1, user2, "Take care!")
        handle_final_messages(email_system,user1, user2)

def handle_final_messages(email_system, user1,user2):
    mailbox_contents = email_system.get_mailbox(user2)
    
    for final_email in mailbox_contents:
        print(f"Final email to Jon: {final_email['content']}")
        
        if final_email['content'] == "Take care!":
            print("Communication cycle completed!")
            email_system.send_email(user2, user1, "Bye!")
            print("Jon said goodbye!")
            email_system.send_email(user1, user2, "See you soon!")
            print("Alice said see you soon!")
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
   
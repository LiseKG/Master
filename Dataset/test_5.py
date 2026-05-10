import godclass_5_c as GodClass5S
import godclass_5_c_RGC as GodClass5SRCG

import longmethod_5_c as LongMethod5S
import longmethod_5_c_RLM as LongMethod5SRLM

import featureenvy_5_c as FeatureEnvy5S
import featureenvy_5_c_RFE as FeatureEnvy5SRFE


import featureenvy_5_s_E as E1
import longmethod_5_s_E as E2
import featureenvy_5_s_E as E3


def test_email_system(EmailSystemClass,UserClass):
    # Initialize the EmailSystem
    email_system = EmailSystemClass()
    
    # Create user instances
    alice = UserClass("alice@example.com")
    jon = UserClass("jon@example.com")

    # Test showing mailbox (should initially be empty)
    emails_jons_inbox = email_system.get_mailbox(jon)
    assert len(emails_jons_inbox) == 0, "Jon's mailbox should initially be empty"

    
    # Test sending an email from Alice to Jon saying Hi
    email_system.send_email(alice, jon, "Hi")

    for mail in email_system.mailbox:
        print(mail)
        if isinstance(mail,dict):
            print(mail)
            assert any(mail['content'] == "Hi" for mail in email_system.mailbox), f"Email from Alice to Jon saying 'Hi' not found"
        elif isinstance(mail,str):
            
            assert("Hi" in mail), f"Does not contain Hi in string!"
        else:
            print("not dict")
            print(mail.content)
         #   assert any( mail.content.str.contains("Hi!") for mail in email_system.mailbox), f"Class does not work"
            
    # Test sending a new email to Jon saying Hello!
    email_system.send_email(alice, jon, "Hello!")
    
    # Check that Jon's mailbox now contains the new email
    emails_jons_inbox = email_system.get_mailbox(jon)
    print(emails_jons_inbox)
    for mails in emails_jons_inbox:
       
        if isinstance(mails,dict):
            assert any(email['content'] == "Hello!" for email in emails_jons_inbox), "Jon's mailbox does not contain the email saying 'Hello!'"
        #elif isinstance(mail,str):
            #print(mail,"test")
           # assert any("Hello"  in mail for mail in emails_jons_inbox), f"Does not contain Hello in string!"
        #else:
          #  assert any(mail == "Hello!" for mail in emails_jons_inbox), f"Class does not work"
            

    # Test sending an email containing an image
    email_system.send_email(alice, jon, "<img src='image.png' />")
    
    # Check that Jon's mailbox contains the email with image
    emails_jons_inbox = email_system.get_mailbox(jon)
    print(emails_jons_inbox)
    for mails in emails_jons_inbox:
        mails
        # if isinstance(mails,dict):
        #     assert any("<img src='image.png' />" in email['content'] for email in emails_jons_inbox), "Jon's mailbox does not contain the email with the image"
        # elif isinstance(mail,str):
        #     print(mail,"test")
        #     assert any("<img src='image.png' />"  in mail for mail in emails_jons_inbox), f"Does not contain Hello in string!"
        # else:
        #     assert any("<img src='image.png' />" in ma[2] for ma in email_system.mailbox), "Jon's mailbox does not contain the email with the image"
# Loop through and run tests for each implementation
implementations = [
    ("GodClass5S", GodClass5S),
    # ("GodClass5SRCG", GodClass5SRCG),
    
     ("LongMethod5S", LongMethod5S),
     ("LongMethod5SRLM", LongMethod5SRLM),

     ("FeatureEnvy5S", FeatureEnvy5S),
    ("FeatureEnvy5SRFE", FeatureEnvy5SRFE),
    
      ("energy",E1),("energy",E2),("energy",E3)
]

for name, module in implementations:
    print(f"Testing {name}...")
    test_email_system(module.EmailSystem,module.User)
    print(f"Finished testing {name}.\n")

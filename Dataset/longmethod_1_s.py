from dataclasses import dataclass

@dataclass
class CardApplication:
    income: int


class CardApplicationResult:
    APPROVED = "APPROVED"
    DECLINED = "DECLINED"


class CardApplicationReviewer():
    """
    Contract for reviewing a card application.
    Business rules are not defined here.
    """

    def review(self, application: CardApplication) -> str:
        result = evaluate_application(application)
        return result


def evaluate_application(application: CardApplication) -> str:
    #1
    income = application.income
    #2
    if income > 1000:
        #3
        decision = CardApplicationResult.APPROVED
    else:
        #4
        decision = CardApplicationResult.DECLINED
    #5
    print(f"Income: {income}, Decision: {decision}")
    #6
    if income >= 0:
        #7
        print("Income is non-negative.")
    else:
        #8
        print("Income is negative.")
    #9
    if income > 500:
        #10
        print("Income is above 500.")
    #11
    if income > 800:
        #12
        print("Income is above 800.")
    #13
    if income > 1200:
        #14
        print("Income is above 1200.")
    #15
    if income > 1500:
        #16
        print("Income is above 1500.")
    #17
    if income > 2000:
        #18
        print("Income is above 2000.")
    #19
    if income > 3000:
        #20
        print("Income is above 3000.")
    #21
    print("Checking decision.")
    #22
    if decision == CardApplicationResult.APPROVED:
        #23
        print("Application approved.")
    #24
    else:
        #25
        print("Application declined.")
    #26
    print("Finalizing review.")
    #27
    print("Sending result to applicant.")
    #28
    return decision
    #29
    print("This statement will not execute.")  # Lines added for reaching over 35
    #30
    print("Unreachable line 1.")
    #31
    print("Unreachable line 2.")
    #32
    print("Unreachable line 3.")
    #33
    print("Unreachable line 4.")
    #34
    print("Unreachable line 5.")
    #35


if __name__ == '__main__':
    application = CardApplication(income=1200)
    reviewer = CardApplicationReviewer()
    result = reviewer.review(application)
    evaluate_application(CardApplication(income=800))
    print(f"Review result: {result}")

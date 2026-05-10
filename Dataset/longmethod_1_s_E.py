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
        return evaluate_application(application)


def evaluate_application(application: CardApplication) -> str:
    income = application.income

    if income > 1000:
        decision = CardApplicationResult.APPROVED
    else:
        decision = CardApplicationResult.DECLINED

    # Only log details that are useful, removing unnecessary print statements.
    print(f"Income: {income}, Decision: {decision}")
    
    # Print statements for income checks, but only if relevant.
    if income >= 0:
        print("Income is non-negative.")
    if income > 500:
        print("Income is above 500.")
    if income > 800:
        print("Income is above 800.")
    if income > 1200:
        print("Income is above 1200.")
    if income > 1500:
        print("Income is above 1500.")
    if income > 2000:
        print("Income is above 2000.")
    if income > 3000:
        print("Income is above 3000.")
    
    # Decision made, print result.
    print("Checking decision.")
    if decision == CardApplicationResult.APPROVED:
        print("Application approved.")
    else:
        print("Application declined.")

    print("Finalizing review.")
    print("Sending result to applicant.")
    
    return decision


if __name__ == '__main__':
    application = CardApplication(income=1200)
    reviewer = CardApplicationReviewer()
    result = reviewer.review(application)
    reviewer.review(CardApplication(income=800))
    print(f"Review result: {result}")

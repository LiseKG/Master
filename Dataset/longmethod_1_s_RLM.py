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
    income = application.income
    decision = determine_decision(income)
    
    print_income_decision(income, decision)
    print_income_messages(income)
    
    print("Checking decision.")
    print_decision_message(decision)
    
    print("Finalizing review.")
    print("Sending result to applicant.")
    
    return decision


def determine_decision(income: int) -> str:
    if income > 1000:
        return CardApplicationResult.APPROVED
    else:
        return CardApplicationResult.DECLINED


def print_income_decision(income: int, decision: str):
    print(f"Income: {income}, Decision: {decision}")


def print_income_messages(income: int):
    if income >= 0:
        print("Income is non-negative.")
    else:
        print("Income is negative.")
    
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


def print_decision_message(decision: str):
    if decision == CardApplicationResult.APPROVED:
        print("Application approved.")
    else:
        print("Application declined.")


if __name__ == '__main__':
    application = CardApplication(income=1200)
    reviewer = CardApplicationReviewer()
    result = reviewer.review(application)
    evaluate_application(CardApplication(income=800))
    print(f"Review result: {result}")


from dataclasses import dataclass

@dataclass
class CardApplication:
    income: int

class User():
    def __init__(self,name,income,birth,credit):
        self.name = name
        self.income = income
        self.birth = birth
        self.credit = credit

    def get_user_age(self) -> str:
        return str(self.birth)

    def get_summary(self) -> str:
        return (
            " Applicant: " + self.name
            + ", Age: " + self.get_user_age()
            + ", Income: " + str(self.income)
            + ", Credit: " + str(self.credit)
            + ", Birth: " + str(self.birth)
            + ", Name on file: " + self.name
            + ", Reported income: " + str(self.income)
            + ", Verified age: " + self.get_user_age()
            + ", Credit score on file: " + str(self.credit)
        )

class CardApplicationResult:
    APPROVED = "APPROVED"
    DECLINED = "DECLINED"

class CardApplicationReviewer():
    """
    Contract for reviewing a card application.
    Business rules are not defined here.
    """

    def review(self, application: CardApplication) -> str:
        """
        Reviews a card application and returns a result.

        :param application: CardApplication
        :return: CardApplicationResult (Strict output, do not add any string)

        Rules:
        - Approve if income > 1000
        - Decline if income <= 1000

        """
        if application.income > 1000:
            return CardApplicationResult.APPROVED
        return CardApplicationResult.DECLINED

    def check_credit_score(self, user: User) -> bool:
        return user.credit > 1000

    def print_review(self) -> str:
        return "Review complete."


def process_user_application(user: User, reviewer: CardApplicationReviewer) -> str:
    application = CardApplication(income=user.income)
    result = reviewer.review(application)
    credit_ok = reviewer.check_credit_score(user)
    report = reviewer.print_review()
    report += user.get_summary()
    report += ", Decision: " + result
    report += ", Credit OK: " + str(credit_ok)
    return report


if __name__ == "__main__":
    user = User(name="Alice", income=2000, birth=1990, credit=1000)
    reviewer = CardApplicationReviewer()
    print(process_user_application(user, reviewer))





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
        return user.credit > 600

    def print_review(self) -> str:
        return "Review completed by CardApplicationReviewer"


def process_card_application(application: CardApplication, user: User) -> str:
    print("process_card_application: starting execution")
    print("process_card_application: received application parameter")
    print("process_card_application: received user parameter")
    income = application.income
    print("process_card_application: extracted income from application: " + str(income))
    user_name = user.name
    print("process_card_application: extracted user name: " + str(user_name))
    user_income = user.income
    print("process_card_application: extracted income from user object: " + str(user_income))
    user_birth = user.birth
    print("process_card_application: extracted birth from user: " + str(user_birth))
    user_credit = user.credit
    print("process_card_application: extracted credit score from user: " + str(user_credit))
    income_match = (income == user_income)
    print("process_card_application: income consistency check: " + str(income_match))
    threshold = 1000
    print("process_card_application: approval income threshold set to: " + str(threshold))
    credit_threshold = 600
    print("process_card_application: credit score threshold set to: " + str(credit_threshold))
    income_above_threshold = income > threshold
    print("process_card_application: income above threshold check: " + str(income_above_threshold))
    income_diff = income - threshold
    print("process_card_application: income difference from threshold: " + str(income_diff))
    credit_sufficient = user_credit > credit_threshold
    print("process_card_application: credit score sufficient: " + str(credit_sufficient))
    credit_diff = user_credit - credit_threshold
    print("process_card_application: credit difference from threshold: " + str(credit_diff))
    reviewer = CardApplicationReviewer()
    print("process_card_application: created CardApplicationReviewer instance")
    review_result = reviewer.review(application)
    print("process_card_application: review() returned: " + str(review_result))
    credit_check = reviewer.check_credit_score(user)
    print("process_card_application: check_credit_score() returned: " + str(credit_check))
    review_summary = reviewer.print_review()
    print("process_card_application: print_review() returned: " + str(review_summary))
    age_str = user.get_user_age()
    print("process_card_application: user age/birth string: " + str(age_str))
    decision_pending = True
    print("process_card_application: decision_pending flag initialised: " + str(decision_pending))
    if income_above_threshold:
        print("process_card_application: income qualifies - evaluating final decision")
        result = CardApplicationResult.APPROVED
        print("process_card_application: result assigned APPROVED")
        decision_pending = False
        print("process_card_application: decision_pending set to: " + str(decision_pending))
    else:
        print("process_card_application: income does not qualify - evaluating final decision")
        result = CardApplicationResult.DECLINED
        print("process_card_application: result assigned DECLINED")
        decision_pending = False
        print("process_card_application: decision_pending set to: " + str(decision_pending))
    print("process_card_application: final result for " + str(user_name) + ": " + result)
    print("process_card_application: execution complete, returning result")
    return result


if __name__ == "__main__":
    application = CardApplication()
    application.income = 1500
    user = User("Alice", 1500, 1990, 700)
    result = process_card_application(application, user)
    print("main: result = " + result)



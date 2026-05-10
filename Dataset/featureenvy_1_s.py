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
        """
        Reviews a card application and returns a result.

        :param application: CardApplication
        :return: CardApplicationResult

        Rules:
        - Approve if income > 1000
        - Decline if income <= 1000

        """
        if application.income > 1000:
            return CardApplicationResult.APPROVED
        else:
            return CardApplicationResult.DECLINED


def evaluate_multiple_applications(applications):
    results = []
    for app in applications:
        reviewer = CardApplicationReviewer()
        review_result = reviewer.review(app)
        
        # Excessive use of CardApplication attributes
        result = {
            "income": app.income,
            "review_status": review_result,
            "is_approved": review_result == CardApplicationResult.APPROVED,
            "income_twice": app.income * 2,
            "income_plus_100": app.income + 100,
            "income_minus_100": app.income - 100,
            "income_is_high": app.income > 1500,
            "income_is_low": app.income < 500,
            "app_income": app.income,
            "application_status": "{}: {}".format(app.income, review_result),
            "application_income_check": app.income if app.income > 800 else 0
        }
        
        results.append(result)
    
    return results

if __name__ == '__main__':
    CA1200 = CardApplication(income=1200)
    CA800 = CardApplication(income=800)
    CR = CardApplicationReviewer()
    print(CR.review(CA1200))
    print(CR.review(CA800))
    print(evaluate_multiple_applications([CA1200,CA800]))



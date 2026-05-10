from dataclasses import dataclass


@dataclass
class CardApplication:
    income: int


class CardApplicationResult:
    APPROVED = "APPROVED"
    DECLINED = "DECLINED"


class IncomeValidator:
    @staticmethod
    def is_eligible(income: int) -> bool:
        return income > 1000

    @staticmethod
    def evaluate_income_category(income: int) -> str:
        if income < 500:
            return "Insufficient Income"
        elif 500 <= income <= 1000:
            return "Marginal Income"
        return "High Income"  # Simplified return


class CardApplicationLogger:
    @staticmethod
    def log(application: CardApplication, result: str):
        print(f"Application {result.lower()} for income: {application.income}")


class CardApplicationReviewer:
    """
    Contract for reviewing a card application.
    Business rules are defined here.
    """

    def __init__(self):
        self.total_applications_reviewed = 0

    def review(self, application: CardApplication) -> str:
        self.total_applications_reviewed += 1
        result = (CardApplicationResult.APPROVED 
                  if IncomeValidator.is_eligible(application.income) 
                  else CardApplicationResult.DECLINED)
        CardApplicationLogger.log(application, result)
        return result

    def review_multiple_applications(self, applications: list) -> dict:
        return {app.income: self.review(app) for app in applications}

    def handle_application_with_feedback(self, application: CardApplication) -> str:
        result = self.review(application)
        if result == CardApplicationResult.DECLINED:
            print("Application declined due to insufficient income.")
        return result

    def assess_applications_on_criteria(self, applications: list) -> dict:
        return {app.income: IncomeValidator.evaluate_income_category(app.income) for app in applications}

    def summarize_review_outcomes(self, applications: list):
        summary = self.review_multiple_applications(applications)
        for income, result in summary.items():
            print(f"Income: {income}, Result: {result}")

    def reset_application_count(self):
        self.total_applications_reviewed = 0

    def get_review_count(self) -> int:
        return self.total_applications_reviewed

    def get_total_applications_processed(self) -> str:
        return f"Total applications reviewed: {self.get_review_count()}"

    def close_application_reviews(self):
        self.reset_application_count()
        print("Application reviews closed.")


if __name__ == '__main__':
    CA1200 = CardApplication(income=1200)
    CA800 = CardApplication(income=800)
    CR = CardApplicationReviewer()

    print(CR.review(CA1200))
    print(CR.review(CA800))
    CR.review_multiple_applications((CA1200, CA800))
    CR.reset_application_count()
    CR.handle_application_with_feedback(CA1200)

    report = CR.assess_applications_on_criteria((CA1200, CA800))
    CardApplicationLogger.log(CA1200,"approved")
    print(CR.get_total_applications_processed())
    CR.review(CA800)
    CR.assess_applications_on_criteria([CA800])
    CR.summarize_review_outcomes((CA1200, CA800))
    print(CR.get_total_applications_processed())
    CR.close_application_reviews()

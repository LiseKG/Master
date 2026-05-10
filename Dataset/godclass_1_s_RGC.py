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
        else:
            return "High Income"


class CardApplicationLogger:
    @staticmethod
    def log_approval(income: int):
        print(f"Application approved for income: {income}")

    @staticmethod
    def log_decline(income: int):
        print(f"Application declined for income: {income}")

    @staticmethod
    def print_review_summary(results: dict):
        for income, result in results.items():
            print(f"Income: {income}, Result: {result}")

    @staticmethod
    def generate_application_report(report: dict):
        for income, outcome in report.items():
            print(f"Income: {income} - Assessment: {outcome}")


class CardApplicationReviewer:
    """
    Contract for reviewing a card application.
    Business rules are defined here.
    """

    def __init__(self):
        self.total_applications_reviewed = 0

    def review(self, application: CardApplication) -> str:
        self.total_applications_reviewed += 1
        if IncomeValidator.is_eligible(application.income):
            return self.approve_application(application.income)
        else:
            return self.decline_application(application.income)

    def approve_application(self, income: int) -> str:
        CardApplicationLogger.log_approval(income)
        return CardApplicationResult.APPROVED

    def decline_application(self, income: int) -> str:
        CardApplicationLogger.log_decline(income)
        return CardApplicationResult.DECLINED

    def review_multiple_applications(self, applications: list) -> dict:
        results = {}
        for app in applications:
            results[app.income] = self.review(app)
        return results

    def handle_application_with_feedback(self, application: CardApplication) -> str:
        result = self.review(application)
        if result == CardApplicationResult.DECLINED:
            self.provide_feedback(application)
        return result

    def provide_feedback(self, application: CardApplication):
        print("Application declined due to insufficient income.")

    def assess_applications_on_criteria(self, applications: list) -> dict:
        criteria_results = {}
        for app in applications:
            criteria_results[app.income] = IncomeValidator.evaluate_income_category(app.income)
        return criteria_results

    def summarize_review_outcomes(self, applications: list):
        summary = self.review_multiple_applications(applications)
        CardApplicationLogger.print_review_summary(summary)

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
    CardApplicationLogger.generate_application_report(report)
    print(CR.get_total_applications_processed())
    CR.review(CA1200) #Get application status
    CR.assess_applications_on_criteria([CA1200]) #income and assesment
    CR.summarize_review_outcomes((CA1200, CA800))
    CR.close_application_reviews()

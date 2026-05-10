from dataclasses import dataclass



class CardApplicationReviewer:
    """
    A 'God Class' that centralizes the processing, reviewing, and decision-making
    for card applications based on various criteria.
    """

    def __init__(self):
        self.total_applications_reviewed = 0

    def review(self, application: CardApplication) -> str:
        self.total_applications_reviewed += 1
        if self.is_application_eligible(application):
            return self.approve_application(application)
        else:
            return self.decline_application(application)

    def is_application_eligible(self, application: CardApplication) -> bool:
        return application.income > 1000

    def approve_application(self, application: CardApplication) -> str:
        self.log_approval(application)
        return CardApplicationResult.APPROVED

    def decline_application(self, application: CardApplication) -> str:
        self.log_decline(application)
        return CardApplicationResult.DECLINED

    def log_approval(self, application: CardApplication):
        print(f"Application approved for income: {application.income}")

    def log_decline(self, application: CardApplication):
        print(f"Application declined for income: {application.income}")

    def review_multiple_applications(self, applications: list) -> dict:
        results = {}
        for app in applications:
            results[app.income] = self.review(app)
        return results

    def print_review_summary(self, results: dict):
        for income, result in results.items():
            print(f"Income: {income}, Result: {result}")

    def reset_application_count(self):
        self.total_applications_reviewed = 0

    def get_review_count(self) -> int:
        return self.total_applications_reviewed

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
            criteria_results[app.income] = self.evaluate_criteria(app)
        return criteria_results

    def evaluate_criteria(self, application: CardApplication) -> str:
        if application.income < 500:
            return "Insufficient Income"
        elif 500 <= application.income <= 1000:
            return "Marginal Income"
        else:
            return "High Income"

    def generate_application_report(self, applications: list):
        report = self.assess_applications_on_criteria(applications)
        for income, outcome in report.items():
            print(f"Income: {income} - Assessment: {outcome}")

    def get_total_applications_processed(self) -> str:
        return f"Total applications reviewed: {self.get_review_count()}"

    def get_application_status(self, application: CardApplication) -> str:
        return self.review(application)

    def validate_income_against_threshold(self, income: int, threshold: int) -> bool:
        return income > threshold

    def perform_income_analysis(self, applications: list) -> dict:
        analysis = {}
        for app in applications:
            analysis[app.income] = self.validate_income_against_threshold(app.income, 1000)
        return analysis

    def process_application_with_assessment(self, application: CardApplication) -> str:
        if self.evaluate_criteria(application) == "High Income":
            return self.approve_application(application)
        else:
            return self.decline_application(application)

    def summarize_review_outcomes(self, applications: list):
        summary = self.review_multiple_applications(applications)
        self.print_review_summary(summary)

    def close_application_reviews(self):
        self.reset_application_count()
        print("Application reviews closed.")


@dataclass
class CardApplication:
    income: int


class CardApplicationResult:
    APPROVED = "APPROVED"
    DECLINED = "DECLINED"


if __name__ == '__main__':
    CA1200 = CardApplication(income=1200)
    CA800 = CardApplication(income=800)
    CR = CardApplicationReviewer()
    print(CR.review(CA1200))
    print(CR.review(CA800))

    CR.review_multiple_applications((CA1200,CA800))
    CR.reset_application_count()
    CR.handle_application_with_feedback(CA1200)

    CR.generate_application_report((CA1200,CA800))
    
    CR.get_total_applications_processed()
    CR.get_application_status(CA800)
    CR.perform_income_analysis((CA1200,CA800))
    CR.process_application_with_assessment(CA1200)
    CR.summarize_review_outcomes((CA1200,CA800))
    CR.close_application_reviews()







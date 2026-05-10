class CardApplication:
    def __init__(self, income):
        self.income = income

    def check_income(self) -> bool:
        """Returns True if income is above the approval threshold of 1000."""
        return self.income > 1000

    def assess_debt_ratio(self) -> bool:
        """Returns True if the estimated debt-to-income ratio is below 40 percent."""
        if self.income == 0:
            return False
        debt_estimate = self.income * 0.2
        return (debt_estimate / self.income) < 0.4

    def calculate_credit_limit(self) -> float:
        """Returns a proposed credit limit as 30 percent of income."""
        return self.income * 0.3

    def score_application(self) -> int:
        """Computes and returns an overall risk score out of 100."""
        score = 0
        if self.check_income():
            score += 50
        if self.assess_debt_ratio():
            score += 30
        if self.income > 500:
            score += 20
        return score


class User:
    def __init__(self, name, income, birth, credit):
        self.name = name
        self.income = income
        self.birth = birth
        self.credit = credit

    def get_user_age(self) -> str:
        return str(self.birth)

    def assess_age_eligibility(self) -> bool:
        """Returns True if the user's birth year indicates they are at least 18 years old."""
        return (2024 - self.birth) >= 18


class CardApplicationResult:
    APPROVED = "APPROVED"
    DECLINED = "DECLINED"


class ApplicationLogger:
    def __init__(self):
        self.review_log = []
        self.reviewed_count = 0
        self.approved_count = 0
        self.declined_count = 0

    def log_result(self, result: str) -> None:
        """Appends a numbered result entry to the internal review log."""
        entry = "Review #" + str(self.reviewed_count) + ": " + result
        self.review_log.append(entry)

    def get_approval_rate(self) -> float:
        """Calculates and returns the current approval rate as a percentage."""
        if self.reviewed_count == 0:
            return 0.0
        return (self.approved_count / self.reviewed_count) * 100

    def get_statistics(self) -> dict:
        """Returns a dictionary with total reviewed, approved, declined, and approval rate."""
        return {
            "total_reviewed": self.reviewed_count,
            "approved": self.approved_count,
            "declined": self.declined_count,
            "approval_rate_pct": self.get_approval_rate(),
        }

    def reset_statistics(self) -> None:
        """Resets all counters and clears the review log back to an empty state."""
        self.reviewed_count = 0
        self.approved_count = 0
        self.declined_count = 0
        self.review_log.clear()


class ApplicationRiskAssessor:
    def classify_risk(self, application: CardApplication) -> str:
        """Classifies the application as LOW_RISK, MEDIUM_RISK, or HIGH_RISK based on score."""
        score = application.score_application()
        if score >= 80:
            return "LOW_RISK"
        if score >= 50:
            return "MEDIUM_RISK"
        return "HIGH_RISK"

    def recommend_card_tier(self, application: CardApplication) -> str:
        """Recommends a card tier of Platinum, Gold, or Standard based on risk."""
        risk = self.classify_risk(application)
        if risk == "LOW_RISK":
            return "Platinum"
        if risk == "MEDIUM_RISK":
            return "Gold"
        return "Standard"

    def is_borderline(self, application: CardApplication) -> bool:
        """Returns True if the application score falls in the borderline range of 50 to 69."""
        score = application.score_application()
        return 50 <= score < 70

    def flag_for_manual_review(self, application: CardApplication) -> str:
        """Returns MANUAL_REVIEW_REQUIRED for borderline cases, otherwise AUTO_PROCESS."""
        if self.is_borderline(application):
            return "MANUAL_REVIEW_REQUIRED"
        return "AUTO_PROCESS"


class ApplicationReportBuilder:
    def __init__(self, reviewer, risk_assessor: ApplicationRiskAssessor):
        self.reviewer = reviewer
        self.risk_assessor = risk_assessor

    def summarise_applicant(self, user: User) -> str:
        """Returns a formatted string summarising the applicant's key personal details."""
        age_eligible = user.assess_age_eligibility()
        credit_ok = self.reviewer.check_credit_score(user)
        return (
            "Name: " + user.name
            + " | Birth year: " + str(user.birth)
            + " | Age eligible: " + str(age_eligible)
            + " | Credit ok: " + str(credit_ok)
        )

    def full_review(self, user: User, application: CardApplication) -> dict:
        """Performs a complete review and returns a summary dictionary of all key details."""
        decision = self.reviewer.review(application)
        return {
            "applicant": user.name,
            "decision": decision,
            "credit_ok": self.reviewer.check_credit_score(user),
            "risk_tier": self.risk_assessor.classify_risk(application),
            "card_tier": self.risk_assessor.recommend_card_tier(application),
            "credit_limit": application.calculate_credit_limit(),
            "score": application.score_application(),
        }

    def batch_review(self, applications: list) -> list:
        """Reviews a list of (User, CardApplication) pairs and returns a list of decisions."""
        results = []
        for user, application in applications:
            outcome = self.full_review(user, application)
            results.append(outcome["decision"])
        return results

    def generate_report(self, user: User, application: CardApplication) -> str:
        """Generates a human-readable report string covering all key review details."""
        details = self.full_review(user, application)
        flag = self.risk_assessor.flag_for_manual_review(application)
        applicant_summary = self.summarise_applicant(user)
        lines = [
            "=== Application Report ===",
            applicant_summary,
            "Decision     : " + details["decision"],
            "Risk Tier    : " + details["risk_tier"],
            "Card Tier    : " + details["card_tier"],
            "Credit Limit : " + str(round(details["credit_limit"], 2)),
            "Score        : " + str(details["score"]) + "/100",
            "Flag         : " + flag,
            "Latest Log   : " + self.reviewer.print_review(),
        ]
        return "\n".join(lines)


class CardApplicationReviewer:
    """
    Contract for reviewing a card application.
    Business rules are not defined here.
    """

    def __init__(self, logger=ApplicationLogger()):
        self.logger = logger

    def review(self, application: CardApplication) -> str:
        """
        Reviews a card application and returns a result.

        :param application: CardApplication
        :return: CardApplicationResult (Strict output, do not add any string)

        Rules:
        - Approve if income > 1000
        - Decline if income <= 1000
        """
        self.logger.reviewed_count += 1
        if application.check_income():
            self.logger.approved_count += 1
            result = CardApplicationResult.APPROVED
        else:
            self.logger.declined_count += 1
            result = CardApplicationResult.DECLINED
        self.logger.log_result(result)
        return result

    def check_credit_score(self, user: User) -> bool:
        """Returns True if the user's credit score meets the minimum threshold of 600."""
        return user.credit >= 600

    def print_review(self) -> str:
        """Returns the most recent log entry, or a default message if none exist."""
        if not self.logger.review_log:
            return "No reviews recorded."
        return self.logger.review_log[-1]


# ── Main call ──────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    logger = ApplicationLogger()
    reviewer = CardApplicationReviewer(logger)
    risk_assessor = ApplicationRiskAssessor()
    report_builder = ApplicationReportBuilder(reviewer, risk_assessor)

    user1 = User(name="Alice", income=3000, birth=1990, credit=720)
    app1 = CardApplication(income=3000)

    user2 = User(name="Bob", income=800, birth=2005, credit=450)
    app2 = CardApplication(income=800)

    user3 = User(name="Carol", income=1200, birth=1985, credit=610)
    app3 = CardApplication(income=1200)

    # review
    print("Review app1:", reviewer.review(app1))

    # check_credit_score
    print("Credit ok user2:", reviewer.check_credit_score(user2))

    # print_review
    print("Latest log:", reviewer.print_review())

    # check_income
    print("Income ok app2:", app2.check_income())

    # log_result
    logger.log_result("MANUAL_ENTRY")
    print("Manual log entry:", reviewer.print_review())

    # get_approval_rate
    print("Approval rate:", logger.get_approval_rate(), "%")

    # assess_debt_ratio
    print("Debt ratio ok app1:", app1.assess_debt_ratio())

    # assess_age_eligibility
    print("Age eligible user2:", user2.assess_age_eligibility())

    # calculate_credit_limit
    print("Credit limit app1:", app1.calculate_credit_limit())

    # score_application
    print("Score app1:", app1.score_application())

    # classify_risk
    print("Risk app2:", risk_assessor.classify_risk(app2))

    # recommend_card_tier
    print("Card tier app1:", risk_assessor.recommend_card_tier(app1))

    # full_review
    print("Full review app3:", report_builder.full_review(user3, app3))

    # batch_review
    batch = report_builder.batch_review([(user1, app1), (user2, app2), (user3, app3)])
    print("Batch decisions:", batch)

    # get_statistics
    print("Statistics:", logger.get_statistics())

    # reset_statistics
    logger.reset_statistics()
    print("After reset:", logger.get_statistics())

    # is_borderline
    print("Is borderline app3:", risk_assessor.is_borderline(app3))

    # flag_for_manual_review
    print("Flag app3:", risk_assessor.flag_for_manual_review(app3))

    # summarise_applicant
    print("Applicant summary:", report_builder.summarise_applicant(user1))

    # generate_report
    reviewer.review(app1)
    print(report_builder.generate_report(user1, app1))

    # get_user_age
    print("User1 birth year:", user1.get_user_age())

class CardApplication:
    def __init__(self, income):
        self.income = income


class User:
    def __init__(self, name, income, birth, credit):
        self.name = name
        self.income = income
        self.birth = birth
        self.credit = credit

    def get_user_age(self) -> str:
        return str(self.birth)


class CardApplicationResult:
    APPROVED = "APPROVED"
    DECLINED = "DECLINED"


class CardApplicationReviewer:
    """
    Contract for reviewing a card application.
    Business rules are not defined here.

    God class: centralizes all decision-making for card application processing,
    acting as the single controller surrounded by data classes.
    """

    def __init__(self):
        self.review_log = []
        self.reviewed_count = 0
        self.approved_count = 0
        self.declined_count = 0

    # Method 1
    def review(self, application: CardApplication) -> str:
        """
        Reviews a card application and returns a result.

        :param application: CardApplication
        :return: CardApplicationResult (Strict output, do not add any string)

        Rules:
        - Approve if income > 1000
        - Decline if income <= 1000
        """
        self.reviewed_count += 1
        if self.check_income(application):
            self.approved_count += 1
            result = CardApplicationResult.APPROVED
        else:
            self.declined_count += 1
            result = CardApplicationResult.DECLINED
        self.log_result(result)
        return result

    # Method 2
    def check_credit_score(self, user: User) -> bool:
        """Returns True if the user's credit score meets the minimum threshold of 600."""
        return user.credit >= 600

    # Method 3
    def print_review(self) -> str:
        """Returns the most recent log entry, or a default message if none exist."""
        if not self.review_log:
            return "No reviews recorded."
        return self.review_log[-1]

    # Method 4
    def check_income(self, application: CardApplication) -> bool:
        """Returns True if the application income is above the approval threshold of 1000."""
        return application.income > 1000

    # Method 5
    def log_result(self, result: str) -> None:
        """Appends a numbered result entry to the internal review log."""
        entry = "Review #" + str(self.reviewed_count) + ": " + result
        self.review_log.append(entry)

    # Method 6
    def get_approval_rate(self) -> float:
        """Calculates and returns the current approval rate as a percentage."""
        if self.reviewed_count == 0:
            return 0.0
        return (self.approved_count / self.reviewed_count) * 100

    # Method 7
    def assess_debt_ratio(self, application: CardApplication) -> bool:
        """Returns True if the debt-to-income ratio is acceptable (below 40 percent)."""
        if application.income == 0:
            return False
        debt_estimate = application.income * 0.2
        return (debt_estimate / application.income) < 0.4

    # Method 8
    def assess_age_eligibility(self, user: User) -> bool:
        """Returns True if the user's birth year indicates they are at least 18 years old."""
        return (2024 - user.birth) >= 18

    # Method 9
    def calculate_credit_limit(self, application: CardApplication) -> float:
        """Calculates and returns a proposed credit limit as 30 percent of income."""
        return application.income * 0.3

    # Method 10
    def score_application(self, application: CardApplication) -> int:
        """Computes and returns an overall risk score for the application out of 100."""
        score = 0
        if self.check_income(application):
            score += 50
        if self.assess_debt_ratio(application):
            score += 30
        if application.income > 500:
            score += 20
        return score

    # Method 11
    def classify_risk(self, application: CardApplication) -> str:
        """Classifies the application as LOW_RISK, MEDIUM_RISK, or HIGH_RISK based on score."""
        score = self.score_application(application)
        if score >= 80:
            return "LOW_RISK"
        if score >= 50:
            return "MEDIUM_RISK"
        return "HIGH_RISK"

    # Method 12
    def recommend_card_tier(self, application: CardApplication) -> str:
        """Recommends a card tier of Platinum, Gold, or Standard based on risk classification."""
        risk = self.classify_risk(application)
        if risk == "LOW_RISK":
            return "Platinum"
        if risk == "MEDIUM_RISK":
            return "Gold"
        return "Standard"

    # Method 13
    def full_review(self, user: User, application: CardApplication) -> dict:
        """Performs a complete review and returns a summary dictionary of all key details."""
        decision = self.review(application)
        return {
            "applicant": user.name,
            "decision": decision,
            "credit_ok": self.check_credit_score(user),
            "risk_tier": self.classify_risk(application),
            "card_tier": self.recommend_card_tier(application),
            "credit_limit": self.calculate_credit_limit(application),
            "score": self.score_application(application),
        }

    # Method 14
    def batch_review(self, applications: list) -> list:
        """Reviews a list of (User, CardApplication) pairs and returns a list of decisions."""
        results = []
        for user, application in applications:
            outcome = self.full_review(user, application)
            results.append(outcome["decision"])
        return results

    # Method 15
    def get_statistics(self) -> dict:
        """Returns a dictionary with total reviewed, approved, declined, and approval rate."""
        return {
            "total_reviewed": self.reviewed_count,
            "approved": self.approved_count,
            "declined": self.declined_count,
            "approval_rate_pct": self.get_approval_rate(),
        }

    # Method 16
    def reset_statistics(self) -> None:
        """Resets all counters and clears the review log back to an empty state."""
        self.reviewed_count = 0
        self.approved_count = 0
        self.declined_count = 0
        self.review_log.clear()

    # Method 17
    def is_borderline(self, application: CardApplication) -> bool:
        """Returns True if the application score falls in the borderline range of 50 to 69."""
        score = self.score_application(application)
        return 50 <= score < 70

    # Method 18
    def flag_for_manual_review(self, application: CardApplication) -> str:
        """Returns MANUAL_REVIEW_REQUIRED for borderline cases, otherwise AUTO_PROCESS."""
        if self.is_borderline(application):
            return "MANUAL_REVIEW_REQUIRED"
        return "AUTO_PROCESS"

    # Method 19
    def summarise_applicant(self, user: User) -> str:
        """Returns a formatted string summarising the applicant's key personal details."""
        age_eligible = self.assess_age_eligibility(user)
        credit_ok = self.check_credit_score(user)
        return (
            "Name: " + user.name
            + " | Birth year: " + str(user.birth)
            + " | Age eligible: " + str(age_eligible)
            + " | Credit ok: " + str(credit_ok)
        )

    # Method 20
    def generate_report(self, user: User, application: CardApplication) -> str:
        """Generates a human-readable report string covering all key review details."""
        details = self.full_review(user, application)
        flag = self.flag_for_manual_review(application)
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
            "Latest Log   : " + self.print_review(),
        ]
        return "\n".join(lines)


# ── Main call ──────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    reviewer = CardApplicationReviewer()

    user1 = User(name="Alice", income=3000, birth=1990, credit=720)
    app1 = CardApplication(income=3000)

    user2 = User(name="Bob", income=800, birth=2005, credit=450)
    app2 = CardApplication(income=800)

    user3 = User(name="Carol", income=1200, birth=1985, credit=610)
    app3 = CardApplication(income=1200)

    # Method 1 – review
    print("Review app1:", reviewer.review(app1))

    # Method 2 – check_credit_score
    print("Credit ok user2:", reviewer.check_credit_score(user2))

    # Method 3 – print_review
    print("Latest log:", reviewer.print_review())

    # Method 4 – check_income (also called internally by review and score_application)
    print("Income ok app2:", reviewer.check_income(app2))

    # Method 5 – log_result (also called internally by review)
    reviewer.log_result("MANUAL_ENTRY")
    print("Manual log entry:", reviewer.print_review())

    # Method 6 – get_approval_rate (also called internally by get_statistics)
    print("Approval rate:", reviewer.get_approval_rate(), "%")

    # Method 7 – assess_debt_ratio (also called internally by score_application)
    print("Debt ratio ok app1:", reviewer.assess_debt_ratio(app1))

    # Method 8 – assess_age_eligibility (also called internally by summarise_applicant)
    print("Age eligible user2:", reviewer.assess_age_eligibility(user2))

    # Method 9 – calculate_credit_limit (also called internally by full_review)
    print("Credit limit app1:", reviewer.calculate_credit_limit(app1))

    # Method 10 – score_application (also called internally by classify_risk)
    print("Score app1:", reviewer.score_application(app1))

    # Method 11 – classify_risk (also called internally by recommend_card_tier and full_review)
    print("Risk app2:", reviewer.classify_risk(app2))

    # Method 12 – recommend_card_tier (also called internally by full_review)
    print("Card tier app1:", reviewer.recommend_card_tier(app1))

    # Method 13 – full_review (also called internally by batch_review and generate_report)
    print("Full review app3:", reviewer.full_review(user3, app3))

    # Method 14 – batch_review
    batch = reviewer.batch_review([(user1, app1), (user2, app2), (user3, app3)])
    print("Batch decisions:", batch)

    # Method 15 – get_statistics
    print("Statistics:", reviewer.get_statistics())

    # Method 16 – reset_statistics
    reviewer.reset_statistics()
    print("After reset:", reviewer.get_statistics())

    # Method 17 – is_borderline (also called internally by flag_for_manual_review)
    print("Is borderline app3:", reviewer.is_borderline(app3))

    # Method 18 – flag_for_manual_review (also called internally by generate_report)
    print("Flag app3:", reviewer.flag_for_manual_review(app3))

    # Method 19 – summarise_applicant (also called internally by generate_report)
    print("Applicant summary:", reviewer.summarise_applicant(user1))

    # Method 20 – generate_report
    reviewer.review(app1)
    print(reviewer.generate_report(user1, app1))

    # User.get_user_age called at least once
    print("User1 birth year:", user1.get_user_age())

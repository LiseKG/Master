import unittest
from godclass_1_c import CardApplicationReviewer as Reviewer1
#from godclass_1_c_RGC import CardApplicationReviewer as Reviewer2
from godclass_1_s_RGC_E import CardApplicationReviewer as Reviewer7
from godclass_1_s_RGC import CardApplicationReviewer as R8
from godclass_1_s_E import CardApplicationReviewer as E1


from longmethod_1_c import CardApplicationReviewer as Reviewer3
from longmethod_1_c_RLM import CardApplicationReviewer as Reviewer4
from longmethod_1_s_E import CardApplicationReviewer as R9

from longmethod_1_s_RLM_E import CardApplicationReviewer as R10
from longmethod_1_c_RLM import CardApplicationReviewer as R11

from featureenvy_1_c import CardApplicationReviewer as Reviewer5
from featureenvy_1_c_RFE import CardApplicationReviewer as Reviewer6
from featureenvy_1_s_E import CardApplicationReviewer as R12


from dataclasses import dataclass

@dataclass
class CardApplication:
    income: int

class CardApplicationResult:
    APPROVED = "APPROVED"
    DECLINED = "DECLINED"

class TestCardApplicationReviewers(unittest.TestCase):

    def setUp(self):
        self.applications = [
            CardApplication(income=1200),
            CardApplication(income=800),
        ]

        self.reviewers = [
    (Reviewer1(), "godclass_1_s"),
    #(Reviewer2(), "godclass_1_RF"),
    (Reviewer7(), "godclass_1_RF_E_"),
    (R8(),        "godclass_1_s_RGC"),

    (Reviewer3(), "longmethod_1_s"),
    (Reviewer4(), "longmethod_1_RF"),
    (R9(),        "longmethod_1_RF_E"),
    (R10(),       "longmethod_1_RF_E"),
    (R11(),       "longmethod_1_s_RLM"),
    (E1(),  "energy godclass"),

    (Reviewer5(), "featureenvy_1_s"),
    (Reviewer6(), "featureenvy_1_RF"),
    (R12(),       "featureenvy_1_s_E"),
    (R9(),       "energy lonfmethod"),
]


    def test_review(self):
        for reviewer, implementation in self.reviewers:
            for application in self.applications:
                with self.subTest(reviewer=implementation, income=application.income):
                    if application.income > 1000:
                        self.assertEqual(reviewer.review(application), CardApplicationResult.APPROVED)
                        print(f"Testing {implementation}: Approved for income {application.income}")
                    else:
                        self.assertEqual(reviewer.review(application), CardApplicationResult.DECLINED)
                        print(f"Testing {implementation}: Declined for income {application.income}")

if __name__ == '__main__':
    unittest.main()

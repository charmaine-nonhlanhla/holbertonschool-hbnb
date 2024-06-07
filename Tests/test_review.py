import unittest
from Model.Review import Review

class TestReview(unittest.TestCase):

    def test_review_instance(self):
        review = Review(5, "Great experience!")
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.comment, "Great experience!")

if __name__ == '__main__':
    unittest.main()


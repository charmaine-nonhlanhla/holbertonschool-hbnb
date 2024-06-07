import unittest
from Model.Place import Place

class TestPlace(unittest.TestCase):

    def test_add_review(self):
        place = Place("Cozy Apartment", "New York", 100)
        review = "Great experience!"
        place.add_review(review)
        self.assertIn(review, place.reviews)

    def test_add_amenity(self):
        place = Place("Cozy Apartment", "New York", 100)
        amenity = "Wi-Fi"
        place.add_amenity(amenity)
        self.assertIn(amenity, place.amenities)

if __name__ == '__main__':
    unittest.main()


import unittest
from Model.Amenity import Amenity

class TestAmenity(unittest.TestCase):

    def test_amenity_instance(self):
        amenity = Amenity("Wi-Fi", "High-speed internet access")
        self.assertEqual(amenity.name, "Wi-Fi")
        self.assertEqual(amenity.description, "High-speed internet access")

if __name__ == '__main__':
    unittest.main()


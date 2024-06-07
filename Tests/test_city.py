import unittest
from Model.City import City

class TestCity(unittest.TestCase):

    def test_city_instance(self):
        city = City("New York")
        self.assertEqual(city.name, "New York")

if __name__ == '__main__':
    unittest.main()


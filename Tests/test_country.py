import unittest
from Model.Country import Country

class TestCountry(unittest.TestCase):

    def test_country_instance(self):
        country = Country("USA")
        self.assertEqual(country.name, "USA")

if __name__ == '__main__':
    unittest.main()


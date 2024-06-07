# File: Model/Country.py

class Country:
    def __init__(self, name):
        self.name = name
        self.cities = []

    def add_city(self, city):
        self.cities.append(city)

    def remove_city(self, city):
        if city in self.cities:
            self.cities.remove(city)
        else:
            print("City not found in country's list.")
    
    @staticmethod
    def is_country_unique(name, existing_countries):
        """
        Check if the given country name is unique among existing countries.
        """
        return name not in [country.name for country in existing_countries]


# Example usage
if __name__ == "__main__":
    country = Country("USA")


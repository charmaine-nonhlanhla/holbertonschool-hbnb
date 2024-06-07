# File: Model/City.py

class City:
    def __init__(self, name):
        self.name = name
        self.places = []

    def add_place(self, place):
        self.places.append(place)

    def remove_place(self, place):
        if place in self.places:
            self.places.remove(place)
        else:
            print("Place not found in city's list.")

    @staticmethod
    def is_city_unique(name, existing_cities):
        """
        Check if the given city name is unique among existing cities.
        """
        return name not in [city.name for city in existing_cities]


# Example usage
if __name__ == "__main__":
    # Example usage for User class
    existing_users = [user1, user2]  # Assume these are existing user objects
    email_to_check = "user3@example.com"
    if User.is_email_unique(email_to_check, existing_users):
        print(f"Email '{email_to_check}' is unique.")
    else:
        print(f"Email '{email_to_check}' is not unique.")

    # Example usage for Country class
    existing_countries = [country1, country2]  # Assume these are existing country objects
    country_name_to_check = "Canada"
    if Country.is_country_unique(country_name_to_check, existing_countries):
        print(f"Country '{country_name_to_check}' is unique.")
    else:
        print(f"Country '{country_name_to_check}' is not unique.")

    # Example usage for City class
    existing_cities = [city1, city2]  # Assume these are existing city objects
    city_name_to_check = "Toronto"
    if City.is_city_unique(city_name_to_check, existing_cities):
        print(f"City '{city_name_to_check}' is unique.")
    else:
        print(f"City '{city_name_to_check}' is not unique.")


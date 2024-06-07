# File: Model/Place.py

class Place:
    def __init__(self, name, location, price):
        self.name = name
        self.location = location
        self.price = price
        self.reviews = []
        self.amenities = []

    def add_review(self, review):
        self.reviews.append(review)
 
    def remove_review(self, review):
        if review in self.reviews:
            self.reviews.remove(review)
        else:
            print("Review not found in place's list.")
            
    def add_amenity(self, amenity):
        self.amenities.append(amenity)

    def remove_amenity(self, amenity):
        if amenity in self.amenities:
            self.amenities.remove(amenity)
        else:
            print("Amenity not found in place's list.")

# Example usage
if __name__ == "__main__":
    place1 = Place("Cozy Apartment", "New York", 100)
    place2 = Place("Beach House", "Miami", 200)


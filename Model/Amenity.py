# File: Model/Amenity.py

class Amenity:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def update_description(self, new_description):
        self.description = new_description


# Example usage
if __name__ == "__main__":
    amenity1 = Amenity("Wi-Fi", "High-speed internet access")
    amenity2 = Amenity("Gym", "Fitness center")


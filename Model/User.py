import unittest

class User:
    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.places = []

    def add_place(self, place):
        self.places.append(place)

    def remove_place(self, place):
        if place in self.places:
            self.places.remove(place)
        else:
            print("Place not found in user's list of places.")

    @staticmethod
    def is_email_unique(email, existing_users):
        """
        Check if the given email is unique among existing users.
        """
        return email not in [user.email for user in existing_users]


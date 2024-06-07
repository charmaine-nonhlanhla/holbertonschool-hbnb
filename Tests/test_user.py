import unittest
from Model.User import User
class TestUser(unittest.TestCase):
    def test_unique_email(self):
        user1 = User("user1@example.com", "John", "Doe")
        user2 = User("user2@example.com", "Jane", "Smith")
        existing_users = [user1, user2]
        self.assertTrue(User.is_email_unique("newuser@example.com", existing_users))
        self.assertFalse(User.is_email_unique("user1@example.com", existing_users))

    def test_add_remove_place(self):
        user = User("user1@example.com", "John", "Doe")
        place1 = "Cozy Apartment"
        place2 = "Beach House"
        user.add_place(place1)
        self.assertIn(place1, user.places)
        user.add_place(place2)
        self.assertIn(place2, user.places)
        user.remove_place(place1)
        self.assertNotIn(place1, user.places)

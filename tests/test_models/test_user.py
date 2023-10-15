#!/usr/bin/python3
"""unittest for User class"""
# from models.base_model import BaseModel
from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """Define unittest for User class"""
    def setUp(self):
        self.my_user = User()

    def tearDown(self):
        del self.my_user

    def test_user_type(self):
        self.assertEqual(self.my_user.email, "")
        self.assertEqual(self.my_user.password, "")
        self.assertEqual(self.my_user.first_name, "")
        self.assertEqual(self.my_user.last_name, "")

    def test_user_attribute(self):
        """Test the values of attributes"""
        self.my_user.email = "airbnb@mail.com"
        self.my_user.password = "root"
        self.my_user.first_name = "Betty"
        self.my_user.last_name = "Bar"

        self.assertEqual(self.my_user.email, "airbnb@mail.com")
        self.assertEqual(self.my_user.password, "root")
        self.assertEqual(self.my_user.first_name, "Betty")
        self.assertEqual(self.my_user.last_name, "Bar")


if __name__ == '__main__':
    unittest.main()

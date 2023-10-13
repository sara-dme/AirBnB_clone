#!/usr/bin/python3
"""unittest for Amenity class"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Define unittest for Amenity"""

    def setUp(self):
        self.my_user = Amenity()

    def tearDown(self):
        del self.my_user

    def test_user_type(self):
        self.assertEqual(self.my_user.name, "")

    def test_user_attribute(self):
        self.my_user.name = "python"

        self.assertEqual(self.my_user.name, "python")


if __name__ == '__main__':
    unittest.main()

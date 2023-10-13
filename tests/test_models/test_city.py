#!/usr/bin/python3
"""unittest for City class"""
from models.city import City
from models.state import State
# from models.base_model import BaseModel
import unittest


class TestCity(unittest.TestCase):
    """Define unittest for City class"""

    def setUp(self):
        self.new_user = City()
        self.state = State()

    def tearDown(self):
        del self.new_user

    def test_city_type(self):
        self.assertEqual(self.new_user.state_id, "")
        self.assertEqual(self.new_user.name, "")

    def test_city_attribute(self):
        self.new_user.name = "root"
        self.new_user.state_id = self.state.id

        self.assertEqual(self.new_user.name, "root")
        self.assertEqual(self.new_user.state_id, self.state.id)


if __name__ == '__main__':
    unittest.main()

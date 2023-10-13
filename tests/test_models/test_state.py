#!/usr/bin/python3
"""unittest for State class"""
from models.base_model import BaseModel
from models.state import State
import unittest


class TestState(unittest.TestCase):
    """Define unittest for State class"""

    def setUp(self):
        self.my_user = State()

    def tearDown(self):
        del self.my_user

    def test_state_type(self):
        self.assertEqual(self.my_user.name, "")

    def tst_state_attribute(self):
        self.my_user.name = "state"

        self.assertEqual(self.my_user.name, "state")


if __name__ == '__main__':
    unittest.main()

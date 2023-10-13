#!/usr/bin/python3
"""unittest for Review"""
from models.review import Review
from models.place import Place
from models.user import User
import unittest


class TestReview(unittest.TestCase):
    """define unittest for Review class"""

    def setUp(self):
        self.my_user = Review()
        self.u = User()
        self.p = Place()

    def tearDown(self):
        del self.my_user

    def test_user_type(self):
        self.assertEqual(self.my_user.place_id, "")
        self.assertEqual(self.my_user.user_id, "")
        self.assertEqual(self.my_user.text, "")

    def test_user_attribute(self):
        self.my_user.place_id = self.p.id
        self.my_user.user_id = self.u.id
        self.my_user.text = "text"

        self.assertEqual(self.my_user.place_id, self.p.id)
        self.assertEqual(self.my_user.user_id, self.u.id)
        self.assertEqual(self.my_user.text, "text")


if __name__ == '__main__':
    unittest.main()

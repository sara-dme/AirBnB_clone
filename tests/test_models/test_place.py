#!/usr/bin/python3
"""unittest for Place class"""
from models.place import Place
from models.city import City
from models.user import User
from models.amenity import Amenity
import unittest


class TestPlace(unittest.TestCase):
    """Define unittest for Place"""

    def setUp(self):
        self.my_user = Place()
        self.c = City()
        self.u = User()
        self.a = Amenity()

    def tearDown(self):
        del self.my_user

    def test_user_type(self):
        self.assertEqual(self.my_user.city_id, "")
        self.assertEqual(self.my_user.user_id, "")
        self.assertEqual(self.my_user.name, "")
        self.assertEqual(self.my_user.description, "")
        self.assertEqual(self.my_user.number_rooms, 0)
        self.assertEqual(self.my_user.number_bathrooms, 0)
        self.assertEqual(self.my_user.max_guest, 0)
        self.assertEqual(self.my_user.price_by_night, 0)
        self.assertEqual(self.my_user.latitude, 0.0)
        self.assertEqual(self.my_user.longitude, 0.0)
        self.assertEqual(self.my_user.amenity_ids, [])

    def test_user_attribute(self):
        self.my_user.city_id = self.c.id
        self.my_user.user_id = self.u.id
        self.my_user.name = "name"
        self.my_user.description = "description"
        self.my_user.number_rooms = 5
        self.my_user.number_bathrooms = 2
        self.my_user.max_guest = 4
        self.my_user.price_by_night = 150
        self.my_user.latitude = 5.3
        self.my_user.longitude = 6.3
        self.my_user.amenity_ids = [self.a.id]

        self.assertEqual(self.my_user.city_id, self.c.id)
        self.assertEqual(self.my_user.user_id, self.u.id)
        self.assertEqual(self.my_user.name, "name")
        self.assertEqual(self.my_user.description, "description")
        self.assertEqual(self.my_user.number_rooms, 5)
        self.assertEqual(self.my_user.number_bathrooms, 2)
        self.assertEqual(self.my_user.max_guest, 4)
        self.assertEqual(self.my_user.price_by_night, 150)
        self.assertEqual(self.my_user.latitude, 5.3)
        self.assertEqual(self.my_user.longitude, 6.3)
        self.assertEqual(self.my_user.amenity_ids, [self.a.id])


if __name__ == '__main__':
    unittest.main()

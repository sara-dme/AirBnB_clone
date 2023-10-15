#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class"""

    def test_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_object_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_path_isPrivateString(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_init_storage(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of FileStorage class"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_args(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        bm = BaseModel()
        u = User()
        s = State()
        p = Place()
        c = City()
        a = Amenity()
        r = Review()
        models.storage.new(bm)
        models.storage.new(u)
        models.storage.new(s)
        models.storage.new(p)
        models.storage.new(c)
        models.storage.new(a)
        models.storage.new(r)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())
        self.assertIn("User." + u.id, models.storage.all().keys())
        self.assertIn(u, models.storage.all().values())
        self.assertIn("State." + s.id, models.storage.all().keys())
        self.assertIn(s, models.storage.all().values())
        self.assertIn("Place." + p.id, models.storage.all().keys())
        self.assertIn(p, models.storage.all().values())
        self.assertIn("City." + c.id, models.storage.all().keys())
        self.assertIn(c, models.storage.all().values())
        self.assertIn("Amenity." + a.id, models.storage.all().keys())
        self.assertIn(a, models.storage.all().values())
        self.assertIn("Review." + r.id, models.storage.all().keys())
        self.assertIn(r, models.storage.all().values())

    def test_new_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save(self):
        bm = BaseModel()
        u = User()
        s = State()
        p = Place()
        c = City()
        a = Amenity()
        r = Review()
        models.storage.new(bm)
        models.storage.new(u)
        models.storage.new(s)
        models.storage.new(p)
        models.storage.new(c)
        models.storage.new(a)
        models.storage.new(r)
        models.storage.save()
        txt = ""
        with open("file.json", "r") as f:
            txt = f.read()
            self.assertIn("BaseModel." + bm.id, txt)
            self.assertIn("User." + u.id, txt)
            self.assertIn("State." + s.id, txt)
            self.assertIn("Place." + p.id, txt)
            self.assertIn("City." + c.id, txt)
            self.assertIn("Amenity." + a.id, txt)
            self.assertIn("Review." + r.id, txt)

    def test_save_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        bm = BaseModel()
        u = User()
        s = State()
        p = Place()
        c = City()
        a = Amenity()
        r = Review()
        models.storage.new(bm)
        models.storage.new(u)
        models.storage.new(s)
        models.storage.new(p)
        models.storage.new(c)
        models.storage.new(a)
        models.storage.new(r)
        models.storage.save()
        models.storage.reload()
        obj = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, obj)
        self.assertIn("User." + u.id, obj)
        self.assertIn("State." + s.id, obj)
        self.assertIn("Place." + p.id, obj)
        self.assertIn("City." + c.id, obj)
        self.assertIn("Amenity." + a.id, obj)
        self.assertIn("Review." + r.id, obj)

    def test_reload_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()

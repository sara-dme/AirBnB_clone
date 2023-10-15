#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
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

    def setUp(self):
        super().setUp()
        self.file_path = storage._FileStorage__file_path
        self.instance = BaseModel()
        self._objs = storage._FileStorage__objects
        self.keyname = "BaseModel." + self.instance.id

    def tearDown(self):
        super().tearDown()
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        bm = BaseModel()
        models.storage.new(bm)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save(self):
        bm = BaseModel()
        models.storage.new(bm)
        models.storage.save()
        txt = ""
        with open("file.json", "r") as f:
            txt = f.read()
            self.assertIn("BaseModel." + bm.id, txt)
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        bm = BaseModel()
        models.storage.new(bm)
        obj = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, obj)
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()

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


class TestFileStorage(unittest.TestCase):
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

    def test_methods(self):
        obj = FileStorage
        self.assertTrue(hasattr(obj, "all"))
        self.assertTrue(hasattr(obj, "new"))
        self.assertTrue(hasattr(obj, "save"))
        self.assertTrue(hasattr(obj, "reload"))

    def test_all_method(self):
        """Test all() method"""
        result = storage.all()
        self.assertEqual(result, self._objs)

    def test_new_method(self):
        """test new() method"""
        storage.new(self.instance)
        key = f"{self.instance.__class__.__name__}.{self.instance.id}"
        self.assertIn(key, self._objs)

    def test_save_method(self):
        """test save() method"""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        storage.new(my_model)
        storage.save()
        with open(self.file_path, "r") as fl:
            save_data = json.load(fl)

        expected_data = {}
        for key, value in self._objs.items():
            expected_data[key] = value.to_dict()

        self.assertEqual(save_data, expected_data)

    def test_reload_method(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        storage.new(my_model)
        storage.save()
        with open(self.file_path, 'r') as file:
            save_data = json.load(file)
        storage.reload()

        with open(self.file_path, 'r') as file:
            reloaded_data = json.load(file)

        self._objs = {}
        self.assertEqual(reloaded_data[self.keyname], save_data[self.keyname])

    def test_path(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        self.assertFalse(os.path.exists(self.file_path))
        storage.reload()


if __name__ == "__main__":
    unittest.main()

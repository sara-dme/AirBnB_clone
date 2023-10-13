#!/usr/bin/python3
"""Unitest for base_model"""
from models.base_model import BaseModel
import unittest
import datetime
import json
import os


class test_basemodel(unittest.TestCase):
    """Define unitest for BaseModel class"""

    def setUp(self):
        """method that setUp the cases to test"""

        self.my_model = BaseModel()
        self.my_model.name = "My_First_Model"
        self.my_model.my_number = 89
        self.id = self.my_model.id
        self.type_att = datetime.datetime
        self.my_model_json = self.my_model.to_dict()

    def tearDown(self):
        """clean the tests"""
        del self.my_model

    def test__init__(self):
        """Test for the constructor"""
        self.assertIsInstance(self.my_model, BaseModel)

    def test_attributes(self):
        """Test for the attributes"""
        self.assertEqual(self.my_model.name, "My_First_Model")
        self.assertEqual(self.my_model.my_number, 89)

    def test_id(self):
        """Test for the id"""
        self.assertEqual(self.id, self.my_model.id)

    def test_unique_id(self):
        """Test if each instance of class has a unique id"""
        base_model1 = BaseModel()
        base_model2 = BaseModel()

        self.assertNotEqual(base_model1.id, base_model2.id)

    def test_str(self):
        """Test of the __str__ method"""
        base_model = BaseModel()
        str_method = str(base_model)
        self.assertIn("[BaseModel]", str_method)
        self.assertIn(base_model.id, str_method)
        self.assertIn(str(base_model.__dict__), str_method)

    def test_created_at(self):
        """test of the attribute created at"""
        self.assertEqual(self.type_att, type(self.my_model.created_at))

    def test_to_dict_created_at_isoformat(self):
        self.assertEqual(self.my_model_json['created_at'],
                         self.my_model.created_at.isoformat())

    def test_to_dict_updated_at_isoformat(self):
        self.assertEqual(self.my_model_json['updated_at'],
                         self.my_model.updated_at.isoformat())

    def test_save_updated_at(self):
        updated = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(updated, self.my_model.updated_at)

    def test_to_dict(self):
        """Test for t_dict method"""
        self.assertEqual(self.my_model_json, self.my_model.to_dict())

    def test_to_dict_keys(self):
        my_list = ['id', 'created_at', 'updated_at', '__class__']
        for key in my_list:
            self.assertIn(key, self.my_model_json)

    def test_to_dict_result(self):
        """Test if to_dict returns a dictionary
        with the correct attributes"""
        base_model = BaseModel()
        dict_base_model = base_model.to_dict()
        self.assertIsInstance(base_model, BaseModel)
        self.assertIsInstance(dict_base_model, dict)
        self.assertIn('id', dict_base_model)
        self.assertIn('created_at', dict_base_model)
        self.assertIn('updated_at', dict_base_model)
        self.assertIn('__class__', dict_base_model)
        self.assertIn(dict_base_model['__class__'], "BaseModel")


if __name__ == '__main__':
    unittest.main()

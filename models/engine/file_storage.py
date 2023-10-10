#!/usr/bin/python3
"""Module for FileStorage class"""
import json
import os
import datetime


class FileStorage:

    """serializes instances and deserializes JSON file to instances
    Attributes:
        __file_path (str): string - path to the JSON file
        __objects (dict): dictionnary to store all objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj class name>.id"""
        key = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(key, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        obj = FileStorage.__objects
        dictio = {o: obj[o].to_dict() for o in obj.keys()}
        with open(FileStorage.__file_path, "w", encodind="utf-8") as fl:
            json.dump(dictio, fl)

    def reload(self):
        """ deserializes the JSON file to __objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as fl:
            dictio = json.load(fl)
            for o in dictio.values():
                cls_name = o["__class__"]
                del o["__class__"]
                self.new(eval(cls_name)(**o))

#!/usr/bin/python3
"""Create a BaseModel class"""
import uuid
from datetime import datetime
import models
# from models import storage


class BaseModel:
    """
    Define a class BaseModel
    Public instance methods:
        -save(self): updates the public instance attribute
        updated_at with the current datetime
        -to_dict(self): returns a dictionary containing all
        keys/values of __dict__ of the instance
        -__str__: should print: [<class name>] (<self.id>) <self.__dict__>
    """

    def __init__(self, *args, **kwargs):
        """
        class constructor
        __init__(self, *args, **kwargs):
            *args won’t be used
            if kwargs is not empty:
                *each key of this dictionary is an attribute name
                *each value of this dictionary is the value of
                this attribute name
                *created_at and updated_at are strings in this dictionary:
                You have to convert these strings into datetime object.
            otherwise:
                *create id and created_at
        """

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Define str method"""

        return ("[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """Define a public instance method that updates the public
        instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Define a method that returns a dictionary containing
        all keys/values of __dict__ of the instance"""

        mydict = self.__dict__.copy()
        mydict['__class__'] = self.__class__.__name__
        mydict['created_at'] = self.created_at.isoformat()
        mydict['updated_at'] = self.updated_at.isoformat()
        return mydict

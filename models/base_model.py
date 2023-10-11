#!/usr/bin/python3
"""Create a BaseModel class"""
import uuid
from datetime import datetime


class BaseModel:
    """Define a class"""

    def __init__(self, *args, **kwargs):
        """class constructor"""

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

    def __str__(self):
        """Define str method"""

        return ("[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """Define a public instance method that updates the public
        instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Define a method that returns a dictionary containing
        all keys/values of __dict__ of the instance"""

        mydict = self.__dict__.copy()
        mydict['__class__'] = self.__class__.__name__
        mydict['created_at'] = self.created_at.isoformat()
        mydict['updated_at'] = self.updated_at.isoformat()
        return mydict

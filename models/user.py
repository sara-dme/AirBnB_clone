#!/usr/bin/python3
"""Create a class User that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Define a class User"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

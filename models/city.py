#!/usr/bin/python3
"""Create a City class"""


class City(BaseModel):
    """
    City class that inherit from BaseModel
    Public class attributes:
       state_id: string - empty string: it will be the State.id
       name: string - empty string
    """

    state_id = ""
    name = ""

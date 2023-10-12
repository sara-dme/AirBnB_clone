#!/usr/bin/python3
"""Create a Review class"""


class Review(BaseModel):
    """Define a Review class that inherit from BaseModel
    Public class attributes:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """

    place_id = ""
    user_id = ""
    text = ""

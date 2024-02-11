#!/usr/bin/python3
"""Contains class review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class inheriting from BaseModel
    Attributes:
        place_id (str) - The location/property identification
        user_id (str) - The user identification
        text (str) - The message text review
    """
    place_id = ""
    user_id = ""
    text = ""

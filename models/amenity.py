#!/usr/bin/python3
"""Contains Class amenity"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class inheriting from BaseModel
    Attributes:
        name (str) - The name of amenities on the facility
    """
    name = ""

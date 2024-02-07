#!/usr/bin/python3
"""Contains Class amenity"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """Amenity class inheriting from BaseModel"""

    def __init__(self, *args, **kwargs):
        """
        Initializes Amenity instance

        Args:
            *args: Tuple of class instance arguments
            **kwargs: Dictionary of class instance arguments
        """
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', '')

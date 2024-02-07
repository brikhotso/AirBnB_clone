#!/usr/bin/python3
"""Contains class review"""

from models.base_model import BaseModel

class Review(BaseModel):
    """Review class inheriting from BaseModel"""

    def __init__(self, *args, **kwargs):
        """
        Initializes Review instance

        Args:
            *args: Tuple of class instance arguments
            **kwargs: Dictionary of class instance arguments
        """
        super().__init__(*args, **kwargs)
        self.place_id = kwargs.get('place_id', '')
        self.user_id = kwargs.get('user_id', '')
        self.text = kwargs.get('text', '')

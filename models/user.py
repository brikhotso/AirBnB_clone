#!/usr/bin/python3
"""contain class user"""

from models.base_model import BaseModel

class User(BaseModel):
    """User class inheriting from BaseModel"""

    def __init__(self, *args, **kwargs):
        """
        Initializes User instance

        Args:
            *args: Tuple of class instance arguments
            **kwargs: Dictionary of class instance arguments
        """
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

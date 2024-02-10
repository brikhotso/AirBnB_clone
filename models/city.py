#!/usr/bin/python3
""" Contains class city"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class inheriting from BaseModel"""

    def __init__(self, *args, **kwargs):
        """
        Initializes City instance

        Args:
            *args: Tuple of class instance arguments
            **kwargs: Dictionary of class instance arguments
        """
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""

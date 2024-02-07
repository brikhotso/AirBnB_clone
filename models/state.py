#!/usr/bin/python3
"""Contains class state"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class inheriting from BaseModel"""

    def __init__(self, *args, **kwargs):
        """
        Initializes State instance

        Args:
            *args: Tuple of class instance arguments
            **kwargs: Dictionary of class instance arguments
        """
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', '')

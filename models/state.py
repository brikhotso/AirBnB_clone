#!/usr/bin/python3
"""Contains class state"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class inheriting from BaseModel
    Attributes:
        name (str) - Name of the state
    """
    name = ""


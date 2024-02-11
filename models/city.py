#!/usr/bin/python3
""" Contains class city"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class inheriting from BaseModel
    Attributes:
        state_id (str) - The state identification code
        name (str) - The city name
    """
    state_id = ""
    name = ""

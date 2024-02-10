#!/usr/bin/python3
"""contain class user"""

from models.base_model import BaseModel

class User(BaseModel):
    """User class inheriting from BaseModel"""
    self.email = ""
    self.password = ""
    self.first_name = ""
    self.last_name = ""

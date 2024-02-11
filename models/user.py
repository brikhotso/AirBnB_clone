#!/usr/bin/python3
"""contain class user"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel
    Class Attributes:
        email (str) - User email
        password (str) - User Password
        first_name(str) - User first name
        last_name(str) - User last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

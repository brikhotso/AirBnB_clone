#!/usr/bin/python3
"""A python module: base_model"""

import uuid
from datetime import datetime


class BaseModel:
    """A Base Model class"""

    def __init__(self, *args, **kwargs):
        """Initializing the BaseModel instance
        Args: args - Tuple of class instance arguments
              kwargs - Dictionary of class instance arguments 
        """
        if kwargs:
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.strptime(
                        kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if 'update_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(
                        kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns the string representation of the BaseModel instance"""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns dictionary representation of BaseModel instance."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

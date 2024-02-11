#!/usr/bin/python3
"""A python module: base_model"""

import uuid
import models
from datetime import datetime


class BaseModel:
    """A Base Model class"""

    def __init__(self, *args, **kwargs):
        """
        Initializing the BaseModel instance

        Args: args - Tuple of class instance arguments
              kwargs - Dictionary of class instance arguments
        """
        if kwargs:
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.strptime(
                        kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(
                        kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns the string representation of the BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates with current time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns dictionary representation of BaseModel instance.

        Returns:
            dict: Dictionary with all keys and values:
                - '__class__': The class name of the object.
                - 'created_at': Timestamp for when an instance is created
                - 'updated_at': Timestamp for the last instance updated
        """
        if not hasattr(self, 'id') or not hasattr(self, 'created_at') or \
           not hasattr(self, 'updated_at'):
            raise AttributeError("Missing required attributes")

        obj_dic = self.__dict__.copy()
        obj_dic['__class__'] = self.__class__.__name__
        obj_dic['created_at'] = self.created_at.isoformat()
        obj_dic['updated_at'] = self.updated_at.isoformat()
        return obj_dic

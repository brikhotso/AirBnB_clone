#!/usr/bin/python3
""" contains file storage and related methods"""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """
    Class for serializing and deserializing objects to and from a JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    @classmethod
    def all(cls):
        """
        Returns a dictionary containing all objects.
        """
        return cls.__objects

    @classmethod
    def new(cls, obj):
        """
        Adds a new object to the storage dictionary.

        Parameters:
            obj: An instance of a class inheriting from BaseModel.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        cls.__objects[key] = obj

    @classmethod
    def save(cls):
        """
        Saves objects in the storage dictionary to a JSON file.
        """
        serialized_objects = {key: obj.to_dict() for key,
                              obj in cls.__objects.items()}
        with open(cls.__file_path, 'w', encoding='utf-8') as myfile:
            json.dump(serialized_objects, myfile)

    @classmethod
    def reload(cls):
        """
        Reloads the storage dictionary from the JSON file.
        """
        try:
            with open(cls.__file_path, 'r') as myfile:
                objdict = json.load(myfile)
                for key, value in objdict.items():
                    class_name, obj_id = key.split('.')
                    # Dynamically create instances based on class_name
                    if class_name == 'User':
                        cls.__objects[key] = User(**value)
                    else:
                        cls.__objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            return

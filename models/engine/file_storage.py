#!/usr/bin/python3

import json
from models.base_model import BaseModel

class FileStorage:
    """
    Class for serializing and deserializing objects to and from a JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns a dictionary containing all objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the storage dictionary.

        Parameters:
            obj: An instance of a class inheriting from BaseModel.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Saves objects in the storage dictionary to a JSON file.
        """
        serialized_objects = {key: obj.to_dict() for key,
                              obj in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as myfile:
            json.dump(serialized_objects, myfile)

    def reload(self):
        """
        Reloads the storage dictionary from the JSON file.
        """
        try:
            with open(self.__file_path) as myfile:
                objdict = json.load(myfile)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return

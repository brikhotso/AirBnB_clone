#!/usr/bin/python3
"""Unittset for the Module: file_storage"""

import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os


class TestFileStorage(unittest.TestCase):
    """TestFileStorage unittest class"""

    @classmethod
    def setUp(self):
        """Setup method to initialize the FileStorage object"""
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        """Teardown method to remove the file created during testing"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_initialization(self):
        """Test if the FileStorage instance is initialized correctly"""
        self.assertEqual(type(FileStorage()), FileStorage)
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))
        self.assertEqual(type(models.storage), FileStorage)
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_all(self):
        """Test the all() method of FileStorage"""
        self.assertEqual(dict, type(models.storage.all()))
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new_args(self):
        """Test new args"""
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_reload_args(self):
        """Test reload() method with None args"""
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_reload(self):
        """Test reload method"""
        obj = BaseModel()
        usr = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        models.storage.new(obj)
        models.storage.new(usr)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(amenity)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + obj.id, objs)
        self.assertIn("User." + usr.id, objs)
        self.assertIn("State." + state.id, objs)
        self.assertIn("Place." + place.id, objs)
        self.assertIn("City." + city.id, objs)
        self.assertIn("Amenity." + amenity.id, objs)


if __name__ == '__main__':
    unittest.main()

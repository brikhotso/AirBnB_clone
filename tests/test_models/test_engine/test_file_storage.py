#!/usr/bin/python3
"""Unittset for the Module: file_storage"""

import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
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

    def test_new(self):
        """Test the new() method of FileStorage"""
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
        self.assertIn("BaseModel." + obj.id, models.storage.all().keys())
        self.assertIn(obj, models.storage.all().values())
        self.assertIn("User." + usr.id, models.storage.all().keys())
        self.assertIn(usr, models.storage.all().values())
        self.assertIn("State.." + state.id, models.storage.all().keys())
        self.assertIn(state, models.storage.all().values())
        self.assertIn("Place." + place.id, models.storage.all().keys())
        self.assertIn(place, models.storage.all().values())
        self.assertIn("City." + city.id, models.storage.all().keys())
        self.assertIn(city, models.storage.all().values())
        self.assertIn("Amenity." + amenity.id, models.storage.all().keys())
        self.assertIn(amenity, models.storage.all().values())

    def test_new_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save_reload(self):
        """Test the save() and reload() methods of FileStorage"""
        obj1 = BaseModel()
        usr = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 2)
        self.assertIn('BaseModel.' + obj1.id, self.storage.all())
        self.assertIn('BaseModel.' + obj2.id, self.storage.all())

    def test_reload_non_existing_file(self):
        """Test reload() method when the JSON file doesn't exist"""
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})

    def test_reload_existing_file(self):
        """Test reload() method when the JSON file exists"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 1)
        self.assertIn('BaseModel.' + obj.id, self.storage.all())


if __name__ == '__main__':
    unittest.main()

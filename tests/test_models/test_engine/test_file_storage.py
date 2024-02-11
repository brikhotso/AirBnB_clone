#!/usr/bin/python3
"""tests for FileStorage"""

import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Unit tests for the FileStorage class.
    """

    def setUp(self):
        """
        Set up the test environment by ensuring file.json doesn't
        exist before each test.
        """
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """
        Clean up after each test by removing file.json.
        """
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all(self):
        """
        Test retrieving all objects from storage.
        """
        storage = FileStorage()
        model = BaseModel()
        user = User()
        place = Place()
        state = State()
        city = City()
        amenity = Amenity()
        review = Review()

        storage.new(model)
        storage.new(user)
        storage.new(place)
        storage.new(state)
        storage.new(city)
        storage.new(amenity)
        storage.new(review)

        all_objects = storage.all()
        self.assertIn("BaseModel." + model.id, all_objects)
        self.assertIn("User." + user.id, all_objects)
        self.assertIn("Place." + place.id, all_objects)
        self.assertIn("State." + state.id, all_objects)
        self.assertIn("City." + city.id, all_objects)
        self.assertIn("Amenity." + amenity.id, all_objects)
        self.assertIn("Review." + review.id, all_objects)

    def test_new(self):
        """
        Test adding objects to storage.
        """
        storage = FileStorage()
        model = BaseModel()
        user = User()
        place = Place()
        state = State()
        city = City()
        amenity = Amenity()
        review = Review()

        storage.new(model)
        storage.new(user)
        storage.new(place)
        storage.new(state)
        storage.new(city)
        storage.new(amenity)
        storage.new(review)

        self.assertIn("BaseModel." + model.id, storage.all())
        self.assertIn("User." + user.id, storage.all())
        self.assertIn("Place." + place.id, storage.all())
        self.assertIn("State." + state.id, storage.all())
        self.assertIn("City." + city.id, storage.all())
        self.assertIn("Amenity." + amenity.id, storage.all())
        self.assertIn("Review." + review.id, storage.all())

    def test_reload(self):
        """
        Test reloading objects from file.
        """
        storage = FileStorage()
        model = BaseModel()
        user = User()

        storage.new(model)
        storage.new(user)
        storage.save()
        storage._FileStorage__objects = {}
        storage.reload()

        self.assertIn("BaseModel." + model.id, storage.all())
        self.assertIn("User." + user.id, storage.all())

    def test_save(self):
        """
        Test saving objects to file.
        """
        storage = FileStorage()
        model = BaseModel()
        user = User()
        storage.new(model)
        storage.new(user)
        storage.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))


if __name__ == '__main__':
    unittest.main()

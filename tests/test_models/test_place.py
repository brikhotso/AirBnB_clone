#!/usr/bin/python3
"""Module: test_place"""

import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """a unittest class TestPlace inherits from TestCase"""

    def setUp(self):
        """Set up a test instance of Place"""
        self.place = Place()

    def tearDown(self):
        """Clean up after each test"""
        del self.place

    def test_inheritance(self):
        """Test if Place class inherits from BaseModel"""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_instance_creation(self):
        """Test if an instance of Place can be created"""
        self.assertIsInstance(self.place, Place)

    def test_args_and_kwargs(self):
        """Test if instance can be created with args and kwargs"""
        place = Place("city_id", "user_id", "name", "description",
                      5, 3, 6, 100, 40.0, -74.0, ["amenity1", "amenity2"],
                      kwarg_key="kwarg_value")
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])
        self.assertEqual(place.kwarg_key, "kwarg_value")

    def test_default_values(self):
        """Test if default values are set correctly"""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_to_dict_contains_attributes(self):
        """Test if 'to_dict' method contains all attributes"""
        place_dict = self.place.to_dict()
        self.assertNotIn("city_id", place_dict)
        self.assertNotIn("user_id", place_dict)
        self.assertNotIn("name", place_dict)
        self.assertNotIn("description", place_dict)
        self.assertNotIn("number_rooms", place_dict)
        self.assertNotIn("number_bathrooms", place_dict)
        self.assertNotIn("max_guest", place_dict)
        self.assertNotIn("price_by_night", place_dict)
        self.assertNotIn("latitude", place_dict)
        self.assertNotIn("longitude", place_dict)
        self.assertNotIn("amenity_ids", place_dict)

    def test_str_representation(self):
        """Test if __str__ representation is as expected"""
        expected_str = "[Place] ({}) {}".format(
            self.place.id, self.place.__dict__)
        self.assertEqual(expected_str, str(self.place))


if __name__ == '__main__':
    unittest.main()

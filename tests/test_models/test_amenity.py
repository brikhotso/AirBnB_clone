#!/usr/bin/python3
"""Module: test_amenity"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """unittest class TestAmenity inherits from TestCase"""

    def setUp(self):
        """Set up a test instance of Amenity"""
        self.amenity = Amenity()

    def tearDown(self):
        """Clean up after each test"""
        del self.amenity

    def test_inheritance(self):
        """Test if Amenity class inherits from BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_instance_creation(self):
        """Test if an instance of Amenity can be created"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_args_and_kwargs(self):
        """Test if instance can be created with args and kwargs"""
        amenity = Amenity("arg_name", kwarg_name="kwarg_value")
        self.assertEqual(amenity.name, "")
        self.assertEqual(amenity.kwarg_name, "kwarg_value")

    def test_name_attribute(self):
        """Test if the 'name' attribute is present and initialized"""
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertEqual(self.amenity.name, "")

    def test_to_dict_contains_name(self):
        """Test if 'to_dict' method contains 'name' key"""
        amenity_dict = self.amenity.to_dict()
        self.assertIn("name", amenity_dict)

    def test_str_representation(self):
        """Test if __str__ representation is as expected"""
        expected_str = "[Amenity] ({}) {}".format(
            self.amenity.id, self.amenity.__dict__)
        self.assertEqual(expected_str, str(self.amenity))


if __name__ == '__main__':
    unittest.main()

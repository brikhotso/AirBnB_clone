#!/usr/bin/python3
"""Module: test_city"""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """class TestCity inheriting from unittest TestCase"""

    def setUp(self):
        """Set up a test instance of City"""
        self.city = City()

    def tearDown(self):
        """Clean up after each test"""
        del self.city

    def test_inheritance(self):
        """Test if City class inherits from BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_instance_creation(self):
        """Test if an instance of City can be created"""
        self.assertIsInstance(self.city, City)

    def test_args_and_kwargs(self):
        """Test if instance can be created with args and kwargs"""
        city = City("state_id", "name", kwarg_key="kwarg_value")
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
        self.assertEqual(city.kwarg_key, "kwarg_value")

    def test_state_id_attribute(self):
        """Test if the 'state_id' attribute is present and initialized"""
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertEqual(self.city.state_id, "")

    def test_name_attribute(self):
        """Test if the 'name' attribute is present and initialized"""
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertEqual(self.city.name, "")

    def test_to_dict_contains_state_id_and_name(self):
        """Test if 'to_dict' method contains 'state_id' and 'name' keys"""
        city_dict = self.city.to_dict()
        self.assertIn("state_id", city_dict)
        self.assertIn("name", city_dict)

    def test_str_representation(self):
        """Test if __str__ representation is as expected"""
        expected_str = "[City] ({}) {}".format(
            self.city.id, self.city.__dict__)
        self.assertEqual(expected_str, str(self.city))


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""Tests for class user"""

import unittest
from models.user import User
from datetime import datetime
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Unit tests for the User class"""

    def test_inheritance(self):
        """Test if User inherits from BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_attributes(self):
        """Test User attributes"""
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_attribute_types(self):
        """Test if User attribute types are correct"""
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_attribute_defaults(self):
        """Test if User attributes have default values"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_to_dict(self):
        """Test if to_dict method returns dictionary representation"""
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertIsInstance(datetime.fromisoformat
                              (user_dict['created_at']), datetime)
        self.assertIsInstance(datetime.fromisoformat
                              (user_dict['updated_at']), datetime)


if __name__ == '__main__':
    unittest.main()

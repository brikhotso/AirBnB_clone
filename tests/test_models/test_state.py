#!/usr/bin/python3
"""Module: test_state"""

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """unittest class TestState inherits from TestCase"""
    def setUp(self):
        """Set up a test instance of State"""
        self.state = State()

    def tearDown(self):
        """Clean up after each test"""
        del self.state

    def test_inheritance(self):
        """Test if State class inherits from BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_instance_creation(self):
        """Test if an instance of State can be created"""
        self.assertIsInstance(self.state, State)

    def test_args_and_kwargs(self):
        """Test if instance can be created with args and kwargs"""
        state = State("California", kwarg_key="kwarg_value")
        self.assertEqual(state.name, "")
        self.assertEqual(state.kwarg_key, "kwarg_value")

    def test_default_values(self):
        """Test if default values are set correctly"""
        self.assertEqual(self.state.name, "")

    def test_to_dict_contains_attributes(self):
        """Test if 'to_dict' method contains all attributes"""
        state_dict = self.state.to_dict()
        self.assertNotIn("name", state_dict)

    def test_str_representation(self):
        """Test if __str__ representation is as expected"""
        expected_str = "[State] ({}) {}".format(
            self.state.id, self.state.__dict__)
        self.assertEqual(expected_str, str(self.state))


if __name__ == '__main__':
    unittest.main()

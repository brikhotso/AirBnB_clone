#!/usr/bin/python3
"""Module: test_review"""

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """unittest class TestReview inherits from TestCase"""

    def setUp(self):
        """Set up a test instance of Review"""
        self.review = Review()

    def tearDown(self):
        """Clean up after each test"""
        del self.review

    def test_inheritance(self):
        """Test if Review class inherits from BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_instance_creation(self):
        """Test if an instance of Review can be created"""
        self.assertIsInstance(self.review, Review)

    def test_args_and_kwargs(self):
        """Test if instance can be created with args and kwargs"""
        review = Review("place_id", "user_id", "text", kwarg_key="kwarg_value")
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
        self.assertEqual(review.kwarg_key, "kwarg_value")

    def test_default_values(self):
        """Test if default values are set correctly"""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_to_dict_contains_attributes(self):
        """Test if 'to_dict' method contains all attributes"""
        review_dict = self.review.to_dict()
        self.assertIn("place_id", review_dict)
        self.assertIn("user_id", review_dict)
        self.assertIn("text", review_dict)

    def test_str_representation(self):
        """Test if __str__ representation is as expected"""
        expected_str = "[Review] ({}) {}".format(
            self.review.id, self.review.__dict__)
        self.assertEqual(expected_str, str(self.review))


if __name__ == '__main__':
    unittest.main()

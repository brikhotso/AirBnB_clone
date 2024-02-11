#!/usr/bin/python3
"""Module: test_console"""

import unittest
from unittest.mock import patch, MagicMock
from models import storage
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestConsole(unittest.TestCase):
    """unittest for class TestConsole inherits from TestCase"""

    def setUp(self):
        """Set up the console for testing"""
        self.console = HBNBCommand()

    def test_create(self):
        """Test the create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertIsInstance(BaseModel().id, str)
            self.assertEqual(len(output), 36)

    def test_show(self):
        """Test the show command"""
        new_model = BaseModel()
        new_model.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show BaseModel {new_model.id}")
            output = f.getvalue().strip()
            self.assertIn(str(new_model), output)

    def test_destroy(self):
        """Test the destroy command"""
        new_model = BaseModel()
        new_model.save()
        model_id = new_model.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"destroy BaseModel {model_id}")
            output = f.getvalue().strip()
            self.assertNotIn(model_id, storage.all())
            self.assertEqual(output, "")

    def test_all(self):
        """Test the all command"""
        new_model1 = BaseModel()
        new_model2 = BaseModel()
        new_model1.save()
        new_model2.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all BaseModel")
            output = f.getvalue().strip()
            self.assertIn(str(new_model1), output)
            self.assertIn(str(new_model2), output)

    def test_update(self):
        """Test the update command"""
        new_model = BaseModel()
        new_model.save()
        model_id = new_model.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"update BaseModel {model_id} name 'New Name'")
            self.console.onecmd(f"show BaseModel {model_id}")
            output = f.getvalue().strip()
            self.assertIn("'name': 'New Name'", output)

    def test_count(self):
        """Test the count command"""
        new_user1 = User()
        new_user2 = User()
        new_model1 = BaseModel()
        new_model2 = BaseModel()
        new_user1.save()
        new_user2.save()
        new_model1.save()
        new_model2.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count User")
            output = f.getvalue().strip()
            self.assertEqual(output, "2")


if __name__ == '__main__':
    unittest.main()

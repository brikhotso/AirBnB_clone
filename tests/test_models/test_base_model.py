#!/usr/bin/python3
"""The test_base_model class"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """BaseModel test class using unittest inheritance TestCase"""

    def test_attributes(self):
        """Test instance attributes"""
        model = BaseModel()
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

    def test_id(self):
        """Test if id attribute is a string"""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertIsInstance(model1.id, str)
        self.assertNotEqual(model1.id, model2.id)

    def test_created_at_and_updtaed_at_are_datetime(self):
        """Test if created_at and updated_at are datetime objects"""
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_save_method(self):
        """Test save method"""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_str_method(self):
        """Test str method"""
        model = BaseModel()
        model_str = str(model)
        self.assertTrue(isinstance(model_str, str))

    def test_to_dict(self):
        """Test to_dict method"""
        model = BaseModel()
        obj_dict = model.to_dict()
        self.assertTrue('__class__' in obj_dict)
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['updated_at'],
                         model.updated_at.isoformat())

    def test_args_none(self):
        model = BaseModel(None)
        self.assertNotIn(None, model.__dict__.values())

    def test_kwargs_none(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_kwargs(self):
        dtime = datetime.now()
        dtime_iso = dtime.isoformat()
        dt = dtime.strftime('%Y-%m-%dT%H:%M:%S.%f')
        kwargs = {'id': '345', 'created_at': dt, 'updated_at': dt}
        model = BaseModel(**kwargs)
        self.assertEqual(model.id, "345")
        self.assertEqual(model.created_at, dtime)
        self.assertEqual(model.updated_at, dtime)


if __name__ == '__main__':
    unittest.main()

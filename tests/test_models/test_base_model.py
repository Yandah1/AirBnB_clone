#!/usr/bin/python3
"""Unittest for BaseModel class"""

import unittest
import uuid
from models import storage
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """unittest"""

    def setup(self):
        """Set up any necessary dependencies"""
        pass

    def tearDown(self):
        """Clean up after each test if needed"""
        pass

    def test__init__(self):
        """the initialization of BaseModel"""
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        key = "{}.{}".format(model.__class__.__name__, model.id)
        self.assertEqual(storage.all().get(key), model)

    def test_save(self):
        """Test the save method of BaseModel"""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test the to_dict method of BaseModel"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'],
                         model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'],
                         model.updated_at.isoformat())


if __name__ == '__:main__':
    unittest.main()

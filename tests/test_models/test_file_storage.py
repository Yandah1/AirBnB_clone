#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Create an instance of FileStorage"""
        self.storage = FileStorage()

    def test_all_empty(self):
        """Test that all() returns an empty dictionary initially"""
        result = self.storage.all()
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 0)

    def test_new_object(self):
        """ Test that new() adds a new object to the storage"""
        model = BaseModel()
        self.storage.new(model)
        result = self.storage.all()
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 1)
        key = "{}.{}".format(model.__class__.__name__, model.id)
        self.assertIn(key, result)

    # Add more unit tests for other methods


if __name__ == '__main__':
    unittest.main()

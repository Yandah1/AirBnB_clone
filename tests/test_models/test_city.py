#!/usr/bin/python3
"""unittest the for city class"""

import unittest
from datetime import datetime
import time
from models.city import City
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
"""unittest for city class"""

   def setUp(self):
     """sets up test methods"""
        pass

   def tearDown(self):
     """tears down the test methods"""
        self.resetStorage()
        pass

   def resetStorage(self):
     """resets data from FileStorage"""
        FileStorage._FileStorage__objects = {}
     if os.path.isfile(FileStorage._FileStorage__file_path):
        os.remove(FileStorage._FileStorage__file_path)

   def test_8_instantiation(self):
     """tests instantiation of the city class"""

        b = City()
        self.assertEqual(str(type(b)), "<class 'models.city.City'>")
        self.assertIsInstance(b, City)
        self.assertTrue(issubclass(type(b), BaseModel))

   def test_8_attributes(self):
     """tests city class attributes"""
        attributes = storage.attributes()["City"]
        o = City()
    for k, v in attributes.items():
        self.assertTrue(hasattr(o, k))
        self.assertEqual(type(getattr(o, k, None)), v)


     if __name__ == "__main__":
        unittest.main()

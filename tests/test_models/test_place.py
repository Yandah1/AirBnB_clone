<<<<<<< HEAD
#!/usr/bin/python3
"""unittest for place class"""

import unittest
from datetime import datetime
import time
from models.place import Place
import re
import json
from models.engine.file_storage
import FileStorage
=======
#/usr/bin/python3
"""Unittest for class Place"""
>>>>>>> 64de3fe (tester)
import os
from models import storage
from models.base_model import BaseModel
import unittest

class TestPlace(unittest.TestCase):
    """Unittest for Place Class"""

    def setUp(self):
        """a set up for the test methods"""
        pass

    def tearDown(self):
        """tears down the methods"""
        self.resetStorage()
        pass

    def resetStorage(self):
        """"resets data of FileStorage"""
        FileStorage._FileStorage_objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

<<<<<<< HEAD
 FileStorage._FileStorage_objects = {}
     if os.path.isfile(FileStorage._FileStorage__file_path):

 os.remove(FileStorage._FileStorage__path)
   
    def test_8_instantiation(self):
      """tests instantiation of place class""" 

      b = Place()
      self.assertEqual(str(b)), "<class'models.place.Place'>")
      self.assertlslnstance(b, Place)

      self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
      """the tests attributes of plass class"""
      attributes = storage.attributes()
 ["Place"]
      o = Place()
      for k, v in attributes.items():
          self.assertTrue(hasattr(o, k))
          self.assertEqual(type(getattr(o, k,None)), v)

 if _name_ == "_main_":
     unittest.main()   
 
=======

if __name__ == "__main__":
        unittest.main()
>>>>>>> 64de3fe (tester)

import os
from models.base storage
from models models.base_model import BaseModel

class TestPlace(unittest.TestCase):
    """a unittest for Place Class"""

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
     if
 os.path.isfile(FileStorage._FileStorage__file_path) 

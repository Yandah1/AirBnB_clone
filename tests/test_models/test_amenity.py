import time
from models.amenity import amenity
import re
import json
from models.engine.file_storage
import FileStorage
import os
from models import storage
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    """unittest for testing amenity class"""

    def setUp(self):
      """sets test methods of amenity class"""         
      pass

    def tearDown(self):
      """tears down methods of amenity class"""
      self.resetStorage(self)
      pass

    def resetSorage(self):
      """resets Filestorage data"""

 FileStorage._FileStorage__objects = {} 
      if os.path.isfile(FileStorage.FileStorage__file_path):

 os.remove(FileStorage._FileStorage__file_path)

    def test_8_intantiation(self):
      """tests the instantiation of amenity class"""
      b = Amenity()
      self.assertEqual(str(type(b)), "<class 'models.amenity.Amenity'>")
      self.assertlslnstance(b, Amenity)

 self.assertTrue(issubclass(type(b), Basemodel))

    def test_8_attributes(self):
      """tests attributes of the amenity class"""
      attributes = storage.attributes()
 ["Amenity"]
     o = Amenity()
     for k, v in attributes.items():
         self.assertTrue(hasattr(o, k))
         self.assertEqual(type(getattr(o, k, None)), v)

 if _name_ == "_main_":
     unittest.main()  

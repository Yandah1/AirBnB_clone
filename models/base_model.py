#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods
for other classes:"""

import uuid
from datetime import datetime
import  models

class BaseModel:
    """Defining a class base model"""

    def __init__(self):
        """Initialized attribute of base class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Defining str method"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Defining save method"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Defining to_dict method"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
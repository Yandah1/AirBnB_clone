#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods
for other classes:"""
import uuid
from datetime import datetime


class BaseModel:
    """Defining a class base model"""

    def __init__(self, *args, **kwargs):
        """Initialization of base class instance

        Args:
            *args: arguments
            **kwargs: key-value arguments
        """
        from . import storage
        if kwargs:
            kwargs.pop("__class__", None)
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Defining str method"""
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Defining save method"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Defining to_dict method"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

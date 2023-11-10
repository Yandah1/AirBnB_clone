#!/usr/bin/python3
"""Module for file storage class"""

import os
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Class for persistent storage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns _objects dictionary"""
        return self.__objects

    def new(self, obj):
        """Sets new objects"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Saves all files"""
        objs = {}
        for k, v in self.__objects.items():
            objs[k] = v.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(objs, file)

    def reload(self):
        """Deserializes the JSON file to _objects"""
        if not os.path.isfile(self.__file_path):
            return

        with open(self.__file_path, 'r') as file:
            obj_dict = json.load(file)
            self.__objects = {}
            for k, v in obj_dict.items():
                class_name = v.get('__class__')    
                if class_name and class_name in globals():
                    self.__objects[k] = globals()[class_name](**v)
                else:
                   # Handle unknown class name
                   print("Unknown class name: {}".format(class_name)) 

    def get_objs_by_class(self):
        """get objects by their class name"""
        objects_by_class = {
                "BaseModel": BaseModel,
                "User": User
                }
        return objects_by_class

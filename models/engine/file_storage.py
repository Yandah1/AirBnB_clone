#!/usr/bin/python3
"""Module for file storage class"""

import os
import json
import models

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
            obj_dict = {k: self.classes()[v['__class__']](**v)
                        for k, v in obj_dict.items()}
            self.__objects = obj_dict

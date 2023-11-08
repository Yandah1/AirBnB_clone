#!/usr/bin/python3
"""Module for file storage class"""

import os
import json
import models

class FileStorage:
    """Class for persistent storage"""
    _file_path = "file.json"
    _objects = {}

    def all(self):
        """Returns _objects dictionary"""
        return self._objects

    def new(self, obj):
        """Sets new objects"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self._objects[key] = obj

    def save(self):
        """Saves all files"""
        objs = {}
        for k, v in self._objects.items():
            objs[k] = v.to_dict()

        with open(self._file_path, 'w') as file:
            json.dump(objs, file)

    def reload(self):
        """Deserializes the JSON file to _objects"""
        if not os.path.isfile(self._file_path):
            return

        with open(self._file_path, 'r') as file:
            obj_dict = json.load(file)
            obj_dict = {k: self.classes()[v['__class__']](**v)
                        for k, v in obj_dict.items()}
            self._objects = obj_dict

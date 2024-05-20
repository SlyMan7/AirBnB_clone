#!/usr/bin/python3
"""
The module for serializing and deserializing objects.
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City

class FileStorage:
    """ Handles serialization and deserialization of data to/from JSON. """
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """ Adds an object to the storage dictionary. """
        self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def all(self):
        """ Returns the dictionary of stored objects. """
        return self.__objects

    def save(self):
        """ Serializes the objects to JSON and writes to the file. """
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """ Deserializes the JSON file to objects if file exists. """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                for k, v in json.load(f).items():
                    cls_name, _ = k.split('.')
                    cls = globals()[cls_name]
                    self.__objects[k] = cls(**v)


#!/usr/bin/python3
"""
File storage mdule that includes a class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances.
"""

import json
from models import base_model


class FileStorage():
    """
    FileStorage serializes instances to a JSON file and deserializes JSON file
    to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        self[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""

        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(self.__file_path, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)"""

        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                json.load(self.__file_path, f)
        except Exception:
            pass

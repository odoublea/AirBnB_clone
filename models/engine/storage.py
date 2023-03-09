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
        return __objects
    
    def new(self, obj):
        setattr(self, __class__.id, obj)

    def save(self):
        """Class method that writes the JSON string representation
        of list_objs to a file.
        Args:
            list_objs: is a list of instances who inherits of Base - example:
            list of Rectangle or list of Square instances.
            cls: Class
        """

        with open(__file_path, "w", encoding="utf-8") as f:
            json.dump(__file_path, f)


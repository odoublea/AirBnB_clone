#!/usr/bin/python3
"""
File storage module which holds a class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances.

` <class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump ->
<class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'>
-> <class 'BaseModel'> `

"""

import json
from models.base_model import BaseModel
from datetime import datetime


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
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized_objs = {}
        for key, value in self.__objects.items():
            serialized_objs[key] = value.to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(serialized_objs, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)"""

        try:
            with open(self.__file_path, "r") as f:
                objs = json.load(f)
                for o in objs.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))

        except FileNotFoundError:
            pass

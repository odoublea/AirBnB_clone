#!/usr/bin/python3
"""
File storage module which holds a class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances.

` <class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump ->
<class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'>
-> <class 'BaseModel'> `

"""

import json


class FileStorage():
    """
    FileStorage serializes instances to a JSON file and deserializes JSON file
    to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of all objects of a given class."""
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
        """Loads storage dictionary from file

        Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)"""

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

        try:
            objs = {}
            with open(self.__file_path, "r") as f:
                objs = json.load(f)
                for key, val in objs.items():
                    self.all()[key] = classes[val['__class__']](**val)

        except FileNotFoundError:
            pass

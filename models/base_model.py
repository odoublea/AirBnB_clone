#!/usr/bin/python3
"""
This module houses the BaseModel that defines all common attributes/
methods for other classes.

Public instance attributes:
    id: string - uuid
    created_at: datetime - current datetime when an instance is created
    updated_at: datetime - current datetime when an instance is created
                and updated every time the object is changed.

"""


from uuid import uuid4
from datetime import datetime

class BaseModel():
    """
    The base model that defines all common attributes/methods for other
    classes.
    """
    def __init__(self, id=None, created_at=None, updated_at=None):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        str = f"[{__class__.__name__}] ({self.id}) {self.__dict__}"
        return str
    def save(self):
        self.updated_at = datetime.now()
    def to_dict(self):
        """instance to dictionary representation."""
        dict_repr = {}
        attrs = ('id', 'created_at', 'updated_at')
        dict_repr["__class__"] = type(self).__name__
        for i in attrs:
            if isinstance(i, datetime):
                dict_repr[key] = i.strftime('%Y-%m-%dT%H:%M:%S.%f')
            dict_repr[i] = getattr(self, i)
        return dict_repr




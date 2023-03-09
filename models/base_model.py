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
import models


class BaseModel():
    """
    The base model that defines all common attributes/methods for other
    classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the public instance attributes of the BaseModel Class.
        """

        if not kwargs:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()

        for key, value in kwargs.items():
            if key == '__class__':
                continue
            if key == 'created_at' or key == 'updated_at':
                value = datetime.isoformat(value)
            setattr(self, key, value)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        str_repr = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        return str_repr

    def save(self):
        """
        Updates the public instance attribute updated_at with the
        current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns dictionary representation of the instance, along with
        the class name
        - isoformat of datetime object for created_at and updated_at.
        """
        dict_repr = self.__dict__.copy()
        dict_repr["__class__"] = self.__class__.__name__
        for k, v in dict_repr.items():
            if isinstance(k, datetime):
                dict_repr[k] = v.isoformat()

        return dict_repr

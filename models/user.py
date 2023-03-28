#!/usr/bin/python3
"""Class User that inherits from BaseModel
    """

from models.base_model import BaseModel


class User(BaseModel):
    """Class User that inherits from BaseModel

    Args:
        email (str): email of the user
        password (str): password of the user
        first_name (str): first name of the user
        last_name (str): last name of the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

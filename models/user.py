#!/usr/bin/python3
"""Class User that inherits from BaseModel
    """

from models.base_model import BaseModel
import models


class User(BaseModel):
    """Class User that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Constructor method
        """
        super().__init__(*args, **kwargs)

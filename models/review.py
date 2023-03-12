#!/usr/bin/python3
"""Revirew class that inherits from BaseModel
    """

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel

    Args:
        place_id (str): the place id
        user_id (str): the user id
        text (str): the review text 
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Constructor method
        """
        super().__init__(*args, **kwargs)

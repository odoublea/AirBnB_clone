#!/usr/bin/python3
"""Class Amenity that inherits from BaseModel
    """


from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class Amenity that inherits from BaseModel

    Args:
        name (str): name of the amenity
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Constructor method
        """
        super().__init__(*args, **kwargs)

#!/usr/bin/python3
"""Class City that inherits from BaseModel
    """


from models.base_model import BaseModel


class City(BaseModel):
    """Class City that inherits from BaseModel

    Args:
        state_id (str): The State Id.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""

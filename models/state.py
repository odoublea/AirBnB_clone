#!/usr/bin/python3
"""Class State that inherits from BaseModel
    """


from models.base_model import BaseModel


class State(BaseModel):
    """Class State that inherits from BaseModel

    Args:
        BaseModel
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Constructor method
        """
        super().__init__(*args, **kwargs)

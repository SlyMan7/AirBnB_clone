#!/usr/bin/python3
"""
This module defines the City class.
"""

from models.base_model import BaseModel

class City(BaseModel):
    """
    Represents a city within a state.

    Attributes:
        state_id (str): The identifier of the state to which the city belongs.
        name (str): The official name of the city.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new City instance.

        Args:
            *args: Unused.
            **kwargs: Key/value pairs of attributes, including state_id and name.
        """
        super().__init__(*args, **kwargs)
        self.state_id = kwargs.get('state_id', "")
        self.name = kwargs.get('name', "")


#!/usr/bin/python3
"""
This module defines the State class.
"""

from models.base_model import BaseModel

class State(BaseModel):
    """
    Represents a geographical state with a name attribute.

    Attributes:
        name (str): The official name of the state.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new State instance.

        Args:
            *args: Unused.
            **kwargs: Key/value pairs of attributes, primarily the name of the state.
        """
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', "")


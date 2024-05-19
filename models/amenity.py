#!/usr/bin/python3
"""
The module defining an Amenity.
"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """ Represents an amenity with a name. """
    def __init__(self, name=""):
        super().__init__()
        self.name = name


#!/usr/bin/python3
"""
This module defines the Review class.
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """
    Represents a review by a user for a place.

    Attributes:
        place_id (str): The unique identifier of the place being reviewed.
        user_id (str): The unique identifier of the user who wrote the review.
        text (str): The content of the review.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new Review instance.

        Args:
            *args: Unused.
            **kwargs: Key/value pairs of attributes, including place_id, user_id, and text.
        """
        super().__init__(*args, **kwargs)
        self.place_id = kwargs.get('place_id', "")
        self.user_id = kwargs.get('user_id', "")
        self.text = kwargs.get('text', "")


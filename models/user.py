#!/usr/bin/python3
"""
This module defines the User class.
"""

from models.base_model import BaseModel

class User(BaseModel):
    """
    Represents a user with personal information attributes.

    Attributes:
        email (str): The email address of the user.
        password (str): The password for the user's account.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new User instance.

        Args:
            *args: Unused.
            **kwargs: Key/value pairs of attributes.
        """
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', "")
        self.password = kwargs.get('password', "")
        self.first_name = kwargs.get('first_name', "")
        self.last_name = kwargs.get('last_name', "")


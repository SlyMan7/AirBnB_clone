#!/usr/bin/python3
"""
This module defines the Place class.
"""

from models.base_model import BaseModel

class Place(BaseModel):
    """
    Represents a lodging place with various attributes.

    Attributes:
        city_id (str): The identifier of the city where the place is located.
        user_id (str): The identifier of the user who owns the place.
        name (str): The name of the lodging place.
        description (str): A detailed description of the place.
        number_rooms (int): The count of rooms available in the place.
        number_bathrooms (int): The count of bathrooms available in the place.
        max_guest (int): The maximum number of guests the place can accommodate.
        price_by_night (int): The cost per night to stay at the place.
        latitude (float): The geographical latitude of the place.
        longitude (float): The geographical longitude of the place.
        amenity_ids (list): A list of identifiers for amenities offered at the place.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new Place instance.

        Args:
            *args: Unused.
            **kwargs: Key/value pairs of attributes, including identifiers, descriptive information, and numerical values related to the lodging place.
        """
        super().__init__(*args, **kwargs)
        self.city_id = kwargs.get('city_id', "")
        self.user_id = kwargs.get('user_id', "")
        self.name = kwargs.get('name', "")
        self.description = kwargs.get('description', "")
        self.number_rooms = kwargs.get('number_rooms', 0)
        self.number_bathrooms = kwargs.get('number_bathrooms', 0)
        self.max_guest = kwargs.get('max_guest', 0)
        self.price_by_night = kwargs.get('price_by_night', 0)
        self.latitude = kwargs.get('latitude', 0.0)
        self.longitude = kwargs.get('longitude', 0.0)
        self.amenity_ids = kwargs.get('amenity_ids', [])


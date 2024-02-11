#!/usr/bin/python3
"""Contains class place"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Place class inheriting from BaseModel
    Attributes:
        city_id (str) - The city identification code
        user_id (str) - The user identification code
        name (str) - The name of the location/property
        description (str) - The property description
        number_rooms (int) - The number of rooms on thr property
        number_bathrooms (int) - The number of bathrooms on the property
        max_guest (int) - The maximum allowable guest on the property
        price_by_night (int) - The price pert night of the property
        latitude (float) - The geographical latitudinal coordinate
        longitude (float) - The geographical longititudinal coordinate
        amenity_ids (list) - The list of identification for the amenities
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

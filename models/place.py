#!/usr/bin/python3
"""Creates a new Place class object."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Instantiates/Reps a place.

    Attributes:
        city_id(type <str>): city's ID.
        user_id(type <str>): user's ID.
        name(type <str>): place's name.
        description(type <str>): place's decription.
        number_rooms(type <int>): available rooms in number.
        number_bathrooms(type <int>): available bathroom.
        max_guest(type <int>): max guests allowed.
        price_by_night(type <int>): price per night.
        latitude(type <float>): X-coordinate of the place.
        longitude(type <float>): Y-coordinate of the place.
        amenity_ids(type <list>): amenity's id.
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

#!/usr/bin/python3
"""Creates a new Amenity class object."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Instantiates/Reps an amenity.

    Attributes:
        name(type <str>): amenity's name.
    """

    name = ""

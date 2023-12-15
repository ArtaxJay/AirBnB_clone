#!/usr/bin/python3
"""Creates a new City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Instantiates/Reps a city.

    Attributes:
        state_id(type <str>): state's ID.
        name(type <str>): city's name.
    """

    state_id = ""
    name = ""

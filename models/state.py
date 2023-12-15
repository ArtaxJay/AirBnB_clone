#!/usr/bin/python3
"""Creates a new State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Instantiates/Reps a state.

    Attributes:
        name (str): state's name.
    """

    name = ""

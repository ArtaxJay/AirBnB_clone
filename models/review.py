#!/usr/bin/python3
"""Creates a new Review class object."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Instantiates/Reps users' reviews.

    Attributes:
        place_id(type <str>): place's ID.
        user_id(type <str>): user's ID.
        text(type <str>): review/comment.
    """

    place_id = ""
    user_id = ""
    text = ""

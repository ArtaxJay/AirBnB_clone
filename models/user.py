#!/usr/bin/python3
"""Creates a new User class inheriting from the BaseModel class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Instanstiate/Reps a User.

    Attrs:
        email (str): user's e-mail.
        password (str): user's passcode.
        first_name (str): user's actual name.
        last_name (str): user's surname.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

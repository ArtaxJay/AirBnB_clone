#!/usr/bin/python3
"""Creates the BaseModel class object blueprint."""
import models
from uuid import uuid1
from datetime import datetime


class BaseModel:
    """Reps the BaseModel for ALX AirBnB project."""

    def __init__(self, *args, **kwargs):
        """Inits a new BaseModel object for each instance.

        Args:
            *args (array): An array of limitless params. Not used.
            **kwargs (dict): An array of key-value pairs of limitless attrs.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid1())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(val, tform)
                else:
                    self.__dict__[key] = val
        else:
            models.storage.new(self)

    def save(self):
        """Changes updated_at as the datetime changes."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Rets a dict of BaseModel instance 
        that contains all the key-value pairs.
        """
        basedict = self.__dict__.copy()
        basedict["created_at"] = self.created_at.isoformat()
        basedict["updated_at"] = self.updated_at.isoformat()
        basedict["__class__"] = self.__class__.__name__
        return basedict

    def __str__(self):
        """
        Re-Config to print/str repres of a BaseModel class instance.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

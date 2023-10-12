#!/usr/bin/python3
"""This module defines a class named BaseModel"""


import uuid
from datetime import datetime


class BaseModel:
    """This is a representation class called Basemodel for HBNB"""

    def __init__(self, *args, **kwargs):
        """An instantiating method"""

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    n_value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, n_value)
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """This returns a string representation of an instance"""

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self, updated_at):
        """Updates attribute updated_at to the current time"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns the dictionary of the represented instances"""

        ret_dict = self.__dict__
        ret_dict["__class__"] = self.__class__.__name__
        ret_dict["created_at"] = self.created_at.isoformat()
        ret_dict["updated_at"] = self.updated_at.isoformat()
        return ret_dict

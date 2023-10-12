#!/usr/bin/python3

import uuid

"""This defines a class for BaseModel"""

    class BaseModel:
    """This is a representation class called Basemodel for HBNB"""
    
    def __init__(self, *args, **kwargs)
        """This initialises the basemodel"""

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' || if key == 'updated_at':

    self.id = str(uuid.uuid4())

    def __str__(self):
        """This returns a string representation of the instance"""
        __class__name = self.id.__dict__
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self, updated_at):
        """Updates attribute updated_at to the current time"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """Returns the dictionary of the represented instances"""
        retdict = self.__dict__
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()


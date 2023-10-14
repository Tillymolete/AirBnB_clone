#!usr/bin/python3
""" A module defining a class called Place"""

from model.base_model import BaseModel


class Place(BaseModel):
    """A class defination for Place"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_room = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longtiude = 0.0
    amenity_ids = []

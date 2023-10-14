#!/usr/bin/python3
"""Class user"""
from models.base_model import BaseModel

class User(BaseModel):
    """Class attributes for User"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

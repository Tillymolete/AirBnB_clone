#!/usr/bin/python3
"""This is a class module for filestorage"""

import os
import json
from pathlib import Path
from models.base_model import BaseModel


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Public instance that returns objects"""

        return FileStorage.__objects

    def new(self, obj):
        """set obj in __objects with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__,  obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes the objects to JSON file"""
        new_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to objects"""
        file_path = Path(FileStorage.__file_path)
        if file_path.is_file():
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = {
                    k: BaseModel(**v) for k, v in json.load(f).items()
                }

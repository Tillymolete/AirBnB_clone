#!/usr/bin/python3
    """This is a class module for filestorage"""

class FileStorage:
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Public instance that returns objects"""

        return self.__objects
    
    def new(self, obj):
        """set obj in __objects with key <obj class name>.id"""

    def save(self):
        """Serializes the objects to JSON file"""
        serialize_objs = {}

        for key, obj in FileStorage.__objects.items():
            serialize_objs[key] = value.to_dict()

    def reload(self):
        """Deserializes the JSON file to ojects"""

        with open(FileStorage.__file_path, 'r') as f:
            for key, value in json.load(f).items():

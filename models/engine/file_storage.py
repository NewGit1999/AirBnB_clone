#!/usr/bin/python3
"""module of file storage"""
import json
from os import path

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """file storage class"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """set objects with key"""
        airname = obj.__class__.__name
        FileStorage.__objects["{}.{}".format(airname, obj.id)] = obj

    def save(self):
        """serialize objects to the json file"""
        my_dict = FileStorage.__objects.copy()
        fin_dict = {i: my_dict[i].to_dict() for i in my_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(fin_dict, f)

    def reload(self):
        """desrialize json file to objects"""
        try:
            with open(FileStorage.__file_path) as f:
                fin_dict = json.load(f)
                for j in fin_dict.values():
                    this_name = j["__class__"]
                    del j["__class__"]
                    self.new(eval(this_name)(**j))
        except FileNotFoundError:
            return

#!/usr/bin/python3
"""Base model class"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """base class"""
    def __init__(self, *args, **kwargs):
        """initialize attributes"""
        form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, form)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """representation of base model"""
        slfname = sefl.__class__.__name__
        return ("[{}] ({}) {}".format(slfname, self.id, self.__dict__))

    def save(self):
        """update updated_at attribute with current time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionnary of key/value"""
        val_dict = self.__dict__.copy()
        val_dict.update({"__class__": self.__class__.__name__})
        val_dict.update({"created_at": self.created_at.isoformat()})
        val_dict.update({"updated_at": self.updated_at.isoformat()})
        return (val_dict)

#!/usr/bin/python3
"""Basemodel class"""

import uuid
from datetime import datetime
"""this is the import documentation"""

class BaseModel:
    """a class documentation"""
    def __init__(self, *args, **kwargs):

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key != "__class__":
                    self.__dict__[key] = value
    
    def __str__(self):
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        todict = dict(self.__dict__)
        todict["__class__"] = self.__class__.__name__
        if not isinstance(todict["created_at"], str):
            todict["created_at"] = todict["created_at"].isoformat()
        if not isinstance(todict["updated_at"], str):
            todict["updated_at"] = todict["updated_at"].isoformat()
        return todict

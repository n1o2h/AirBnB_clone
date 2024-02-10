#!/usr/bin/python3
""" import docum """
import json
import os
from models.base_model import BaseModel

class FileStorage:
    """class docum"""

    __file_path = "file.json"
    __objects = {}

    def all(self):

        return FileStorage.__objects

    def new(self, obj):

        id = obj.to_dict()["id"]
        class_Name = obj.to_dict()["__class__"]
        key_Name = class_Name+"."+id
        FileStorage.__objects[key_Name] = obj

    def save(self):

        filePath = FileStorage.__file_path
        data = dict(FileStorage.__objects)
        for key, value in data.items():
            data[key] = value.to_dict()
        with open(filePath, 'w') as f:
            json.dump(data, f)

    def reload(self):

        filePath = FileStorage.__file_path
        data = FileStorage.__objects
        if os.path.exists(filePath):
            try:
                with open(filePath) as fl:
                    for key, value in json.load(fl).items():
                        if "BaseModel" in key:
                            data[key] = BaseModel(**value)
            except Exception:
                pass

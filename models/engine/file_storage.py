#!/usr/bin/python3
"""import documontation"""
import json
from models.base_model import BaseModel

class FileStorage:
    """class documontation"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_objts = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as fl:
            json.dump(serialized_objts, fl)

    def reload(self):
        with open(self.__file_path, 'r') as f:
            loaded_objects = json.load(f)
                for key, obj_dict in loaded_objects.items():
                    class_name, obj_id = key.split('.')
                    obj = BaseModel.from_dict(obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

#!usr/bin/python3
""" user file"""
from models.base_model import BaseModel
""" import section"""
class User(BaseModel):
""" the class documentation"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
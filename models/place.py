#!/usr/bin/python3
""" Place file"""
from models.base_model import BaseModel
""" import section"""
class Place(BaseModel):
""" the class documentation"""
    name = ""
    user_id = ""
    city_id = ""
    description = ""
    number_bathrooms = 0
    price_by_night = 0
    number_rooms = 0
    longitude = 0.0
    latitude = 0.0
    max_guest = 0
    amenity_ids = []

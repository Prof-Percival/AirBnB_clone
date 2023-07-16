#!/usr/bin/python3
"""This module creates a Amenity class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity Class """

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

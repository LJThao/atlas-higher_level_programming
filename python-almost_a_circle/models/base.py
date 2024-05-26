#!/usr/bin/python3
"""Creating Class Base Module"""


import json


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Function that initializes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Function to return JSON string of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

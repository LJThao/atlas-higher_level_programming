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

    @classmethod
    def save_to_file(cls, list_objs):
        """Function to write the JSON string rep of list_objs to a file"""
        if list_objs is None:
            list_objs = []

        filename = f"{cls.__name__}.json"
        with open(filename, "w") as file:
            json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])

            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Function returning the list of JSON string rep"""
        if json_string is None or not json_string:
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Function returns an dummmy instance of assign attrs"""
        dummy = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """Function returns a list of instances"""
        file_name = f"{cls.__name__}.json"
        try:
            with open(file_name, "r") as file:
                return ([cls.create(**data) for data in cls.from_json_string(file.read())])
        except FileNotFoundError:
            return ([])

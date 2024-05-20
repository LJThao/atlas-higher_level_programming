#!/usr/bin/python3
"""This function writes an Object
to a text file, using the JSON
representation"""


import json


def save_to_json_file(my_obj, filename):
    """Function that writes an object using JSON"""

    with open(filename, "w") as f:
        json.dump(my_obj, f)

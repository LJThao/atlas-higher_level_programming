#!/usr/bin/python3
"""This function will create an
Object from a JSON file"""


import json


def load_from_json_file(filename):
    """Creating an object from a JSON file"""

    with open(filename) as f:
        return (json.load(f))

#!/usr/bin/python3
"""This function returns an object
(Python data structure)"""


import json


def from_json_string(my_str):
    """Returning an Object represented by JSON string"""

    return (json.loads(my_str))

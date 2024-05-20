#!/usr/bin/python3
"""This function returns the dictionary
description with a simple data
structure (list, dictionary, string, and
boolean) for JSON serialization of an object"""


def class_to_json(obj):
    """Function returning the dictionary desciption"""

    return (obj.__dict__)

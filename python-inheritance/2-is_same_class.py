#!/usr/bin/python3
"""This funcion returns True if the object
is exactly an instance of the specified class;
otherwise False"""


def is_same_class(obj, a_class):
    """function used for returning the object"""

    return (type(obj) is a_class)

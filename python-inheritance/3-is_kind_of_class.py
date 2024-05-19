#!/usr/bin/python3
"""This function will return True if the object
is an instance of, or if the object is an instance
of a class that inherited from, the specified class"""


def is_kind_of_class(obj, a_class):
    """Returning the function"""

    return (isinstance(obj, a_class))

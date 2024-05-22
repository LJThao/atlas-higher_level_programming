#!/usr/bin/python3
"""This function will write a
class BaseGeometry (based on
6-base_geometry.py)"""


class BaseGeometry():
    """Class BaseGeometry"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function that validates a value"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

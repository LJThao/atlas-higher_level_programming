#!/usr/bin/python3
"""This function will write a
class Rectangle that inherits from
BaseGeometry (7-base_geometry.py)"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle"""

    def __init__(self, width, height):
        """Function that validates width and height"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

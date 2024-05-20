#!/usr/bin/python3
"""This function will write a
class Rectangle that inherits from
BaseGeometry (7-base_geometry.py)"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle"""

    def __init__(self, width, height):
        """Function that validates"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        """Function that return a string the following
        rectangle description"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)

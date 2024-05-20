#!/usr/bin/python3
"""This function will write a
class Square that inherits from
Rectangle (9-rectangle.py)"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size):
        """Function that validates"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

#!/usr/bin/python3
"""
Coordinates of a square: Write a class Square
"""


class Square:
    """Class defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def __str__(self):
        self.my_print()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError('size must be an integer')

        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')

        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')

        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value

    def area(self):
        return self.__size ** 2

    def pos_print(self):
        s_position = ""
        if self.size == 0:
            return "\n"

        for n in range(self.position[1]):
            s_position += "\n"

        for n in range(self.size):
            for x in range(self.position[0]):
                s_position += " "

            for y in range(self.size):
                s_position += "#"

            s_position += "\n"

        return s_position

    def my_print(self):
        print(self.pos_print(), end='')

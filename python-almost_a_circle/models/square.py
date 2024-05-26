#!/usr/bin/python3
"""Created Class Square Module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Function that initializes a new instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returning format string
        [Square] (<id>) <x>/<y> - <size>"""
        return ("[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.width)
        )

    @property
    def size(self):
        """Function for the size of the square"""
        return (self.width)

    @size.setter
    def size(self, value):
        """Function to validate the same value"""
        self.width = value
        self.height = value

#!/usr/bin/python3
"""Created Class Rectangle Module"""


from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Assigning arguments to attributes"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Function for width of rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        self.validate_integers("width", value, False)
        self.__width = value

    @property
    def height(self):
        """Function for height of rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        self.validate_integers("height", value, False)
        self.__height = value

    @property
    def x(self):
        """Function for x of rectangle"""
        return (self.__x)

    @x.setter
    def x(self, value):
        self.validate_integers("x", value, True)
        self.__x = value

    @property
    def y(self):
        """Function for y of rectangle"""
        return (self.__y)

    @y.setter
    def y(self, value):
        self.validate_integers("y", value, True)
        self.__y = value

    def validate_integers(self, name, value, eq):
        """Validating integers"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if eq:
            if value < 0:
                raise ValueError(f"{name} must be >= 0")
        else:
            if value <= 0:
                raise ValueError(f"{name} must be > 0")
    
    def area(self):
        """Function that returns the area value of Rectangle"""
        return (self.width * self.height)

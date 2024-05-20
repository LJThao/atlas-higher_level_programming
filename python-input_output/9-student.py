#!/usr/bin/python3
"""This function will write
a class Student that defines
a student"""


class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        """Function for instance attributes"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Function to retrieve a dictionary representation 
        of a Student"""

        return (self.__dict__)

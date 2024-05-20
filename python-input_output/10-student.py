#!/usr/bin/python3
"""Function to write a class
Student that defines a student by:
(based on 9-student.py)"""


class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        """Function for instance attributes"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self, attrs=None):
        """Function to retrieve a dictionary representation
        of a Student instance"""

        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return (self.__dict__)

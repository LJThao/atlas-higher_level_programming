#!/usr/bin/python3
"""This function will write a class
Student that defines a student by:
(based on 10-student.py)"""


class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        """Function for instance attributes"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Function that retrieves a dictionary rep of a
        Student instance"""

        if (
            isinstance(attrs, list)
            and all(isinstance(attr, str) for attr in attrs)
        ):
            return {
                attr: getattr(self, attr) for attr in attrs 
                if hasattr(self, attr)
            }

        return (self.__dict__)

    def reload_from_json(self, json_data):
        """Function to replace all attributes of the Student
        instance"""

        for key, value in json_data.items():
            setattr(self, key, value)

#!/usr/bin/python3
"""This function will write a string
to a text file (UTF8)"""


def write_file(filename="", text=""):
    """Writing a string and returning chars"""

    with open(filename, "w") as f:
        return (f.write(text))

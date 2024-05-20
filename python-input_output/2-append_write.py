#!/usr/bin/python3
"""This function will append a
string at the end of the text file
(UTF8)"""


def append_write(filename="", text=""):
    """Append a string and return chars"""

    with open(filename, "a") as f:
        return f.write(text)

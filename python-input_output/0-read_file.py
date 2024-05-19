#!/usr/bin/python3
"""This function will read a text
file (UTF8) and print to stdout"""


def read_file(filename=""):
    """Function to read UTF8 file"""

    with open(filename) as f:
        print(f.read(), end="")

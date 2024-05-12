#!/usr/bin/python3
"""Test indentation"""


def text_indentation(text):
    """A function that prints a text with 2 new lines"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    space = ""
    for char in text:
        space += char
        if char in ['.', '?', ':']:
            print(space)

#!/usr/bin/python3
"""Print square"""


def print_square(size):
   """A function that prints a square"""

   if not isinstance(size, int):
            raise TypeError("size must be an integer")
   if size < 0:
            raise ValueError("size must be >= 0")
   if isinstance(size, float) and size < 0:
            raise ValueError("size must be an integer")
   for _ in range(size):
            print(f"#" * size)

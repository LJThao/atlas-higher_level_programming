#!/usr/bin/python3
"""Writing a class MyList that inherits from list"""


class MyList(list):
   """Class MyList inherits"""

   def print_sorted(self):
    """Prints the list and sorted ascendingly"""

    print(sorted(self))

#!/usr/bin/python3
"""Max integer - Unittest
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Defining tests for max integer in a list"""

    def max_end(self):
        """function for max at the end"""

        self.assertEqual(max_integer([13, -4, 300, 35]), 300)
        
    def max_begin(self):
        """function for max at the beginning"""

        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        
    def max_mid(self):
        """function for max in the middle"""

        self.assertEqual(max_integer([1, 4, 2, 3]), 2)
        
    def one_int(self):
        """function for one int"""

        self.assertEqual(max_integer([5]), 5)
    
    def same_int(self):
        """function for same int"""

        self.assertEqual(max_integer([50, 2024, 2024]), 2024)
        
    def no_int(self):
        """function for empty list"""

        self.assertEqual(max_integer([]), None)
        
    def neg_int(self):
        """function for negative int"""

        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -4)
    
    def zero_int(self):
        """function for 0 int"""

        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

if __name__ == "__main__":
    unittest.main()

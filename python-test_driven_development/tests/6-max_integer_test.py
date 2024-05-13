#!/usr/bin/python3
"""Max integer - Unittest
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Defining tests for max integer in a list"""

    def test_max_end(self):
        """function for max at the end"""

        self.assertEqual(max_integer([20, -10, 55, 310]), 310)
        
    def test_max_begin(self):
        """function for max at the beginning"""

        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        
    def test_max_mid(self):
        """function for max in the middle"""

        self.assertEqual(max_integer([1, 4, 2, 3]), 4)
        
    def test_one_int(self):
        """function for one int"""

        self.assertEqual(max_integer([10]), 10)
    
    def test_same_int(self):
        """function for same int"""

        self.assertEqual(max_integer([100, 2024, 2024]), 2024)
        
    def test_no_int(self):
        """function for empty list"""

        self.assertEqual(max_integer([]), None)
        
    def test_neg_int(self):
        """function for negative int"""

        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)
    
    def test_zero_int(self):
        """function for 0 int"""

        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

if __name__ == "__main__":
    unittest.main()

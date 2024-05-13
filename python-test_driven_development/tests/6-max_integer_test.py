#!/usr/bin/python3
"""Module to find the max integer in a list
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def max_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        
    def max_begin(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        
    def max_mid(self):
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)
        
    def one_int(self):
        self.assertEqual(max_integer([4]), 4)
    
    def same_int(self):
        self.assertEqual(max_integer([5, 5, 5, 5, 5]), 5)
        
    def no_int(self):
        self.assertEqual(max_integer([]), None)
        
    def neg_int(self):
        self.assertEqual(max_integer([-4, -5, -6, -7, -8]), -4)

#!/usr/bin/python3
"""Class Base Module Tests"""


import unittest
from models.base import Base


# Task 1 - Base Class Test
class TestBase(unittest.TestCase):
    """Class to test the Base Class"""
    def test_ids(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertNotEqual(b1.id, b2.id)
        self.assertNotEqual(b2.id, b3.id)
        self.assertNotEqual(b1.id, b3.id)
    
    def test_id_add(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id +1, b2.id)
    
    def test_specific_id(self):
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

if __name__ == "__main__":
    unittest.main()

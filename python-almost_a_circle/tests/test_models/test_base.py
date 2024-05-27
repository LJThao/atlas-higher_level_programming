#!/usr/bin/python3
"""Class Base Module Tests"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


# Tests for Base Module
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

    def test_base_json_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])

        self.assertEqual(dictionary, {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8})
        self.assertIsInstance(dictionary, dict)
        self.assertEqual(json_dictionary, '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]')
        self.assertIsInstance(json_dictionary, str)

if __name__ == "__main__":
    unittest.main()

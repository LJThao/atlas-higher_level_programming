#!/usr/bin/python3
"""Module Tests"""


import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


# Tests for Modules
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

        expected_dict = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}

        json_list = json.loads(json_dictionary)

        self.assertEqual(dictionary, expected_dict)
        self.assertIsInstance(dictionary, dict)
        self.assertEqual(json_list, [expected_dict])
        self.assertIsInstance(json_dictionary, str)

    def test_to_json_string_none(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_string_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

    def test_from_json_string_none(self):
        json_string = None
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [])

class TestRectangle(unittest.TestCase):
    """Class to test the Rectangle"""
    def setUp(self):
        self.rectangle1 = Rectangle(10, 7, 2, 8)
        self.rectangle2 = Rectangle(2, 4)
        Rectangle.save_to_file([self.rectangle1, self.rectangle2])

        file_name = "Rectangle.json"
        if not os.path.exists(file_name):
            with open(file_name, "w") as file:
                file.write("[]")

    def tearDown(self):
        file_name = "Rectangle.json"
        if os.path.exists(file_name):
            os.remove(file_name)

    def test_save_to_file(self):
        file_name = "Rectangle.json"
        with open("Rectangle.json", "r") as file:
            data = file.read()
        expected_output = [
            {"id": self.rectangle1.id, "width": 10, "height": 7, "x": 2, "y": 8},
            {"id": self.rectangle2.id, "width": 2, "height": 4, "x": 0, "y": 0}
        ]
        self.assertEqual(json.loads(data), expected_output)

    def test_rectangle_inv_args(self):
        cases = [
            ("1", 2), (1, "2"), (1, 2, "3"), (1, 2, 3, "4"), (-1, 2), (1, -2),
            (0, 2), (1, 0), (1, 2, -3), (1, 2, 3, -4)
            ]
        for args in cases:
            with self.assertRaises((TypeError, ValueError)):
                Rectangle(*args)

    def test_rectangle_more_inv_args(self):
        self.assertEqual(5, Rectangle(1, 2, 3, 4, 5).id)

    def test_rectangle_area(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)
    
    def test_rectangle_str_method(self):
        r = Rectangle(5, 10, 1, 2, 99)
        self.assertEqual(str(r), "[Rectangle] (99) 1/2 - 5/10")

class TestSquare(unittest.TestCase):
    """Class to test the Square"""
    def test_init(self):
        s1, s2, s3, s4 = Square(1), Square(1, 2), Square(1, 2, 3), Square(1, 2, 3, 4)
        self.assertEqual((s1.size, s1.x, s1.y), (1, 0, 0))
        self.assertEqual((s2.size, s2.x, s2.y), (1, 2, 0))
        self.assertEqual((s3.size, s3.x, s3.y), (1, 2, 3))
        self.assertEqual((s4.size, s4.x, s4.y, s4.id), (1, 2, 3, 4))

        for args in [("1",), (1, "2"), (1, 2, "3"), (-1,), (1, -2), (1, 2, -3), (0,)]:
            with self.assertRaises((TypeError, ValueError)):
                Square(*args)

if __name__ == '__main__':
    unittest.main()

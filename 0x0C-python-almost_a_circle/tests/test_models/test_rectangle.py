#!/usr/bin/python3
""" 0-main """
import unittest

from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_case1_id(self):
        assert(Rectangle(10, 2).id) == 1
    def test_case2_id(self):
        assert(Rectangle(2, 10).id) == 2
    def test_case3_id(self):
        assert(Rectangle(10, 2, 0, 0, 12).id) == 12
    def test_case4_excep(self):
        Rectangle(10, "2")
        self.assertRaisesRegex(TypeError, "height must be an integer")
    def test_case5_excep(self):
        r=Rectangle(10, 2)
        r.width=-10
        self.assertRaisesRegex(ValueError, "width must be > 0")
    def test_case6_excep(self):
        r=Rectangle(10, 2)
        r.x={}
        self.assertRaisesRegex(TypeError, "x must be an integer")
    def test_case7_excep(self):
        r=Rectangle(10, 2, 3, -1)
        self.assertRaisesRegex(ValueError, "y must be >= 0")

#!/usr/bin/python3
"""
Defines unittest for models/rectangle.py
Unittest classes:
    TestRectangle_instances
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instances(unittest.TestCase):
    """
    Unittests for testing instantiation of the Rectangle class
    """

    def test_rectangle_is_base(self):
        """
        Test if Rectangle is a subclass of Base
        """
        self.assertIsInstance(Rectangle(10, 2), Base)

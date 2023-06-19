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
        Checks if Rectangle is a subclass of Base
        """
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        """
        Checks exceptions for an empty arg when func is called
        """
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        """
        Checks any error detection in case of 1 arg
        """
        with self.assertRaises(TypeError):
            Rectangle(5)

    def test_two_args(self):
        """
        Checks for id when the function call is done
        with two args
        """
        r1 = Rectangle(5, 3)
        r2 = Rectangle(4, 9)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        """
        Checks for id when the function call is done
        with three args
        """
        r1 = Rectangle(5, 3, 3)
        r2 = Rectangle(4, 6, 8)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        """
        Checks for id when the function call is done
        with four args
        """
        r1 = Rectangle(5, 3, 3, 8)
        r2 = Rectangle(4, 6, 8, 9)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        """
        Checks for id when the function call is done
        with five args
        """
        r1 = Rectangle(5, 3, 3, 8, 2)
        self.assertEqual(r1.id, 2)

    def test_more_than_five_args(self):
        """
        Checks if an error message is raised if
        arguments are beyond the required specifications
        """
        with self.assertRaises(TypeError):
            Rectangle(5, 3, 3, 8, 2, 7)

    def test_width_private(self):
        """
        checks if width is a private instance attribute
        """
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 3, 3, 8, 2).__width)

    def test_height_private(self):
        """
        Checks if height is a private instance attribute
        """
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 3, 3, 8, 2).__height)

    def test_x_private(self):
        """
        Checks if x-coordinate is a private instance attribute
        """
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 3, 3, 8, 2).__x)

    def test_y_private(self):
        """
        Check if y-coordinate is a private instance attribute
        """
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 3, 3, 8, 2).__y)

    def test_width_getter(self):
        """
        Returns the called value of width
        """
        r1 = Rectangle(5, 3, 3, 8, 2)
        self.assertEqual(r1.width, 5)

    def test_width_setter(self):
        """
        Sets the new value of width
        """
        r1 = Rectangle(5, 3, 3, 8, 2)
        r1.width = 7
        self.assertEqual(r1.width, 7)

    def test_height_getter(self):
        """
        Returns the called value of the height
        """
        r1 = Rectangle(5, 3, 3, 8, 2)
        self.assertEqual(r1.height, 3)

    def test_height_setter(self):
        """
        Sets the new value of the height
        """
        r1 = Rectangle(5, 3, 3, 8, 2)
        r1.height = 9
        self.assertEqual(r1.height, 9)

    def test_x_getter(self):
        """
        Returns the called value of x
        """
        r1 = Rectangle(5, 3, 3, 8, 2)
        self.assertEqual(r1.x, 3)

    def test_x_setter(self):
        """
        Sets the new value of x
        """
        r1 = Rectangle(5, 3, 3, 8, 2)
        r1.x = 8
        self.assertEqual(r1.x, 8)

    def test_y_getter(self):
        """
        Returns the called value for y coordinate
        """
        r1 = Rectangle(5, 3, 3, 8, 2)
        self.assertEqual(r1.y, 8)

    def test_y_setter(self):
        """
        Sets the new value of y coordinate
        """
        r1 = Rectangle(5, 3, 3, 8, 2)
        r1.y = 9
        self.assertEqual(r1.y, 9)

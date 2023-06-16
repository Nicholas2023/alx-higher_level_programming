#!/usr/bin/python3
"""
Contains unittest for base.py
Unittest classes:
    TestBase
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unittest for testing instantiation of the Base class"""
    def test_no_arg(self):
        """
        Tests for instances without argument
        """
        c1 = Base()
        c2 = Base()
        c3 = Base()
        self.assertEqual(c1.id, c2.id - 1)
        self.assertEqual(c1.id, c3.id - 2)

    def test_None(self):
        """
        Tests for instances with `None` as argument
        """
        c1 = Base(None)
        c2 = Base(None)
        c3 = Base(None)
        self.assertEqual(c1.id, c2.id - 1)
        self.assertEqual(c1.id, c3.id - 2)

    def test_unique_id(self):
        """
        Tests for instances with unique id entries
        """
        c1 = Base(3)
        c2 = Base()
        c3 = Base()
        self.assertEqual(c1.id, 3)
        self.assertEqual(c2.id, c3.id - 1)

    def test_id_public(self):
        """
        Tests for instances with public id entries
        """
        c1 = Base(3)
        c1.id = 7
        self.assertEqual(c1.id, 7)

    def test_nb_instance_private(self):
        """
        Tests for private id entry feature
        """
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_str_id(self):
        """
        Tests for strings as id entry
        """
        c1 = Base('Nick')
        self.assertEqual(c1.id, 'Nick')

    def test_float_id(self):
        """
        Tests for floats as id entry
        """
        c1 = Base(1.5)
        self.assertEqual(c1.id, 1.5)

    def test_complex_id(self):
        """
        Tests for complex numbers as id entries
        """
        c1 = Base(complex(9))
        self.assertEqual(c1.id, complex(9))

    def test_dict_id(self):
        """
        Tests for dictionaries as id entries
        """
        c1 = Base({'age': 12})
        self.assertEqual(c1.id, {'age': 12})

    def test_bool_id(self):
        """
        Tests for booleans as id entries
        """
        c1 = Base(True)
        self.assertEqual(c1.id, True)

    def test_list_id(self):
        """
        Tests for lists as id entry
        """
        c1 = Base([1, 2, 3])
        self.assertEqual(c1.id, [1, 2, 3])

    def test_tuple(self):
        """
        Tests for tuples as id entry
        """
        c1 = Base((1, 2, 3))
        self.assertEqual(c1.id, (1, 2, 3))

    def test_set_id(self):
        """
        Tests for sets as id entry
        """
        c1 = Base({1, 2, 3})
        c2 = Base(frozenset({1, 2, 3}))
        self.assertEqual(c1.id, {1, 2, 3})
        self.assertEqual(c2.id, frozenset({1, 2, 3}))

    def test_range_id(self):
        """
        Tests for range as id entry
        """
        c1 = Base(range(3))
        self.assertEqual(c1.id, range(3))

    def test_bytes_id(self):
        """
        Test for bytes as id entry
        """
        c1 = Base(b'Python')
        c2 = Base(bytearray(b'abcefg'))
        self.assertEqual(c1.id, b'Python')
        self.assertEqual(c2.id, bytearray(b'abcefg'))

    def test_memoryview_id(self):
        """
        Tests for memview as id entry
        """
        c1 = Base(memoryview(b'abcefg'))
        self.assertEqual(c1.id, memoryview(b'abcefg'))

    def test_inf_id(self):
        """
        Tests for infinity as an id entry
        """
        c1 = Base(float('inf'))
        self.assertEqual(c1.id, float('inf'))

    def test_NaN_id(self):
        """
        Tests for a NaN as an id entry
        """
        c1 = Base(float('nan'))
        self.assertNotEqual(c1.id, float('nan'))

    def test_two_args(self):
        """
        Tests for entry of more than one argument id
        """
        with self.assertRaises(TypeError):
            Base(1, 2)


if __name__ == '__main__':
    unittest.main()

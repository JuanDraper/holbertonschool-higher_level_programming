#!/usr/bin/python3
"""
Unittest square.
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """testing"""

    def test_empty(self):
        """empty instantiation. """
        with self.assertRaises(TypeError):
            s = Square()

    def test_more_arguments(self):
        """instantiation with 1 more argument. """
        with self.assertRaises(TypeError):
            s = Square(1, 1, 1, 1, 1)

    def test_correct_inst(self):
        """correct instantiation. """
        s = Square(3, 1, 2, 45)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 45)

    def test_str_rep(self):
        """string representation of a square. """
        s = Square(3, 1, 2, 45)
        self.assertEqual(s.__str__(), "[Square] (45) 1/2 - 3")

    def test_size_setter(self):
        """size setter of square class. """
        s = Square(3, 1, 2, 45)
        s.size = 27
        self.assertEqual(s.size, 27)

    def test_update(self):
        """update method of square. """
        s = Square(3, 1, 2, 45)
        s.update(12, 5, 5, 8)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 8)
        self.assertEqual(s.id, 12)
        s.update(23)
        self.assertEqual(s.id, 23)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 8)
        s.update(y=4, x=12, size=8, id=6)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.x, 12)
        self.assertEqual(s.y, 4)
        self.assertEqual(s.id, 6)
        s.update(x=1)
        self.assertEqual(s.x, 1)
        s.update(6, x=23)
        self.assertEqual(s.id, 6)
        self.assertEqual(s.x, 1)

    def test_to_dict(self):
        """dictionary function. """
        s = Square(3, 1, 2, 45)
        s_d = s.to_dictionary()
        self.assertDictEqual(s_d, {'x': 1, 'size': 3, 'id': 45, 'y': 2})

    def test_wrong_size(self):
        """ wrong type for size. """
        with self.assertRaises(TypeError):
            s = Square("nope")

    def test_size_zero(self):
        """size of zero. """
        with self.assertRaises(ValueError):
            s = Square(0)

    def test_wrong_type_x(self):
        """wrong type for x. """
        with self.assertRaises(TypeError):
            s = Square(10, "nope")

    def test_wrong_type_y(self):
        """wrong type for y. """
        with self.assertRaises(TypeError):
            s = Square(10, "nope")

    def test_size_neg(self):
        """negative size. """
        with self.assertRaises(ValueError):
            s = Square(-1)

    def test_x_neg(self):
        """negative x. """
        with self.assertRaises(ValueError):
            s = Square(1, -1)

    def test_y_neg(self):
        """negative y. """
        with self.assertRaises(ValueError):
            s = Square(1, 1, -1)

    def test_to_dict_with_arg(self):
        """to_dictionary function with argument. """
        s = Square(2)
        with self.assertRaises(TypeError):
            s.to_dictionary(1) 

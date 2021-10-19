#!/usr/bin/python3
"""
Unittest for Rectangle.
"""
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """testing"""

    def test_empty(self):
        """empty instantiation. """
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_more_arguments(self):
        """instantiation with 1 more argument. """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, 1, 1, 1, 1)

    def test_less_arguments(self):
        """less arguments than required. """
        with self.assertRaises(TypeError):
            r = Rectangle(1)

    def test_correct_inst(self):
        """correct instantiation. """
        r = Rectangle(3, 5, 1, 2, 45)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 45)
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_wrong_type_width(self):
        """wrong type for width. """
        with self.assertRaises(TypeError):
            r = Rectangle("nope", 5)

    def test_wrong_type_height(self):
        """wrong type for height. """
        with self.assertRaises(TypeError):
            r = Rectangle(5, "nope")

    def test_wrong_type_x(self):
        """wrong type for x. """
        with self.assertRaises(TypeError):
            r = Rectangle(10, 5, "nope")

    def test_wrong_type_y(self):
        """wrong type for y. """
        with self.assertRaises(TypeError):
            r = Rectangle(10, 5, 1, "nope")

    def test_width_zero(self):
        """width of 0. """
        with self.assertRaises(ValueError):
            r = Rectangle(0, 5)

    def test_height_zero(self):
        """height of 0. """
        with self.assertRaises(ValueError):
            r = Rectangle(10, 0)

    def test_width_neg(self):
        """negative width. """
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 5)

    def test_height_neg(self):
        """negative height. """
        with self.assertRaises(ValueError):
            r = Rectangle(5, -1)

    def test_x_neg(self):
        """negative x. """
        with self.assertRaises(ValueError):
            r = Rectangle(1, 5, -1)

    def test_y_neg(self):
        """negative y. """
        with self.assertRaises(ValueError):
            r = Rectangle(1, 5, 1, -1)

    def test_setters_ok(self):
        """setters with good values. """
        r = Rectangle(1, 5)
        r.width = 2
        r.height = 6
        r.x = 3
        r.y = 4
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_width_setter_wrong(self):
        """wrong type for width setter. """
        r = Rectangle(1, 5)
        with self.assertRaises(TypeError):
            r.width = "nope"

    def test_height_setter_wrong(self):
        """wrong type for height setter. """
        r = Rectangle(1, 5)
        with self.assertRaises(TypeError):
            r.height = "nope"

    def test_x_setter_wrong(self):
        """wrong type for x setter. """
        r = Rectangle(1, 5)
        with self.assertRaises(TypeError):
            r.x = "nope"

    def test_y_setter_wrong(self):
        """wrong type for y setter. """
        r = Rectangle(1, 5)
        with self.assertRaises(TypeError):
            r.y = "nope"

    def test_width_setter_zero(self):
        """0 for width setter. """
        r = Rectangle(1, 5)
        with self.assertRaises(ValueError):
            r.width = 0

    def test_height_setter_zero(self):
        """0 for height setter. """
        r = Rectangle(1, 5)
        with self.assertRaises(ValueError):
            r.height = 0

    def test_width_setter_negative(self):
        """negative for width setter. """
        r = Rectangle(1, 5)
        with self.assertRaises(ValueError):
            r.width = -1

    def test_height_setter_negative(self):
        """negative for height setter. """
        r = Rectangle(1, 5)
        with self.assertRaises(ValueError):
            r.height = -1

    def test_x_setter_negative(self):
        """negative for x setter. """
        r = Rectangle(1, 5)
        with self.assertRaises(ValueError):
            r.x = -1

    def test_y_setter_negative(self):
        """negative for y setter. """
        r = Rectangle(1, 5)
        with self.assertRaises(ValueError):
            r.y = -1

    def test_area_with_arg(self):
        """calling area function with argument. """
        r = Rectangle(1, 5)
        with self.assertRaises(TypeError):
            r.area(1)

    def test_area_ok(self):
        """area function. """
        r = Rectangle(5, 7)
        rr = Rectangle(1, 2)
        rrr = Rectangle(10, 5)
        self.assertEqual(r.area(), 35)
        self.assertEqual(rr.area(), 2)
        self.assertEqual(rrr.area(), 50)

    def test_display_with_arg(self):
        """display function with argument. """
        r = Rectangle(2, 1)
        with self.assertRaises(TypeError):
            r.display(1)

    def test_display_ok(self):
        """display function. """
        r = Rectangle(2, 3, 1, 1)
        o1 = StringIO()
        with redirect_stdout(o1):
            r.display()
            self.assertEqual(o1.getvalue(), "\n ##\n ##\n ##\n")

    def test_str_rep(self):
        """string representation of a rectangle. """
        r = Rectangle(3, 5, 1, 2, 45)
        self.assertEqual(r.__str__(), "[Rectangle] (45) 1/2 - 3/5")

    def test_update(self):
        """update method of rectangle. """
        r = Rectangle(3, 5, 1, 2, 45)
        r.update(12, 9, 5, 5, 8)
        self.assertEqual(r.width, 9)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 8)
        self.assertEqual(r.id, 12)
        r.update(23)
        self.assertEqual(r.id, 23)
        self.assertEqual(r.width, 9)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 8)
        r.update(y=4, x=12, width=8, id=6, height=99)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 99)
        self.assertEqual(r.x, 12)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 6)
        r.update(x=1)
        self.assertEqual(r.x, 1)
        r.update(6, x=23)
        self.assertEqual(r.id, 6)
        self.assertEqual(r.x, 1)

    def test_to_dict(self):
        """to dictionary function. """
        r = Rectangle(3, 5, 1, 2, 45)
        r_d = r.to_dictionary()
        d = {'x': 1, 'width': 3, 'id': 45, 'y': 2, 'height': 5}
        self.assertDictEqual(r_d, d)

    def test_to_dict_with_arg(self):
        """to_dictonary function with argument. """
        r = Rectangle(2, 1)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)

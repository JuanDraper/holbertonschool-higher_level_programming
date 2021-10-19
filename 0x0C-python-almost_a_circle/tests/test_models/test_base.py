#!/usr/bin/python3
"""
Unittest for the class base.
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """testing"""

    def test_empty(self):
        """empty instantiation. """
        b = Base()
        self.assertEqual(b.id, 1)

    def test_more_arguments(self):
        """instantiation with 1 more argument. """
        with self.assertRaises(TypeError):
            s = Base(1, 1)

    def test_give_id(self):
        """instance with a specific id. """
        b = Base(500)
        self.assertEqual(b.id, 500)

    def test_to_json_no_args(self):
        """to_json_string without args. """
        r = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r.to_json_string()

    def test_to_json_more_args(self):
        """to_json_string with more args. """
        r = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r.to_json_string([], [])

    def test_to_json_empty(self):
        """to_json_string with empty list and None. """
        r = Rectangle(1, 1)
        self.assertEqual(r.to_json_string([]), "[]")
        self.assertEqual(r.to_json_string(None), "[]")

    def test_save_to_file_no_args(self):
        """save_to_file with no arguments. """
        r = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r.save_to_file()

    def test_save_to_file_more_args(self):
        """save_to_file with more arguments. """
        r = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r.save_to_file([], [])

    def test_save_to_file_empty(self):
        """save_to_file with empty list and None. """
        r = Rectangle(1, 1)
        if os.path.isfile("Rectangle.json"):
            os.remove("Rectangle.json")
        r.save_to_file([])
        self.assertTrue(os.path.isfile("Rectangle.json"))

    def test_save_to_file_csv_empty(self):
        """save_to_file_csv with empty list and None. """
        r = Rectangle(1, 1)
        if os.path.isfile("Rectangle.csv"):
            os.remove("Rectangle.csv")
        r.save_to_file_csv([])
        self.assertTrue(os.path.isfile("Rectangle.csv"))

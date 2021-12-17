#!/usr/bin/python3
"""blablalba
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """blalblalba
    """
    def test_1(self):
        """blbalbla"""
        self.assertEqual(max_integer([]), None)

    def test_2(self):
        """blblalal"""
        self.assertEqual(max_integer([]), None)
    def test_3(self):
        """bllalbal"""
        self.assertEqual(max_integer([-5]), -5)
    def test_4(self):
        """blalbal"""
        self.assertEqual(max_integer(), None)
    def test_5(self):
        """blablalb"""
        self.assertEqual(max_integer([2, 1]), 2)
    def test_6(self):
        """blablal"""
        self.assertEqual(max_integer([1, 3, 2]), 3)
    def test_7(self):
        """blablal"""
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

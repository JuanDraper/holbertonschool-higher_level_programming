#!/usr/bin/python3
"""this module contains Mylist
"""


class MyList(list):
    """ class inheriting from list"""
    def print_sorted(self):
        """ prints a sorted list"""
        l2 = self.copy()
        l2.sort()
        print(l2)

#!/usr/bin/python3
"""
    blablalblal

"""


def add_integer(a, b=98):
    """lalbala"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if a + 1 == a or b + 1 == b:
        raise OverflowError("Number too large")
    return int(a) + int(b)

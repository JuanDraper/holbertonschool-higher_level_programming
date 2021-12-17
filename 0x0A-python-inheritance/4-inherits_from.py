#!/usr/bin/python3
"""module contains the function.
"""


def inherits_from(obj, a_class):
    """
    returns True if the object is an instance of a class that
    inherited from the class. otherwise False.
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)

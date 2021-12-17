#!/usr/bin/python3
"""module containing class to json
"""


def class_to_json(obj):
    """ returns dictionary description.
    """
    return obj.__dict__

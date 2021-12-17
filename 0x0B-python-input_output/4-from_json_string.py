#!/usr/bin/python3
"""
module containing from_json_string.
"""
import json


def from_json_string(my_str):
    """ returns the object represented.
    """
    return json.loads(my_str)

#!/usr/bin/python3
"""
module containing load_from_json.
"""
import json


def load_from_json_file(filename):
    """ loads an object from json.
    """
    with open(filename, "r", encoding='utf-8') as f:
        return json.load(f)

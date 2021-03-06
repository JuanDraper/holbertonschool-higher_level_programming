#!/usr/bin/python3
"""
module containing  save_to_json_file.
"""
import json


def save_to_json_file(my_obj, filename):
    """saves the json object in file.
    """
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(my_obj, f)

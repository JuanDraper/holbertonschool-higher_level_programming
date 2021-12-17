#!/usr/bin/python3
"""
odule containing read_file.
"""


def read_file(filename=""):
    """reads the file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
            print(f.read(), end="")

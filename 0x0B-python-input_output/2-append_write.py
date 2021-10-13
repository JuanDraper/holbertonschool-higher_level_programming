#!/usr/bin/python3
"""
module containing append_write.
"""


def append_write(filename="", text=""):
    """
    Appends to a file 
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)

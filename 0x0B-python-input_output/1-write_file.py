#!/usr/bin/python3
"""module containing the write_file.
"""


def write_file(filename="", text=""):
    """
    Writes into files.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)

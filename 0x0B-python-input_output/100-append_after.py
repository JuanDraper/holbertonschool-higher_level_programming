#!/usr/bin/python3
"""module contains append_after.
"""


def append_after(filename="", search_string="", new_string=""):
    """ appends a string after another one found.
    """
    with open(filename, "r", encoding='utf-8') as f:
        c = f.readlines()
    i = 0
    while i < len(c):
        if c[i].find(search_string) >= 0:
            i += 1
            c.insert(i, new_string)
        i += 1
    with open(filename, "w", encoding='utf-8') as f:
        f.writelines(c)

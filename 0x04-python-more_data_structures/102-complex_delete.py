#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return None
    for i, j in dict(a_dictionary).items():
        if j == value:
            del a_dictionary[i]
    return a_dictionary

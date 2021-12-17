#!/usr/bin/python3
"""blabla
"""


def text_indentation(text):
    """blalbalba"""
    nl = 1
    sp = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
    for char in text:
        if char == ' ':
            sp += 1
        elif char == '.' or char == '?' or char == ':':
            if not nl:
                print(" " * sp, end="")
            print(char + "\n")
            nl = 1
        elif not nl:
            print(" " * sp + char, end="")
            sp = 0
        else:
            print(char, end="")
            nl = 0
            sp = 0
                       

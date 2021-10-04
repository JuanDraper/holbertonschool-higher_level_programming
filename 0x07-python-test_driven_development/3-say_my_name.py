#!/usr/bin/python3
"""blalbalblal

"""


def say_my_name(first_name, last_name=""):
    """blablabla"""

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is " + first_name, end="")
    if last_name is not "":
        print(" ", end="")
    print(last_name)

#!/usr/bin/python3
"""bllbablal
"""


class Square:
    """Square class
      Defining a square
       return size
    """
    def __init__(self, size=0):
        """blablalbla
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """blalbab"""
        return self.__size ** 2

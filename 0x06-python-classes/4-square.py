#!/usr/bin/python3
"""
    blalblaba
"""


class Square():
    """blalbalba"""

    def __init__(self, size=0):
        """blalblbla"""
        self.size = size

    def area(self):
        """blblalbla"""
        return self.__size ** 2

    @property
    def size(self):
        """blallabla"""
        return self.__size

    @size.setter
    def size(self, value):
        """bllblablal"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

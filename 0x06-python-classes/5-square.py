#!/usr/bin/python3
"""
    blablalblal
"""


class Square():
    """blablla"""

    def __init__(self, size=0):
        """bllbalbla"""
        self.size = size

    def area(self):
        """blablalbla"""
        return self.__size ** 2

    @property
    def size(self):
        """bññbñañbañña"""
        return self.__size

    @size.setter
    def size(self, value):
        """blalbalba"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """bllalblalbal"""
        if self.__size == 0:
            print()
            return
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()

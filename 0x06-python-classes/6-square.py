#!/usr/bin/python3
"""
    blalblabla
"""


class Square():
    """blblalbal"""

    def __init__(self, size=0, position=(0, 0)):
        """blblalla"""
        self.size = size
        self.position = position

    def area(self):
        """blablal"""
        return self.__size ** 2

    @property
    def size(self):
        """blblala"""
        return self.__size

    @size.setter
    def size(self, value):
        """blabllalaa"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """blallbal"""
        if self.__size == 0:
            print()
            return
        for row in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for space in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()

    @property
    def position(self):
        """blabla"""
        return self.__position

    @position.setter
    def position(self, value):
        """blalbalba"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(not isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(num < 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

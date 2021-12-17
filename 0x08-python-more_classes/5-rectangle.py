#!/usr/bin/python3
"""blbalbla"""


class Rectangle:
    """blablalbla"""
    def __init__(self, width=0, height=0):
        """por favor mirar los docs del seba jajaajja"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """vi el de uno solo, que no recuerdo cuál es"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """pero asumo que los demas deben de ser igual"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """anda a mirarlos que son cómicos"""
        return self.__width * self.__height

    def perimeter(self):
        """blblallba"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__width + 2 * self.__height

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        my_str = ("#" * self.__width + "\n") * self.__height
        return my_str[:-1]

    def __repr__(self):
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height)\
                + ")"

    def __del__(self):
        print("Bye rectangle...")

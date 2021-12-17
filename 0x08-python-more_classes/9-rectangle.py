#!/usr/bin/python3
"""bllballllab"""


class Rectangle:
    """blalbalba"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """blalblabla"""
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
        Rectangle.number_of_instances += 1
    print_symbol = "#"

    @property
    def width(self):
        """blalbalbla"""
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
        """blablalblal"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """blalbalbla"""
        return self.__width * self.__height

    def perimeter(self):
        """blalbalblalbal """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__width + 2 * self.__height

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        my_str = (str(self.print_symbol) * self.__width + "\n") * self.__height
        return my_str[:-1]

    def __repr__(self):
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height)\
                + ")"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """blalblabla"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """blallalba"""
        return Rectangle(size, size)

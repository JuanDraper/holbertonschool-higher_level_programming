#!/usr/bin/python3
"""
module containing the  Rectangle.
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class that defines a rectangle.
    """
    def __init__(self, width, height):
        """
        Initializer for the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        method for the print()
        """
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)

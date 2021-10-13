#!/usr/bin/python3
"""
module containing the Square.
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Definition of a square
    """
    def __init__(self, size):
        """
        Initializer for the square .
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
	

    def __str__(self):
        """
        return for the print()
        """
        return "[Square] " + str(self.__size) + "/" + str(self.__size)

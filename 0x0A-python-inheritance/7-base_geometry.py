#!/usr/bin/python3
"""module containing the class BaseGeometry.
"""


class BaseGeometry:
    """
    Class that defines basic geometries.
    """
    def area(self):
        """
        Area of a geometry, will raise exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates that value is integer.
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")

#!/usr/bin/python3
"""
module containing  class BaseGeometry.
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

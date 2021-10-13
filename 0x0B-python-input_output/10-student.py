#!/usr/bin/python3
"""
module containing Student.
"""


class Student:
    """ student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializer 
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        dictionary representation.
        """
        if type(attrs) is not list:
            return self.__dict__
        ans = dict()
        for elem in attrs:
            if type(elem) is not str:
                return self.__dict__
            if elem in self.__dict__.keys():
                ans[elem] = self.__dict__[elem]
        return ans

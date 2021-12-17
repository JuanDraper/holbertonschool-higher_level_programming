#!/usr/bin/python3
"""
blalblab
"""


class MyInt(int):
    """
    class that inherits from int.
    """
    def __eq__(self, other):
        """
        Function equality.
        """
        if int(self) == int(other):
            return False
        return True

    def __ne__(self, other):
        """
        Function inequality.
        """
        return not self.__eq__(other)

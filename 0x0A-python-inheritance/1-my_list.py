#!/usr/bin/python3
"""
module containing the class MyList.
"""


class MyList(list):
    """
    Class that inherits from list.
    """
    def print_sorted(self):
        """
        prints a list sorted.
        """
        list2 = self.copy()
        list2.sort()
        print(list2)

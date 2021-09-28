#!/usr/bin/python3
"""  
    blablalblalbla
    return {}
"""


class Square:
    """
	bllbalblalbal
    """
    def __init__(self, size=0):
        """blblal."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

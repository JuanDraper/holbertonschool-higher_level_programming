#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list or my_list == []:
        return 0
    n = sum([i * j for i, j in my_list])
    d = sum([j for i, j in my_list])
    if not d:
        return 0
    return n/d

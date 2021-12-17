#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return 0
    new_list = []
    new = set(my_list)
    for i in new:
        new_list.append(i)
    return sum(new_list)

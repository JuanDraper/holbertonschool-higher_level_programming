#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    new = []
    for i in matrix:
       new.append([j ** 2 for j in i])
    return new

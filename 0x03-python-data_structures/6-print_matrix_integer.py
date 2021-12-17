#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        c = 0
        for j in i:
            c += 1
            print('{:d}'.format(j), end=(" " if c < len(i) else ""))
        print()

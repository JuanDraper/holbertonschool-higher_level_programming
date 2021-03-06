#!/usr/bin/python3
"""bllablalb
"""


def matrix_mul(m_a, m_b):
    """bllbalbla"""
    r_a = 0
    c_a = 0
    r_b = 0
    c_b = 0
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    length = []
    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        c_a = 0
        for elem in row:
            if type(elem) is not int and type(elem) is not float:
                raise TypeError("m_a should contain only integers or floats")
            c_a += 1
    for row in m_b:
        c_b = 0
        for elem in row:
            if type(elem) is not int and type(elem) is not float:
                raise TypeError("m_b should contain only integers or floats")
            c_b += 1
    for row in m_a:
        length.append(len(row))
        r_a += 1
    if not len(set(length)) <= 1:
        raise TypeError("each row of m_a must be of the same size")
    length.clear()
    for row in m_b:
        length.append(len(row))
        r_b += 1
    if not len(set(length)) <= 1:
        raise TypeError("each row of m_b must be of the same size")
    if c_a != r_b:
        raise ValueError("m_a and m_b can't be multiplied")
    new = [[0 for i in range(c_b)] for j in range(r_a)]
    for new_rows in range(r_a):
        for new_cols in range(c_b):
            for i in range(c_a):
                new[new_rows][new_cols] += m_a[new_rows][i] * m_b[i][new_cols]
    return new

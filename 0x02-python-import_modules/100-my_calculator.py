#!/usr/bin/python3
if __name__ == "__main__":
    from sys import *
    from calculator_1 import add, sub, mul, div
    argc = len(argv)
    if argc != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>\n')
        exit(1)
    if argv[2] != '+' and argv[2] != '-' and argv[2] != '*' and argv[2] != '/':
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    print('{:d} {} {:d} = {}'.format(a, argv[2], b,
                                     add(a, b) if argv[2] == '+' else
                                     sub(a, b) if argv[2] == '-' else
                                     mul(a, b) if argv[2] == '*' else
                                     div(a, b)))


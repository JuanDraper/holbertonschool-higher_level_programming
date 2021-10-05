#!/usr/bin/python3
def magic_string():
    vars(magic_string).setdefault('my', []).append("BestSchool")
    return ", ".join(magic_string.my)

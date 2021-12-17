#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return 0
    if not roman_string:
        return 0
    conv = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    l = len(roman_string) - 1
    if roman_string[l] not in conv:
        return 0
    res = conv[roman_string[l]]
    for i in range(l, 0, -1):
        if roman_string[i] not in conv:
            return 0
        curr = conv[roman_string[i]]
        if roman_string[i - 1] not in conv:
            return 0
        prev = conv[roman_string[i - 1]]
        if i > 1:
            if roman_string[i - 2] not in conv:
                return 0
            if prev < curr and conv[roman_string[i - 2]] <= prev:
                return 0
        if i > 2:
            if prev == curr and conv[roman_string[i - 2]] == prev:
                if roman_string[i - 3] not in conv:
                    return 0
                if conv[roman_string[i - 3]
                        ] == conv[roman_string[i - 2]]:
                    return 0
        res += prev if prev >= curr else -prev
    return res

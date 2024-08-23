#!/usr/bin/python3
"""
let's define if the given data is UTF-8
"""


def validUTF8(data):
    """
    check th list of integers are UTF-8
    """
    ignore = 0
    dist = len(data)
    for x in range(dist):
        if ignore > 0:
            ignore -= 1
            continue
        if type(data[x]) != int or data[x] < 0 or data[x] > 0x10ffff:
            return False
        elif data[x] <= 0x7f:
            ignore = 0
        elif data[x] & 0b11111000 == 0b11110000:
            utf_span = 4
            if dist - 1 >= utf_span:
                next_body = list(map(
                    lambda y: y & 0b11000000 == 0b10000000,
                    data[x + x: x + utf_span],
                ))
                if not all(next_body):
                    return False
                ignore = utf_span - 1
            else:
                return False
        elif data[x] & 0b11110000 == 0b11100000:
            utf_span = 3
            if dist - x >= utf_span:
                next_body = list(map(
                    lambda y: y & 0b11000000 == 0b10000000,
                    data[x + 1: x + utf_span],
                ))
                if not all(next_body):
                    return False
                ignore = utf_span - 1
            else:
                return False
        elif data[x] & 0b11100000 == 0b11000000:
            utf_span = 2
            if dist - x >= utf_span:
                next_body = list(map(
                    lambda y: y & 0b11000000 == 0b10000000,
                    data[x + 1: x + utf_span],
                ))
                if not all(next_body):
                    return False
                ignore = utf_span - 1
            else:
                return False
        else:
            return False
    return True

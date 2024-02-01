#!/usr/bin/python3
"""Defining a function validUTF8"""


def validUTF8(data):
    """determines if a given data set represents a
    valid UTF-8 encoding"""

    number_of_next_bytes = 0

    for byte in data:
        if byte >= 255:  # the number of bits is higher than 8
            return False
        if number_of_next_bytes == 0:
            if byte >> 3 == 0b11110:
                number_of_next_bytes = 3
            elif byte >> 4 == 0b1110:
                number_of_next_bytes = 2
            elif byte >> 5 == 0b1100:
                number_of_next_bytes = 1
            elif byte >> 7 != 0:  # if the byte's leftmost is 1 (starts with 1)
                # and none of the above conditions are true
                # it is definitly not a valid utf8
                return False
        # checking the next n-bytes
        else:
            # if the next byte does not start with '10' '0b10'
            if byte >> 6 != 0b10:
                return False
            number_of_next_bytes -= 1

    return number_of_next_bytes == 0
#!/usr/bin/python3
"""Defining a function named validUTF8"""


def validUTF8(data):
    """ This is a method that determines if a given data set
    -   represents a valid UTF-8 encoding
    """
    for i in range(len(data)):
        # Check if the most significant bit (MSB) is 0
        if (data[i] & 0b10000000) == 0:
            # If MSB is 0, it's a single-byte character (ASCII)
            if data[i] <= 128:
                continue
            else:
                return False
        else:
            # If MSB is 1, it's the start of a multi-byte character
            # Determine the number of bytes for this character
            num_bytes = 0
            while (data[i] & (0b10000000 >> num_bytes)) != 0:
                num_bytes += 1

            # Check the number of continuation bytes
            if num_bytes < 2 or num_bytes > 4:
                return False  # Invalid number of continuation bytes

            # Check the following continuation bytes
            for j in range(1, num_bytes):
                i += 1
                if i >= len(data) or (data[i] & 0b11000000) != 0b10000000:
                    return False  # Invalid continuation byte

    return True

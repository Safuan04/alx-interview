#!/usr/bin/python3
"""Define a function named validUTF8"""


def validUTF8(data):
    """Check if a given data set represents a valid UTF-8 encoding"""

    # Iterate through the data
    i = 0
    while i < len(data):
        # Check if the most significant bit (MSB) is 0
        if (data[i] & 0b10000000) == 0:
            # If MSB is 0, it's a single-byte character (ASCII)
            if data[i] <= 128:
                i += 1
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

        i += 1

    return True

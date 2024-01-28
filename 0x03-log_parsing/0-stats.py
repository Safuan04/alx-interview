#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
import sys


psble_status_code = [200, 301, 400, 401, 403, 404, 405, 500]
status_codes = {}
file_size = 0
counter = 10
i = 0
line_read = 0


def print_stats(f_size, dict):
    """prints the log stats"""
    print('File size: {}'.format(f_size))
    stts_code_sorted = {
        key: val for key, val in sorted(dict.items(),
                                        key=lambda ele: ele[0])}
    for key in stts_code_sorted.keys():
        print('{}: {}'.format(key, stts_code_sorted[key]))


try:
    for line in sys.stdin:
        elements = line.split(' ')
        try:
            size = int(elements[-1])
            stat_code = int(elements[-2])
        except (IndexError, TypeError, ValueError):
            continue
        if len(elements) != 9:
            continue
        if i < counter:
            if stat_code not in status_codes:
                if stat_code in psble_status_code:
                    status_codes[stat_code] = 1
                else:
                    continue
            else:
                status_codes[stat_code] += 1
            file_size += size
            counter -= 1
        else:
            print_stats(file_size, status_codes)
            counter = 10
    print_stats(file_size, status_codes)

except KeyboardInterrupt:
    print_stats(file_size, status_codes)
    raise

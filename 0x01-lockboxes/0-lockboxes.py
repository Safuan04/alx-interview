#!/usr/bin/python3
"""Defining canUnlockAll function"""


def canUnlockAll(boxes):
    """This is a function that returns True if all boxes
        can be opened, else return False"""
    if not boxes:
        return False

    # Initialize a set to track the opened boxes
    opened_boxes = {0}

    # Initialize a set to track the keys that need to be checked
    keys_to_check = set(boxes[0])

    # Continue checking boxes until no more keys are left to check
    while keys_to_check:
        key = keys_to_check.pop()

        # Check if the key opens a box that hasn't been opened yet
        if key < len(boxes) and key not in opened_boxes:
            opened_boxes.add(key)
            keys_to_check.update(boxes[key])

    # Check if all boxes have been opened
    return len(opened_boxes) == len(boxes)

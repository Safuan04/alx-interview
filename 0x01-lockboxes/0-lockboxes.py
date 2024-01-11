#!/usr/bin/python3
def canUnlockAll(boxes):
    if not boxes or not boxes[0]:
        return False  # First box is not unlocked

    n = len(boxes)
    unlocked_boxes = {0}  # Set to keep track of unlocked boxes

    def explore(box_index):
        for key in boxes[box_index]:
            if key not in unlocked_boxes and 0 <= key < n:
                unlocked_boxes.add(key)
                explore(key)

    explore(0)  # Start exploring from the first box

    return len(unlocked_boxes) == n
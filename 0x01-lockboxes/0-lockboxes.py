#!/usr/bin/python3
"""a method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened given the keys inside them.

    Parameters:
    boxes: A list index represents a box,& each box contains a list of keys.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    keys = [0]

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if 0 <= key < n and not opened[key]:
                opened[key] = True
                keys.append(key)

    return all(opened)

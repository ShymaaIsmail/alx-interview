#!/usr/bin/python3
""" Lock Boxes Problem"""


def recheck_locked_boxes(boxes, keys):
    """ recheck_locked_boxes """
    new_keys = set()
    for k, box in boxes.items():
        if k in keys:
            for key in box:
                if key not in keys:
                    new_keys.add(key)
    return new_keys


def canUnlockAll(boxes):
    """ canUnlockAll can unlock all box function"""
    if type(boxes) is not list:
        return False
    elif len(boxes) == 0:
        return False
    keys = set()
    keys.add(0)
    new_keys = set()
    locked_boxes = {}
    for index, box in enumerate(boxes):
        if index in keys:
            for key in box:
                keys.add(key)
        else:
            locked_boxes[index] = box
    new_keys = recheck_locked_boxes(locked_boxes, keys)
    while new_keys:
        keys.update(new_keys)
        new_keys = recheck_locked_boxes(locked_boxes, keys)

    return len(keys) == len(boxes)

#!/usr/bin/python3
""" Lock Boxes Problem"""


def recheck_locked_boxes(boxes, keys):
    """ recheck_locked_boxes """
    for k, box in boxes.items():
        if k in keys:
            for key in box:
                keys.add(key)
    return keys


def canUnlockAll(boxes):
    """ canUnlockAll can unlock all box function"""
    keys = set()
    keys.add(0)
    locked_boxes = {}
    for index, box in enumerate(boxes):
        if index in keys:
            for key in box:
                keys.add(key)
        else:
            locked_boxes[index] = box
    recheck_locked_boxes(locked_boxes, keys)
    return len(keys) == len(boxes)

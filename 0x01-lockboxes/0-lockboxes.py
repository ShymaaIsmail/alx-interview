#!/usr/bin/python3
""" Lock Boxes Problem"""
def canUnlockAll(boxes):
    """ canUnlockAll can unlock all box function"""
    keys = set()
    keys.add(0)
    locked_boxes = [[]]
    for index, box in enumerate(boxes):
        if index in keys:
            for key in box:
                keys.add(key)
        else:
            locked_boxes.append(box)
    return len(keys) == len(boxes)

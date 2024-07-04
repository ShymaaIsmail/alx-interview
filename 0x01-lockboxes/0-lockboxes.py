#!/usr/bin/python3
""" Lock Boxes Problem"""

def open_locked_boxes(boxes, keys ):
    """open_locked_boxes"""
    for index, box in enumerate(boxes):
        print(f"index: {index}")
        print(f"keys:  {keys}")
        print(f"box:   {box}")
        if index in keys:
            for key in box:
                keys.add(key)
    return keys

def canUnlockAll(boxes):
    """ canUnlockAll can unlock all box function"""
    keys = set()
    keys.add(0)
    locked_boxes = [[]]
    for index, box in enumerate(boxes):
        print(f"kindex: {index}")
        print(f"kkeys:  {keys}")
        print(f"kbox:   {box}")
        if index in keys:
            for key in box:
                keys.add(key)
        else:
            locked_boxes.append(box)
    return len(keys) == len(boxes)

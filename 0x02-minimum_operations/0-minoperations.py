#!/usr/bin/python3
"""Solution for Minimum Operations Problem"""


def minOperations(n: int) -> int:
    """Return the minimum number of operations to reach n characters"""
    operations_count = 0
    if 1 <= n <= 10**6:
        operations_count = 1

    return operations_count

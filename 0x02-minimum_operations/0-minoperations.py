#!/usr/bin/python3
"""Solution for Minimum Operations Problem"""


def minOperations(n: int) -> int:
    """Return the minimum number of operations to reach n characters"""
    operations_count = 0
    result = 0
    if 1 <= n <= 10**6:
        while (result < n):
            if (n + result) % 2 == 0:
                result = result * 2 if result > 0 else result + 1
            else:
                result += 1
            operations_count += 1

    return operations_count


#!/usr/bin/python3
"""Solution for Minimum Operations Problem"""


def minOperations(n: int) -> int:
    """Return the minimum number of operations to reach n characters"""
    operations_count = 0
    total = 0
    if 1 <= n <= 10**6:
        while (total < n):
            if n % 2 == 0 and total % 2 == 0 or n % 2 != 0 and total % 2 != 0:
                temp_total = total * 2 if total > 0 else total + 1
                total = temp_total if temp_total <= n else total + 1
            else:
                total += 1
            operations_count += 1

            print(total)

    return operations_count

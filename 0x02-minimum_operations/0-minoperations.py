#!/usr/bin/python3
"""Solution for Minimum Operations Problem"""


import math


def minOperations(n: int) -> int:
    """Return the minimum number of operations to reach n characters"""
    if n <= 1:
        return 0
    
    dp = [float('inf')] * (n + 1)
    dp[1] = 0
    
    for i in range(2, n + 1):
        for j in range(1, int(math.sqrt(i)) + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + (i // j))
                if j != 1:
                    dp[i] = min(dp[i], dp[i // j] + j)
    
    return dp[n]

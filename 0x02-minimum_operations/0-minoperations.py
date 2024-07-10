#!/usr/bin/python3
"""Solution for Minimum Operations Problem"""


def minOperations(n: int) -> int:
    """Return the minimum number of operations to reach n characters"""
    if 1 <= n <= 10**6:
        dp = [float('inf')] * (n + 1)
        dp[1] = 0
        for i in range(2, n + 1):
            for j in range(1, i // 2 + 1):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i // j)
        return dp[n]
    else:
        return 0

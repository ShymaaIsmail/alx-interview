#!/usr/bin/python3
"""
Module for the makeChange function.
"""

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Parameters:
    coins (list): A list of coin denominations.
    total (int): The total amount to achieve with the fewest coins.

    Returns:
    int: The minimum number of coins needed to achieve the total, or -1 if it is not possible.
    """
    if total <= 0:
        return 0

    # Initialize dp array with infinity for all values except dp[0]
    dp = [0] + [float('inf')] * total

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

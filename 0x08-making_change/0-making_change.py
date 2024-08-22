#!/usr/bin/python3
"""Module for Making Change.
"""


def makeChange(coins, total):
    """Calculates the fewest number of coins
     needed to meet a given total.
    Args:
        coins (list[int]): A list of coin values.
        total (int): The total amount of money to make.

    Returns:
        int: The fewest number of coins needed to meet the total.
    """
    # Edge case: if total is 0 or less, no coins are needed
    if total <= 0:
        return 0

    # Initialize a list to store the minimum coins needed
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # 0 coins are needed to make 0 total

    # Loop through each coin and update the dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity,
    return dp[total] if dp[total] != float('inf') else -1

#!/usr/bin/python3
"""make changes"""


def makeChange(coins, total):
    ""making changes"
    if total <= 0:
        return 0

    # Initialize the dp list with infinity
    dp = [float('inf')] * (total + 1)
    
    # Base case
    dp[0] = 0

    # Update dp list
    for coin in coins:
        for amount in range(coin, total + 1):
            if dp[amount - coin] != float('inf'):
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, return -1
    return dp[total] if dp[total] != float('inf') else -1

#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number
    # of coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through all possible amounts from 1 to total
    for i in range(1, total + 1):
        # Iterate through all coin denominations
        for coin in coins:
            # If the current coin value is less than or
            # equal to the current amount
            if coin <= i:
                # Update the minimum number of coins needed
                # for the current amount
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still float('inf'), it means
    # the total cannot be met by any combination of coins
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]

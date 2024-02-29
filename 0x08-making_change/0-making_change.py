#!/usr/bin/python3
"""Defining makeChange function"""


def makeChange(coins, total):
    """ Given a pile of coins of different values,
    -   determine the fewest number of coins needed
    -   to meet a given amount total
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    num_coins = 0
    remaining_total = total
    i = 0
    while remaining_total > 0 and i < len(coins):
        if coins[i] <= remaining_total:
            num_coins += remaining_total // coins[i]
            remaining_total %= coins[i]
        i += 1

    if remaining_total > 0:
        return -1
    else:
        return num_coins

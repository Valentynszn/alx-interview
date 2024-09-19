#!/usr/bin/python3
"""README has the details"""


def makeChange(coins, total):
    """
        Determines the fewest number of coins
        needed to meet a given amount total
    """
    if total < 1:
        return 0

    coins = sorted(coins, reverse=True)
    numCoins = len(coins)
    count = 0
    i = 0

    while i < numCoins:
        while total - coins[i] >= 0:
            count += 1
            total -= coins[i]
        if total == 0:
            return count
        i += 1

    return - 1

#!/usr/bin/python3
"""
minimum operation module
"""


def minOperations(n):
    """
    this method to find true boxes
    """

    if n <= 1:
        return 0
    for iter in range(2, n + 1):
        if n % iter == 0:
            return (minOperations(int(n/iter)) + iter)

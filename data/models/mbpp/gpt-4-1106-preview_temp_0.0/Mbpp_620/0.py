"""
Write a function to find the size of the largest subset of a list of numbers so that every pair is divisible.
assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
"""


import math

def largest_divisible_pair_subset(arr):
    n = len(arr)
    arr.sort(reverse=True)
    dp = [1 for i in range(n)]

    for i in range(1, n):
        for j in range(i):
            if arr[j] % arr[i] == 0:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

assert largest_divisible_pair_subset([1, 3, 6, 13, 17, 18]) == 4

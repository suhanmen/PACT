"""
Write a function that takes an array and finds the maximum sum of a bitonic subsequence for the given array, where a sequence is bitonic if it is first increasing and then decreasing.
assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
"""


import numpy as np

def max_sum(arr):
    n = len(arr)
    inc = np.zeros(n)
    dec = np.zeros(n)

    # Initialize increasing and decreasing sequences
    for i in range(n):
        inc[i] = arr[i]
        dec[i] = arr[i]

    # Fill increasing sequence
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and inc[i] < inc[j] + arr[i]:
                inc[i] = inc[j] + arr[i]

    # Fill decreasing sequence
    for i in range(n-2, -1, -1):
        for j in range(n-1, i, -1):
            if arr[i] > arr[j] and dec[i] < dec[j] + arr[i]:
                dec[i] = dec[j] + arr[i]

    # Find the maximum sum of bitonic subsequence
    max_sum = 0
    for i in range(n):
        max_sum = max(max_sum, inc[i] + dec[i] - arr[i])

    return max_sum

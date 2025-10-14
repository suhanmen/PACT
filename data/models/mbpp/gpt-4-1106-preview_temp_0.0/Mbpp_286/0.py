"""
Write a function to find the largest sum of a contiguous array in the modified array which is formed by repeating the given array k times.
assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
"""


import itertools

def max_sub_array_sum_repeated(arr, n, k):
    # Repeat the array k times
    extended_arr = list(itertools.chain.from_iterable(itertools.repeat(arr, k)))
    # Initialize variables to store the maximum sum and current sum
    max_sum = float('-inf')
    current_sum = 0

    # Iterate over the extended array to find the maximum subarray sum
    for num in extended_arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage
# assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30

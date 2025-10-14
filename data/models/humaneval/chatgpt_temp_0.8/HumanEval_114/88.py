import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    current_min_sum = float('inf')
    current_sum = 0

    for num in nums:
        current_sum = min(current_sum + num, num)
        current_min_sum = min(current_min_sum, current_sum)

    return current_min_sum

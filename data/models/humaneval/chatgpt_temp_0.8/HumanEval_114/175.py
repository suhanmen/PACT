import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    n = len(nums)
    min_ending_here = float('inf')
    min_so_far = float('inf')
    for i in range(n):
        if min_ending_here > 0:
            min_ending_here = nums[i]
        else:
            min_ending_here += nums[i]
        min_so_far = min(min_so_far, min_ending_here)
    return min_so_far

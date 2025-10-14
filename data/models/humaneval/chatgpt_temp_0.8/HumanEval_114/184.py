import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_so_far = math.inf
    min_ending_here = 0
    for i in range(len(nums)):
        min_ending_here += nums[i]
        if min_so_far > min_ending_here:
            min_so_far = min_ending_here
        if min_ending_here > 0:
            min_ending_here = 0
    return min_so_far

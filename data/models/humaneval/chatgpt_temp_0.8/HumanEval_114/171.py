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
    min_ending_here = nums[0]
    min_so_far = nums[0]
    for i in range(1, n):
        min_ending_here = min(nums[i], min_ending_here + nums[i])
        min_so_far = min(min_so_far, min_ending_here)
    return min_so_far

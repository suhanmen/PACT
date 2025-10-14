import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = math.inf
    
    for i in range(len(nums)):
        sub_sum = 0
        for j in range(i, len(nums)):
            sub_sum += nums[j]
            min_sum = min(min_sum, sub_sum)
    
    return min_sum

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
    min_sum = math.inf
    curr_sum = 0
    
    for i in range(n):
        curr_sum += nums[i]
        
        if curr_sum < min_sum:
            min_sum = curr_sum
        
        if curr_sum > 0:
            curr_sum = 0
            
    return min_sum

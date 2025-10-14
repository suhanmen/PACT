import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # initialize variables
    min_sum = math.inf
    current_sum = 0
    
    # loop through nums and update variables
    for num in nums:
        current_sum += num
        min_sum = min(min_sum, current_sum)
        current_sum = max(current_sum, 0)
        
    return min_sum

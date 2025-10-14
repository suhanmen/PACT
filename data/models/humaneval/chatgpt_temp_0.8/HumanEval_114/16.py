import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    current_sum = math.inf # initialize current_sum to infinity
    min_sum = math.inf # initialize min_sum to infinity
    
    for num in nums:
        current_sum = min(current_sum + num, num) # update current_sum
        min_sum = min(min_sum, current_sum) # update min_sum
    
    return min_sum

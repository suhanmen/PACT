import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = math.inf # initialize the minimum sum to positive infinity
    current_sum = 0 # initialize the current sum to zero
    
    for num in nums:
        current_sum += num
        min_sum = min(min_sum, current_sum) # update the minimum sum if necessary
        current_sum = max(current_sum, 0) # reset the current sum if it becomes negative
    
    return min_sum

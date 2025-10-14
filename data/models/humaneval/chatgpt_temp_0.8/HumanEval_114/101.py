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
    current_sum = float('inf')
    min_sum = float('inf')
    
    # loop through each number in the array
    for num in nums:
        # update the current sum
        current_sum = min(num, current_sum + num)
        
        # update the minimum sum
        min_sum = min(min_sum, current_sum)
        
    return min_sum

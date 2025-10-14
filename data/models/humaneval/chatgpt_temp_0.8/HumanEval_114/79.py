import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Initialize minimum sum as infinity
    min_sum = math.inf
    
    # Initialize current sum as 0
    curr_sum = 0
    
    # Loop through the array
    for num in nums:
        # Add current number to current sum
        curr_sum += num
        
        # If current sum is less than minimum sum, update minimum sum
        if curr_sum < min_sum:
            min_sum = curr_sum
        
        # If current sum is negative, reset current sum to 0
        if curr_sum < 0:
            curr_sum = 0
    
    return min_sum

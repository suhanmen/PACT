import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Initialize variables
    min_sum = math.inf
    current_sum = 0
    
    # Loop through array
    for num in nums:
        # Add current number to current sum
        current_sum += num
        # If current sum is negative, set it to 0
        if current_sum < 0:
            current_sum = 0
        # If current sum is less than current minimum sum, update minimum sum
        if current_sum < min_sum:
            min_sum = current_sum
    
    return min_sum

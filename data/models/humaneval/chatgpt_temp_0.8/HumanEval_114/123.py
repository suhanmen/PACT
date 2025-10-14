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
    current_min = math.inf
    current_sum = 0
    
    # Iterate through the array
    for num in nums:
        # Add the current number to the current sum
        current_sum += num
        
        # Check if the current sum is less than the current minimum
        if current_sum < current_min:
            current_min = current_sum
        
        # If the current sum is negative, reset it to 0
        if current_sum < 0:
            current_sum = 0
    
    return current_min

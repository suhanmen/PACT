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
    
    # Loop over the array
    for num in nums:
        # Calculate the current sum
        current_sum += num
        
        # Check if the current sum is less than the minimum sum
        if current_sum < min_sum:
            min_sum = current_sum
        
        # Reset the current sum if it's negative
        if current_sum < 0:
            current_sum = 0
    
    # Return the minimum sum
    return min_sum

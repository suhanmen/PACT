import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    
    # Initialize the minimum sum to be infinity
    min_sum = math.inf
    
    # Loop through the array and keep track of the current sum
    current_sum = 0
    for num in nums:
        current_sum += num
        
        # Update the minimum sum if the current sum is less than it
        if current_sum < min_sum:
            min_sum = current_sum
        
        # If the current sum is negative, reset it to 0
        if current_sum < 0:
            current_sum = 0
    
    # Return the minimum sum
    return min_sum

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
    current_sum = 0
    min_sum = math.inf
    
    # Iterate through the array
    for num in nums:
        # Update the current_sum
        current_sum += num
        
        # If the current_sum is negative, reset it to zero
        if current_sum < 0:
            current_sum = 0
        
        # Update the min_sum if the current_sum is smaller
        if current_sum < min_sum:
            min_sum = current_sum
    
    return min_sum

import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Initialize variables for minimum sum and current sum
    min_sum = math.inf
    current_sum = 0
    
    # Iterate over the input array
    for num in nums:
        # Add the current number to the current sum
        current_sum += num
        
        # If the current sum is less than the minimum sum, update the minimum sum
        if current_sum < min_sum:
            min_sum = current_sum
        
        # If the current sum is negative, reset it to 0 (since we only want non-empty subarrays)
        if current_sum < 0:
            current_sum = 0
    
    # Return the minimum sum
    return min_sum

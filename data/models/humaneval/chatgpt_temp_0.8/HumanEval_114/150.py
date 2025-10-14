import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Initialize variables to keep track of minimum sum and current sum
    # Start with the first element of the array
    min_sum = float('inf')
    curr_sum = nums[0]
    
    # Iterate through the rest of the array
    for i in range(1, len(nums)):
        # Add the current element to the current sum
        curr_sum += nums[i]
        
        # If the current sum is negative, reset it to 0
        if curr_sum < 0:
            curr_sum = 0
        
        # Update the minimum sum if the current sum is smaller
        if curr_sum < min_sum:
            min_sum = curr_sum
    
    return min_sum

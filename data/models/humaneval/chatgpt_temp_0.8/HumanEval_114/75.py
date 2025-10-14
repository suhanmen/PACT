import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Initialize minimum sum and current sum
    min_sum = math.inf
    cur_sum = 0
    
    # Loop through all elements in nums
    for num in nums:
        # Add current element to current sum
        cur_sum += num
        
        # Update min_sum if current sum is less than min_sum
        if cur_sum < min_sum:
            min_sum = cur_sum
        
        # If current sum is negative, reset current sum to 0
        if cur_sum < 0:
            cur_sum = 0
    
    return min_sum

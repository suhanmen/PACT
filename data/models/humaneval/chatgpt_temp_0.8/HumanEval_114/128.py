import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0
    
    # Initialize variables
    curr_sum = 0
    min_sum = math.inf
    
    # Iterate through array
    for num in nums:
        curr_sum += num
        
        # Check if current sum is smaller than minimum sum
        if curr_sum < min_sum:
            min_sum = curr_sum
        
        # Check if current sum is negative
        if curr_sum < 0:
            curr_sum = 0
    
    return min_sum

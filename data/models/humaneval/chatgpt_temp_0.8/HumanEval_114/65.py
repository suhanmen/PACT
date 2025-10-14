import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # initialize variables
    min_sum = math.inf
    current_sum = 0
    
    # loop through array
    for num in nums:
        # add current number to current sum
        current_sum += num
        
        # if current sum is less than minimum sum, update minimum sum
        if current_sum < min_sum:
            min_sum = current_sum
        
        # if current sum becomes negative, reset to zero
        if current_sum < 0:
            current_sum = 0
    
    return min_sum

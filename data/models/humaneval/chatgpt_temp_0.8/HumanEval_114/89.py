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
    curr_sum = 0
    
    # iterate over array
    for num in nums:
        # update current sum
        curr_sum += num
        
        # check if current sum is less than minimum sum
        if curr_sum < min_sum:
            min_sum = curr_sum
        
        # if current sum is negative, reset it to 0
        if curr_sum < 0:
            curr_sum = 0
            
    return min_sum

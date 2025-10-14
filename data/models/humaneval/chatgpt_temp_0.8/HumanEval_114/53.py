import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # initialize min_sum to infinity
    min_sum = math.inf
    
    # initialize current_sum to zero
    current_sum = 0
    
    # loop through the array
    for num in nums:
        # add the current number to the current_sum
        current_sum += num
        
        # if the current_sum is smaller than min_sum, update min_sum
        if current_sum < min_sum:
            min_sum = current_sum
        
        # if the current_sum is negative, reset it to zero
        if current_sum < 0:
            current_sum = 0
    
    # return the min_sum
    return min_sum

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
    current_sum = 0
    min_sum = math.inf
    
    # loop through each element in the array
    for num in nums:
        
        # add the current element to the current sum
        current_sum += num
        
        # update the minimum sum if the current sum is less than the current minimum
        if current_sum < min_sum:
            min_sum = current_sum
        
        # if the current sum is negative, reset it to 0
        if current_sum < 0:
            current_sum = 0
    
    return min_sum

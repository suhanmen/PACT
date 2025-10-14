import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # initialize minimum sum variable to a large number
    min_sum = math.inf
    
    # iterate through all subarrays
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            # calculate sum of current subarray
            subarray_sum = sum(nums[i:j+1])
            # update minimum sum variable
            min_sum = min(min_sum, subarray_sum)
    
    return min_sum

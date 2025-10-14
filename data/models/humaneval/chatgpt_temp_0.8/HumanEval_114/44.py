import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # set a variable to track the minimum subarray sum
    min_sum = math.inf
    
    # loop through each index in the array
    for i in range(len(nums)):
        # set a variable to track the sum of subarrays starting at the current index
        curr_sum = 0
        # loop through each index from the current index to the end of the array
        for j in range(i, len(nums)):
            # add the current value to the current sum
            curr_sum += nums[j]
            # if the current sum is less than the minimum sum, update the minimum sum
            if curr_sum < min_sum:
                min_sum = curr_sum
    
    # return the minimum subarray sum
    return min_sum

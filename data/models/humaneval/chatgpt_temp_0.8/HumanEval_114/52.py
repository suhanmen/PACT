import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # initialize the minimum sum and current sum to be the first element
    min_sum = nums[0]
    curr_sum = nums[0]
    
    # iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # update the current sum to be the maximum of the current element and the current sum plus the current element
        curr_sum = max(nums[i], curr_sum + nums[i])
        # update the minimum sum to be the minimum of the minimum sum and the current sum
        min_sum = min(min_sum, curr_sum)
    
    return min_sum

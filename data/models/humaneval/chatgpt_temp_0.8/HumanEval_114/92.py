import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = math.inf # initialize the minimum sum to positive infinity
    prefix_sum = 0 # initialize the prefix sum to zero
    for num in nums:
        prefix_sum += num # update the prefix sum
        min_sum = min(min_sum, prefix_sum) # update the minimum sum
        prefix_sum = max(prefix_sum, 0) # reset the prefix sum if it becomes negative
    return min_sum

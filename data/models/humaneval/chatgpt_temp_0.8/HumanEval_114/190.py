import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = math.inf # initialize minimum sum to positive infinity
    curr_sum = 0 # initialize current sum to zero
    for num in nums:
        curr_sum += num # add the current number to the current sum
        min_sum = min(min_sum, curr_sum) # update the minimum sum
        curr_sum = max(0, curr_sum) # reset current sum to zero if it becomes negative
    return min_sum

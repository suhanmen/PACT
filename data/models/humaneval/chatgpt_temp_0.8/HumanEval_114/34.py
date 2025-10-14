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
    cur_sum = 0

    # iterate through the array
    for num in nums:
        # update the current sum
        cur_sum += num
        # update the minimum sum if needed
        min_sum = min(min_sum, cur_sum)
        # reset the current sum if it becomes negative
        cur_sum = max(cur_sum, 0)

    return min_sum

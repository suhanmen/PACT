import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = math.inf # initialize min_sum to infinity
    curr_sum = 0 # initialize curr_sum to 0

    for num in nums:
        curr_sum += num # add the current number to curr_sum
        min_sum = min(min_sum, curr_sum) # update min_sum if curr_sum is smaller than min_sum
        curr_sum = max(curr_sum, 0) # reset curr_sum to 0 if it becomes negative

    return min_sum

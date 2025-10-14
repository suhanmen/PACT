import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = math.inf  # set the initial minimum sum as infinity
    current_sum = 0  # set the initial current sum as 0

    for num in nums:
        current_sum += num  # add the current number to the current sum
        min_sum = min(min_sum, current_sum)  # check if the current sum is the new minimum sum
        current_sum = max(current_sum, 0)  # if current sum is negative, start a new sub-array

    return min_sum

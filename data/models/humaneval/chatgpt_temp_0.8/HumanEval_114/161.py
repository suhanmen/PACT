import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = math.inf  # initialize minimum sum to infinity
    current_sum = 0  # initialize current sum to zero
    for num in nums:
        current_sum += num  # add current number to current sum
        min_sum = min(min_sum, current_sum)  # update minimum sum
        if current_sum > 0:  # if current sum becomes positive, reset it to zero
            current_sum = 0
    return min_sum

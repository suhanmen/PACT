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
    curr_sum = 0

    # loop through array
    for num in nums:
        # add current number to sum
        curr_sum += num

        # if current sum is negative, start a new sub-array
        if curr_sum <= 0:
            curr_sum = 0

        # update minimum sum
        min_sum = min(min_sum, curr_sum)

    # return minimum sum
    return min_sum

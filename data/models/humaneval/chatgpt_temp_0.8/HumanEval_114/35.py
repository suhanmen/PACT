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

    # iterate through each element in nums
    for num in nums:
        # add current element to the running total
        curr_sum += num
        # check if the running total is less than the current minimum sum
        if curr_sum < min_sum:
            min_sum = curr_sum
        # if the running total is greater than or equal to zero, reset it
        if curr_sum >= 0:
            curr_sum = 0

    # return the minimum sum
    return min_sum

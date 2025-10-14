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
    current_sum = 0
    
    # loop through nums
    for num in nums:
        # update current sum
        current_sum += num
        # update min_sum if current sum is less than min_sum
        min_sum = min(min_sum, current_sum)
        # reset current_sum to 0 if it's negative
        current_sum = max(current_sum, 0)
    
    return min_sum

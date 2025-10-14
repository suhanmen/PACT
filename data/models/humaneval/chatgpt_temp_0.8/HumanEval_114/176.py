import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0
    
    # initialize variables
    min_sum = math.inf
    curr_sum = 0
    
    # loop through the array
    for num in nums:
        # update current sum
        curr_sum += num
        # update minimum sum if current sum is smaller
        min_sum = min(min_sum, curr_sum)
        # reset current sum if it becomes negative
        curr_sum = max(curr_sum, 0)
    
    return min_sum

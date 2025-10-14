import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Initialize variables
    min_sum = math.inf
    curr_sum = 0
    
    # Iterate through nums and update min_sum and curr_sum
    for num in nums:
        curr_sum += num
        min_sum = min(min_sum, curr_sum)
        curr_sum = max(curr_sum, 0)
    
    return min_sum

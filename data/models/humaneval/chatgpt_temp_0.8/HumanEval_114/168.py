python
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
    current_sum = 0
    min_sum = math.inf
    
    # loop through the array
    for num in nums:
        # update the current sum
        current_sum += num
        
        # update the minimum sum if necessary
        min_sum = min(min_sum, current_sum)
        
        # reset the current sum to 0 if it becomes negative
        current_sum = max(current_sum, 0)
    
    return min_sum

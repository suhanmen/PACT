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
        return None
    
    current_min = math.inf
    current_sum = 0
    
    for num in nums:
        current_sum = min(num, current_sum + num)
        current_min = min(current_min, current_sum)
        
    return current_min

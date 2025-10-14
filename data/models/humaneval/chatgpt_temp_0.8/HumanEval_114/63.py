import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = math.inf
    current_sum = 0
    
    for i in range(len(nums)):
        current_sum += nums[i]
        
        # If current_sum is less than 0, reset to 0
        # Since we want to find the minimum sum, any negative sum is not useful
        if current_sum < 0:
            current_sum = 0
            
        # If current_sum is less than min_sum, update min_sum
        if current_sum < min_sum:
            min_sum = current_sum
            
    return min_sum

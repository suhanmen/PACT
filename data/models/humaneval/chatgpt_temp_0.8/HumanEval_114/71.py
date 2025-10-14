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
    
    # Loop through each element in nums
    for num in nums:
        # Update the current sum to be the maximum of the current element and 
        # the sum of the current element and the previous sum
        curr_sum = max(curr_sum + num, num)
        
        # Update the minimum sum to be the minimum of the current minimum sum and
        # the current sum
        min_sum = min(min_sum, curr_sum)
        
    return min_sum

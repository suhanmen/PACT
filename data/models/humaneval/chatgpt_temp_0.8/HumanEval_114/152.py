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
    
    # Iterate through the array
    for num in nums:
        # Add the current number to the sum
        curr_sum += num
        
        # Update the minimum sum if curr_sum is less than min_sum
        min_sum = min(min_sum, curr_sum)
        
        # Reset curr_sum to 0 if it becomes negative
        curr_sum = max(0, curr_sum)
    
    return min_sum

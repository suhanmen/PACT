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
    
    # Iterate through nums
    for num in nums:
        # Add current num to curr_sum
        curr_sum += num
        # Update min_sum if curr_sum is less than min_sum
        min_sum = min(min_sum, curr_sum)
        # Reset curr_sum to 0 if it becomes negative
        curr_sum = max(curr_sum, 0)
    
    # Return min_sum
    return min_sum

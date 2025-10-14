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
    current_sum = 0
    
    # Iterate through array
    for num in nums:
        # Add current number to sum
        current_sum += num
        # Check if current sum is less than minimum sum so far
        min_sum = min(min_sum, current_sum)
        # Reset current sum to 0 if it's negative
        current_sum = max(current_sum, 0)
    
    # Return minimum sum
    return min_sum

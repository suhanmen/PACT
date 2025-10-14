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
    curr_sum = 0
    min_sum = math.inf
    
    # Iterate through the array
    for num in nums:
        # Update current sum
        curr_sum += num
        
        # Update minimum sum if current sum is smaller
        min_sum = min(min_sum, curr_sum)
        
        # Reset current sum to 0 if it becomes negative
        curr_sum = max(curr_sum, 0)
    
    return min_sum

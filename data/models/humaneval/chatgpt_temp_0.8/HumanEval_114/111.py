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
    
    # Iterate over the array
    for num in nums:
        # Add the current number to the running sum
        curr_sum += num
        
        # Update the minimum sum if the current sum is less than the current minimum
        min_sum = min(min_sum, curr_sum)
        
        # Reset the current sum to 0 if it becomes negative
        curr_sum = max(curr_sum, 0)
    
    # Return the minimum sum
    return min_sum

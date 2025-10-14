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
    # Initialize current sum and minimum sum to the first element of the array
    curr_sum = min_sum = nums[0]
    
    # Loop through the array starting from the second element
    for i in range(1, len(nums)):
        # Calculate the current sum as the maximum of the current element and the current sum plus the current element
        curr_sum = max(nums[i], curr_sum + nums[i])
        # Update the minimum sum if the current sum is less than the current minimum sum
        min_sum = min(min_sum, curr_sum)
    
    return min_sum

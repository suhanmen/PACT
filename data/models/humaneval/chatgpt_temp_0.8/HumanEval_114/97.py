import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Initialize minimum sum and current sum as the first element of the array
    min_sum = nums[0]
    cur_sum = nums[0]
    
    # Loop through the array, starting from the second element
    for i in range(1, len(nums)):
        # Update current sum by adding the current element
        cur_sum += nums[i]
        # If current sum is less than the minimum sum, update the minimum sum
        if cur_sum < min_sum:
            min_sum = cur_sum
        # If the current sum is greater than or equal to zero,
        # reset the current sum to zero
        if cur_sum >= 0:
            cur_sum = 0
    
    # Return the minimum sum
    return min_sum

import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Initialize the minimum sum and current sum as the first element in the array
    min_sum = nums[0]
    curr_sum = nums[0]
    
    # Loop through the remaining elements in the array
    for i in range(1, len(nums)):
        # Update the current sum by adding the current element to it
        curr_sum += nums[i]
        
        # If the current sum is greater than the current element,
        # update the current sum to be the current element
        if curr_sum > nums[i]:
            curr_sum = nums[i]
        
        # If the current sum is less than the minimum sum,
        # update the minimum sum to be the current sum
        if curr_sum < min_sum:
            min_sum = curr_sum
    
    # Return the minimum sum
    return min_sum

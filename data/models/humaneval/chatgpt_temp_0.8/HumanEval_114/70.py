import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Initialize variables to keep track of current and minimum sum
    current_sum = 0
    min_sum = math.inf
    
    # Iterate through the array and calculate current sum
    for num in nums:
        current_sum += num
        
        # If current sum is less than minimum sum, update minimum sum
        if current_sum < min_sum:
            min_sum = current_sum
        
        # If current sum is greater than 0, reset current sum
        if current_sum > 0:
            current_sum = 0
    
    return min_sum

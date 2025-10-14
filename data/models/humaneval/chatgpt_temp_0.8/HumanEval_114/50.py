import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    n = len(nums)
    min_sum = math.inf
    
    # iterate through all possible subarrays and update the minimum sum
    for i in range(n):
        for j in range(i, n):
            curr_sum = sum(nums[i:j+1])
            if curr_sum < min_sum:
                min_sum = curr_sum
    
    return min_sum

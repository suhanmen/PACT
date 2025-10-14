import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # initialize the minimum sum to infinity
    min_sum = math.inf
    
    # iterate over all sub-arrays
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sub_array = nums[i:j+1]
            sub_array_sum = sum(sub_array)
            
            # update the minimum sum if necessary
            if sub_array_sum < min_sum:
                min_sum = sub_array_sum
    
    return min_sum

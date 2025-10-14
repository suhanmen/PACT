import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0
    
    min_sum = math.inf
    subarray_sum = 0
    left = 0
    
    for right in range(len(nums)):
        subarray_sum += nums[right]
        
        while subarray_sum >= 0:
            min_sum = min(min_sum, subarray_sum)
            subarray_sum -= nums[left]
            left += 1
        
    return min_sum

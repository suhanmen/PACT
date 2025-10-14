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
        return None
    
    left, right = 0, 0
    curr_sum = nums[0]
    min_sum = nums[0]
    
    while right < len(nums):
        if curr_sum < min_sum:
            min_sum = curr_sum
        if curr_sum < 0:
            left += 1
            right = left
            if left < len(nums):
                curr_sum = nums[left]
        else:
            right += 1
            if right < len(nums):
                curr_sum += nums[right]
    
    return min_sum

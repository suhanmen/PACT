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
    curr_sum = nums[0]
    min_sum = nums[0]
    for num in nums[1:]:
        curr_sum = min(num, curr_sum + num)
        min_sum = min(min_sum, curr_sum)
    return min_sum

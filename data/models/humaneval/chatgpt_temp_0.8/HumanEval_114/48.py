import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Variable to keep track of minimum sum found so far
    min_sum = math.inf

    # Iterate through all sub-arrays
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            # Calculate sum of sub-array nums[i:j+1]
            sub_array_sum = sum(nums[i:j+1])
            # Update min_sum if sub_array_sum is less than current min_sum
            if sub_array_sum < min_sum:
                min_sum = sub_array_sum

    return min_sum

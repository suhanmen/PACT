"""
Write a python function to find the sum of xor of all pairs of numbers in the given list.
assert pair_xor_Sum([5,9,7,6],4) == 47
"""



def pair_xor_sum(nums, n):
    xor_sum = 0
    for i in range(n):
        for j in range(i+1, n):
            xor_sum += nums[i] ^ nums[j]
    return xor_sum * 2


assert pair_xor_sum([5,9,7,6], 4) == 47

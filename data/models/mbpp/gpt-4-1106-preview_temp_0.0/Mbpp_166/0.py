"""
Write a function that counts the number of pairs of integers in a list that xor to an even number.
assert find_even_pair([5, 4, 7, 2, 1]) == 4
"""



def find_even_pair(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i] ^ nums[j]) % 2 == 0:
                count += 1
    return count

# Example usage
# assert find_even_pair([5, 4, 7, 2, 1]) == 4

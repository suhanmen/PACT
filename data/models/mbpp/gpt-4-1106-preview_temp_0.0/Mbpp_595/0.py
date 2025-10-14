"""
Write a python function to count minimum number of swaps required to convert one binary number represented as a string to another.
assert min_Swaps("1101","1110") == 1
"""


import itertools

def min_Swaps(s1, s2):
    if len(s1) != len(s2) or sorted(s1) != sorted(s2):
        raise ValueError("Strings must be of the same length and have the same number of 0s and 1s")

    swap_count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            swap_index = s2.index(s1[i], i)
            s2 = s2[:i] + s2[swap_index] + s2[i+1:swap_index] + s2[i] + s2[swap_index+1:]
            swap_count += 1
    return swap_count

# Example usage:
# assert min_Swaps("1101","1110") == 1

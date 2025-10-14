"""
Write a python function to find the number of numbers with an odd value when rotating a binary string the given number of times.
assert odd_Equivalent("011001",6) == 3
"""


import collections

def rotate_string(s, n):
    double_s = s + s
    return double_s[n:n+len(s)]

def odd_Equivalent(s, rotations):
    counter = collections.Counter()
    for i in range(rotations):
        rotated_s = rotate_string(s, i)
        counter[rotated_s] += 1
    return sum(1 for key, value in counter.items() if int(key, 2) % 2 != 0)

# Example usage
# assert odd_Equivalent("011001", 6) == 3

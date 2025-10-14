"""
Write a python function to find the minimum number of rotations (greater than 0) required to get the same string.
assert find_Rotations("aaaa") == 1
"""


import itertools

def find_Rotations(s):
    if len(set(s)) == 1:  # If all characters are the same, 1 rotation is enough
        return 1
    for i in range(1, len(s)):
        if s[i:] + s[:i] == s:
            return i
    return len(s)  # If no rotation yields the same string, it requires full length rotations

# Example usage
# assert find_Rotations("aaaa") == 1

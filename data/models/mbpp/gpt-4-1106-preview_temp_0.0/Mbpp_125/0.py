"""
Write a function to find the maximum difference between the number of 0s and number of 1s in any sub-string of the given binary string.
assert find_length("11000010001") == 6
"""


import itertools

def find_length(binary_string):
    max_diff = 0
    for i in range(len(binary_string)):
        for j in range(i+1, len(binary_string)+1):
            sub_str = binary_string[i:j]
            zeros = sub_str.count('0')
            ones = sub_str.count('1')
            max_diff = max(max_diff, abs(zeros - ones))
    return max_diff

# Example usage
# assert find_length("11000010001") == 6

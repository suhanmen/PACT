"""
Write a function to count the number of characters in a string that occur at the same position in the string as in the English alphabet (case insensitive).
assert count_char_position("xbcefg") == 2
"""


import string

def count_char_position(s):
    count = 0
    for index, char in enumerate(s.lower()):
        if char in string.ascii_lowercase and string.ascii_lowercase.index(char) == index:
            count += 1
    return count

# Example usage:
# result = count_char_position("xbcefg")
# print(result)  # Output: 2

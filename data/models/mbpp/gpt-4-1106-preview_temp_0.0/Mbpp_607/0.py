"""
Write a function to search a string for a regex pattern. The function should return the matching subtring, a start index and an end index.
assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
"""


import re

def find_literals(input_string, pattern):
    match = re.search(pattern, input_string)
    if match:
        return match.group(), match.start(), match.end()
    return None, None, None

# Example usage
# result = find_literals('The quick brown fox jumps over the lazy dog.', 'fox')
# print(result)  # Output should be: ('fox', 16, 19)

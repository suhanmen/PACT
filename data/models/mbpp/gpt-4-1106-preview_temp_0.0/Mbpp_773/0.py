"""
Write a function to find the occurrence and position of the substrings within a string. Return None if there is no match.
assert occurance_substring('python programming, python language','python')==('python', 0, 6)
"""


import re

def occurance_substring(main_string, sub_str):
    matches = list(re.finditer(sub_str, main_string))
    if not matches:
        return None
    first_match = matches[0]
    return (sub_str, first_match.start(), first_match.end())

# Example usage:
# result = occurance_substring('python programming, python language', 'python')
# print(result)  # Output should be: ('python', 0, 6)

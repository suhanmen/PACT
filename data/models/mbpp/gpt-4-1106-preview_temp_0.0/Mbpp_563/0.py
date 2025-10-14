"""
Write a function to extract values between quotation marks from a string.
assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']
"""


import re

def extract_values(s):
    # Use regular expression to find all occurrences of text
    # between quotation marks
    return re.findall(r'"(.*?)"', s)

# Example usage
# values = extract_values('"Python", "PHP", "Java"')
# print(values)  # Output: ['Python', 'PHP', 'Java']

"""
Write a function to find all words which are at least 4 characters long in a string.
assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])
"""


import re

def find_char_long(text):
    # Use regular expression to find words with 4 or more characters
    words = re.findall(r'\b\w{4,}\b', text)
    return words

# Example usage
# words = find_char_long('Please move back to stream')
# print(set(words))

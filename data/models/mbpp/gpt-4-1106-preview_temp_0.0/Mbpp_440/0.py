"""
Write a function to find the first adverb and their positions in a given sentence.
assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')
"""


import re

def find_adverb_position(sentence):
    # Regular expression to find adverbs typically ending in 'ly'
    match = re.search(r'\b\w+ly\b', sentence)
    if match:
        # Start and end positions of the matched adverb
        start, end = match.span()
        # The adverb itself
        adverb = match.group()
        return start, end, adverb
    else:
        return None

# Example usage:
# position = find_adverb_position("clearly!! we can see the sky")
# print(position)  # Output should be (0, 7, 'clearly')

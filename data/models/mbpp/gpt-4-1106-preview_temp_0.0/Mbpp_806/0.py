"""
Write a function to find maximum run of uppercase characters in the given string.
assert max_run_uppercase('GeMKSForGERksISBESt') == 5
"""


import re

def max_run_uppercase(s):
    # Find all runs of uppercase letters
    runs = re.findall(r'[A-Z]+', s)
    # Calculate the length of each run
    max_run_length = max(len(run) for run in runs) if runs else 0
    return max_run_length

# Example usage
assert max_run_uppercase('GeMKSForGERksISBESt') == 5

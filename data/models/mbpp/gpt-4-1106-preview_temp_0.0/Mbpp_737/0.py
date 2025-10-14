"""
Write a function to check whether the given string is starting with a vowel or not using regex.
assert check_str("annie")
"""


import re

def check_str(input_str):
    # Define the regex pattern to check if the string starts with a vowel
    pattern = r'^[aeiouAEIOU]'
    # Use re.match to check if the pattern matches the start of the string
    if re.match(pattern, input_str):
        return True
    else:
        return False

# Example usage:
# result = check_str("annie")
# print(result)  # Output: True

# Assert statement
assert check_str("annie") == True

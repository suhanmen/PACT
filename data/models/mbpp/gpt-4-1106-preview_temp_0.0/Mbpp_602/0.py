"""
Write a python function to find the first repeated character in a given string.
assert first_repeated_char("abcabc") == "a"
"""



def first_repeated_char(input_string):
    seen = set()
    for char in input_string:
        if char in seen:
            return char
        seen.add(char)
    return None

# Example usage:
# assert first_repeated_char("abcabc") == "a"

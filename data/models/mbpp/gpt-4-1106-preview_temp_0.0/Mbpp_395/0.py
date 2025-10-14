"""
Write a python function to find the first non-repeated character in a given string.
assert first_non_repeating_character("abcabc") == None
"""



def first_non_repeating_character(s):
    char_order = []
    counts = {}
    for c in s:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
            char_order.append(c)
    for c in char_order:
        if counts[c] == 1:
            return c
    return None

assert first_non_repeating_character("abcabc") == None

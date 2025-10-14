"""
Write a function to remove characters from the first string which are present in the second string.
assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
"""



def remove_dirty_chars(s1, s2):
    return ''.join(filter(lambda char: char not in s2, s1))

assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'

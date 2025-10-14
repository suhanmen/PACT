# CANNOT PARSE CODE SNIPPET
def cycpattern_check(a, b):
    if len(a) < len(b):  # return False if the length of b is greater than a
        return False
    a += a  # concatenate the first word with itself to cover all possible rotations
    for i in range(len(a) - len(b) + 1):  # loop through all possible substrings of length b in a
        if a[i:i+len(b)] == b:  # check if the substring matches b
            return True
    return False  # return False if b is not a substring of a or any of its rotations

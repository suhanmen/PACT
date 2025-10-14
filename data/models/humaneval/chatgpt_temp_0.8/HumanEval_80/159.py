def is_happy(s):
    if len(s) < 3:  # if the string is less than 3 in length, it can't be happy
        return False
    for i in range(len(s) - 2):  # iterate through each group of 3 characters in the string
        if s[i] == s[i+1] or s[i] == s[i+2] or s[i+1] == s[i+2]:
            # if any two of the three characters are the same, the string is not happy
            return False
    return True  # if we made it through the loop without finding any repeated characters, the string is happy

def is_happy(s):
    if len(s) < 3:    # if length is less than 3, return False
        return False
    for i in range(len(s)-2):    # iterate through string, checking if every 3 consecutive letters are distinct
        if s[i] == s[i+1] or s[i] == s[i+2] or s[i+1] == s[i+2]:
            return False
    return True    # if all 3 consecutive letters are distinct, return True

def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    """
    if len(s) < 3: # if the length of the string is less than 3, it cannot be happy
        return False
    for i in range(0, len(s)-2): # iterate through every 3 consecutive letters in the string
        if s[i] == s[i+1] or s[i+1] == s[i+2] or s[i+2] == s[i]: # if any two of the three letters are the same, the string is not happy
            return False
    return True # if the function hasn't returned False by now, the string is happy

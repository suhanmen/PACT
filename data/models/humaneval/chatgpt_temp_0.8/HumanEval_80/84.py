def is_happy(s):
    if len(s) < 3:
        return False # If string length is less than 3, it can't be happy
    for i in range(len(s)-2): # Check every 3 consecutive letters
        if s[i] == s[i+1] or s[i+1] == s[i+2] or s[i] == s[i+2]:
            return False # If there are any repeating letters, the string is not happy
    return True # If every 3 consecutive letters are distinct, the string is happy

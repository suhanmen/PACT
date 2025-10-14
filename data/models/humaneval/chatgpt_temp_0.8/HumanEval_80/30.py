def is_happy(s):
    if len(s) < 3:  # Check if the length of the string is less than 3
        return False
    for i in range(len(s)-2):  # Iterate over the string up to the 3rd last character
        if s[i] == s[i+1] or s[i] == s[i+2] or s[i+1] == s[i+2]:  # Check if any 3 consecutive characters are not distinct
            return False
    return True  # If no such 3 consecutive characters exist in the string, then it is happy

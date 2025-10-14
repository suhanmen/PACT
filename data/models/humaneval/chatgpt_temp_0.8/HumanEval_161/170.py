def solve(s):
    # Check if the string contains any letters
    if not any(c.isalpha() for c in s):
        # Reverse the string if it contains no letters
        return s[::-1]
    
    # Reverse the case of each letter in the string
    result = ""
    for c in s:
        if c.isalpha():
            if c.islower():
                result += c.upper()
            else:
                result += c.lower()
        else:
            result += c
    
    return result

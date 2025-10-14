def solve(s):
    if not any(c.isalpha() for c in s): # If the string contains no letters
        return s[::-1] # Reverse the string
    
    # If the string contains letters, reverse their case
    result = ""
    for c in s:
        if c.isalpha():
            result += c.lower() if c.isupper() else c.upper()
        else:
            result += c
    
    return result

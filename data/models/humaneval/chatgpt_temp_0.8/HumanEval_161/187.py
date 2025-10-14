def solve(s):
    # Check if string contains any letters
    if any(c.isalpha() for c in s):
        # Reverse case of letters
        s = ''.join(c.lower() if c.isupper() else c.upper() if c.islower() else c for c in s)
    else:
        # Reverse the string
        s = s[::-1]
    return s

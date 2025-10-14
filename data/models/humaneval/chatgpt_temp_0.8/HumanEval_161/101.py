def solve(s):
    # check if string s contains letters
    if any(char.isalpha() for char in s):
        # if s contains letters, reverse their case
        return ''.join([char.lower() if char.isupper() else char.upper() for char in s])
    else:
        # if s doesn't contain letters, reverse the string
        return s[::-1]

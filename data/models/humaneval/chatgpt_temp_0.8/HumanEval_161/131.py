def solve(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("ab") = "AB"
    solve("#a@C") = "#A@c"
    """

    # Check if the string contains letters
    letters = [c for c in s if c.isalpha()]

    if not letters:
        # If the string contains no letters, reverse it
        return s[::-1]

    # Otherwise, process the letters
    result = []
    for c in s:
        if c.isalpha():
            # Reverse the case of letters
            if c.isupper():
                result.append(c.lower())
            else:
                result.append(c.upper())
        else:
            # Keep non-letters as they are
            result.append(c)

    return ''.join(result)

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
    reversed_letters = ''
    reversed_string = ''
    for c in s:
        if c.isalpha():
            if c.islower():
                reversed_letters += c.upper()
            else:
                reversed_letters += c.lower()
        else:
            reversed_letters += c
    if not any(c.isalpha() for c in s):
        reversed_string = s[::-1]
    return reversed_letters if len(reversed_letters) > 0 else reversed_string

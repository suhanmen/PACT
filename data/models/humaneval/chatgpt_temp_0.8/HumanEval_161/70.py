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
    new_s = ""
    has_letter = False
    for c in s:
        if c.isalpha():
            new_s += c.lower() if c.isupper() else c.upper()
            has_letter = True
        else:
            new_s += c
    if not has_letter:
        new_s = new_s[::-1]
    return new_s

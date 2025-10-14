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
    new_s = ''
    has_letter = False
    for char in s:
        if char.isalpha():
            has_letter = True
            if char.isupper():
                new_s += char.lower()
            else:
                new_s += char.upper()
        else:
            new_s += char
    if not has_letter:
        new_s = new_s[::-1]
    return new_s

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
    letters = 0
    for i in s:
        if i.isalpha():
            if i.isupper():
                new_s += i.lower()
            else:
                new_s += i.upper()
            letters += 1
        else:
            new_s += i
    if letters == 0:
        new_s = new_s[::-1]
    return new_s

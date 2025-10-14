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
    has_letters = False
    for i in range(len(s)):
        if s[i].isalpha():
            has_letters = True
            if s[i].islower():
                new_s += s[i].upper()
            else:
                new_s += s[i].lower()
        else:
            new_s += s[i]
    if not has_letters:
        new_s = new_s[::-1]
    return new_s

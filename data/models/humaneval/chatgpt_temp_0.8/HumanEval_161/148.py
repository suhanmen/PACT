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
    new_str = ""
    for i in s:
        if i.isalpha():
            if i.islower():
                new_str += i.upper()
            else:
                new_str += i.lower()
        else:
            new_str += i
    if new_str.isalpha():
        return new_str[::-1]
    else:
        return new_str[::-1]

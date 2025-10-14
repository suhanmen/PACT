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
    letters = 0
    for char in s:
        if char.isalpha():
            letters += 1

    if letters == 0:
        return s[::-1]

    new_string = ""
    for char in s:
        if char.isalpha():
            if char.isupper():
                new_string += char.lower()
            else:
                new_string += char.upper()
        else:
            new_string += char

    return new_string

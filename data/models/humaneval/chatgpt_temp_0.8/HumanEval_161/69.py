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

    letters = ""
    for char in s:
        if char.isalpha():
            if char.islower():
                letters += char.upper()
            else:
                letters += char.lower()
        else:
            letters += char

    if not any(char.isalpha() for char in s):
        return letters[::-1]

    return letters

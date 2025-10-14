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
    result = ""

    for i in s:
        if i.isalpha():
            letters += 1
            if i.isupper():
                result += i.lower()
            else:
                result += i.upper()
        else:
            result += i

    if letters == 0:
        result = result[::-1]

    return result

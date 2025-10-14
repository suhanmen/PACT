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
    if not any(c.isalpha() for c in s):
        # if no letters in string, reverse the string
        return s[::-1]
    else:
        # if there are letters in string, reverse their case
        result = ""
        for c in s:
            if c.isalpha():
                if c.islower():
                    result += c.upper()
                else:
                    result += c.lower()
            else:
                result += c
        return result

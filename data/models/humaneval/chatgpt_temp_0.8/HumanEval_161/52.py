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
    result = ""
    letters_count = 0
    for char in s:
        if char.isalpha():
            letters_count += 1
            if char.isupper():
                result += char.lower()
            else:
                result += char.upper()
        else:
            result += char
    if letters_count == 0:
        result = result[::-1]
    return result

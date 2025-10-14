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
    new_string = ""
    has_letters = False
    for i in s:
        if i.isalpha():
            has_letters = True
            if i.islower():
                new_string += i.upper()
            else:
                new_string += i.lower()
        else:
            new_string += i
    if not has_letters:
        new_string = new_string[::-1]
    return new_string

def solve(s):
    new_s = ""
    letters_exist = False
    for c in s:
        if c.isalpha():
            letters_exist = True
            if c.islower():
                new_s += c.upper()
            else:
                new_s += c.lower()
        else:
            new_s += c
    if not letters_exist:
        new_s = s[::-1]
    return new_s

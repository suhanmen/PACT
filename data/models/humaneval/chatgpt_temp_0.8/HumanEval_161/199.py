def solve(s):
    new_s = ""
    contains_letter = False
    for c in s:
        if c.isalpha():
            contains_letter = True
            if c.islower():
                new_s += c.upper()
            else:
                new_s += c.lower()
        else:
            new_s += c
    if not contains_letter:
        new_s = new_s[::-1]
    return new_s

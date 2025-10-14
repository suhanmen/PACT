def solve(s):
    new_s = ""
    has_letters = False
    for c in s:
        if c.isalpha():
            has_letters = True
            if c.isupper():
                new_s += c.lower()
            else:
                new_s += c.upper()
        else:
            new_s += c
    if not has_letters:
        new_s = s[::-1]
    return new_s

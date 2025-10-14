def solve(s):
    new_s = ''
    for c in s:
        if c.isalpha():
            if c.isupper():
                new_s += c.lower()
            else:
                new_s += c.upper()
        else:
            new_s += c
    if not any(c.isalpha() for c in s):
        new_s = new_s[::-1]
    return new_s

def solve(s):
    res = ""
    has_letter = False
    for c in s:
        if c.isalpha():
            has_letter = True
            if c.islower():
                res += c.upper()
            else:
                res += c.lower()
        else:
            res += c
    if not has_letter:
        res = res[::-1]
    return res

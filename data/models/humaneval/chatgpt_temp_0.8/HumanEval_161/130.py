def solve(s):
    letters = 0
    for c in s:
        if c.isalpha():
            letters += 1
    if letters == 0:
        return s[::-1]
    else:
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
